#!/usr/bin/env python3
"""List recent NSFC grant numbers acknowledged by papers on a topic (OpenAlex).

Fills part of the kd.nsfc.cn 结题库 blind spot: in-progress projects that have
already published. Grant titles are not in OpenAlex; resolve them in kd 资助项目检索.
"""

import argparse
import collections
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

NSFC = "F4320321001"  # OpenAlex funder id of NSFC
GRANT = re.compile(r"[1-9U]\d{7}")  # 8-char 批准号; characters 2-3 are the approval year


def fetch(terms, since, max_works, api_key):
    works, total = [], None
    for page in range(1, max_works // 100 + 1):
        query = {
            "filter": f"funders.id:{NSFC},from_publication_date:{since},title_and_abstract.search:{terms}",
            "sort": "relevance_score:desc",
            "select": "title,publication_year,doi,awards,authorships",
            "per_page": 100,
            "page": page,
        }
        if api_key:
            query["api_key"] = api_key
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(query)
        request = urllib.request.Request(url, headers={"User-Agent": "nsfc-benzi-audit"})
        with urllib.request.urlopen(request, timeout=60) as response:
            data = json.load(response)
        total = data["meta"]["count"]
        works += data["results"]
        if len(works) >= total:
            break
    return works, total


def grants(works, first_year, last_year):
    found = collections.defaultdict(list)
    for work in works:
        for award in work.get("awards") or []:
            number = (award.get("funder_award_id") or "").strip()
            if award.get("funder_id", "").endswith(NSFC) and GRANT.fullmatch(number):
                if first_year <= 2000 + int(number[1:3]) <= last_year and work not in found[number]:
                    found[number].append(work)
    return found


def render(terms, since, found, scanned, total):
    today = datetime.date.today().isoformat()
    lines = [
        f"检索式（标题+摘要）：{terms}；资助方：NSFC；论文发表自 {since}；查询日期 {today}；来源 OpenAlex",
        f"扫描论文 {scanned} / {total} 篇；命中批准号 {len(found)} 个"
        + ("（未扫完，计数为下限）" if scanned < total else ""),
        "",
        "| 批准号 | 批准年 | 致谢论文数 | 代表论文（年份 题名 · 第一作者单位） |",
        "| --- | --- | --- | --- |",
    ]
    for number, papers in sorted(found.items(), key=lambda kv: (-int(kv[0][1:3]), -len(kv[1]))):
        shown = []
        for work in papers[:3]:
            first = (work.get("authorships") or [{}])[0]
            place = ((first.get("institutions") or [{}])[0]).get("display_name") or "单位未知"
            title = (work.get("title") or "").replace("|", "/")[:90]
            shown.append(f"{work.get('publication_year')} {title} · {place}")
        lines.append(f"| {number} | 20{number[1:3]} | {len(papers)} | {'<br>'.join(shown)} |")
    lines += [
        "",
        "致谢常顺带列出与本题无关的基金：逐个看论文再判断是否近邻。项目名称、负责人以 kd 资助项目检索按批准号核对为准。",
        "未发表论文的在研项目、只发中文期刊的项目不在此表；零命中不证明无人在做。",
    ]
    return "\n".join(lines)


def main():
    this_year = datetime.date.today().year
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", help='title/abstract query, e.g. \'"phase bias" InSAR\'; never paste unsubmitted draft text')
    parser.add_argument("--since", default=f"{this_year - 3}-01-01", help="paper publication date floor")
    parser.add_argument("--years", default=f"{this_year - 5}-{this_year}", help="approval-year range, e.g. 2021-2025")
    parser.add_argument("--max-works", type=int, default=500)
    args = parser.parse_args()
    first, last = (int(y) for y in args.years.split("-"))
    if "," in args.terms:
        parser.error("terms must not contain commas (OpenAlex filter separator)")
    try:
        works, total = fetch(args.terms, args.since, args.max_works, os.environ.get("OPENALEX_API_KEY"))
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError) as exc:
        print(f"查询失败（不是零命中）：{exc}", file=sys.stderr)
        return 2
    print(render(args.terms, args.since, grants(works, first, last), len(works), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
