"""Replay index mechanics on two synthetic sources and a revision.

Checkpoint conclusions are predetermined fixture text, not a new semantic review.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--helper", type=Path, required=True)
parser.add_argument("--work-dir", type=Path, required=True, help="A new directory for synthetic inputs and results")
args = parser.parse_args()
HELPER = args.helper.resolve(strict=True)
BASE = args.work_dir.resolve()
BASE.mkdir(parents=True, exist_ok=False)
RUN = BASE / 'run'
RUN.mkdir()
SOURCE = RUN / 'sources'
SOURCE.mkdir()
WORK = RUN / 'review-work'
SNAP = RUN / 'snapshots'
SNAP.mkdir()
MAIN = SOURCE / '正文.txt'
ANNEX = SOURCE / '附录 条件.txt'
LOG = []

main_text = '# 选定正文 v1\n\n这是虚构的流程测试材料，不用于任何科学结论。正文与《附录 条件.txt》共同组成当前供审核的材料。\n\n## 科学问题与目标\n\nQ1：在限定对象内，描述因素变化与观测量变化的关系。Q2：识别该关系在哪些预先列出的条件下不再成立。两者均不承诺因果机制。\n\n## 研究任务\n\nT1：通过条件表组织观测并估计上述关系。Q2 的支撑方式见附录“任务补充”，不单列第二项任务。\n\n## 时间安排\n\n项目第3个月使用唯一的观测设备 E 开始采集，采集所得数据是 T1 的必要输入。资源到位时间见附录“资源条件”。\n\n'
for n in range(1, 17):
    main_text += f'## 实施记录 {n:02d}\n\n本段仅说明第 {n:02d} 组记录的整理方式。保留原始记录与条件编号之间的对应，核对计量单位、记录日期及观察备注。若记录不完整，先标识缺失原因，不把缺失自动记为阴性结果。\n\n同一整理方法用于问题 Q1 和 Q2，记录编号不代表独立的研究任务，也不承诺已经获得结果。上述安排都是拟开展工作，当前材料不含执行日志。\n\n'
main_text += '## 当前材料范围\n\n两份文本均已提供；无图片。设备许可附件未提供，需把作者的资源陈述与对许可原件的核验区分开。\n'

annex_text = '# 附录 v1\n\n本附录的条件适用于选定正文中所有任务。\n\n## 任务补充\n\nT1 同时比较预先列出的条件下关系的成立与失效，得到关系估计和适用边界；这分别回答 Q1 和 Q2。验证按同一条件表检查，不要求任务数量与问题数量相等。\n\n## 资源条件\n\n设备 E 是唯一可用采集设备；项目第6个月才可使用。在此之前无替代设备和可复用数据。作者称许可已经取得，但许可原件未提供。\n\n## 记录表\n\n| 记录编号 | 条件说明 | 备注 |\n| --- | --- | --- |\n'
for n in range(1, 19):
    annex_text += f'| R{n:02d} | 预先列出的第 {n:02d} 项条件，按正文组织记录 | 拟获取，当前不是已完成结果 |\n'
annex_text += '\n## 引用示例\n\n下面是需要作为字面文本保存的示例，不是附录标题：\n\n```text\n# 不是标题\nS01-C001 只是快照内的示例编号。\n\n示例中的空行不应当使代码围栏被切开。\n```\n\n## 结果范围\n\n仅分析预先列出的条件，不承诺任意条件下通用。当前审查仅覆盖已提供两份文本，不含许可原件的实际核验。\n'

MAIN.write_text(main_text, encoding='utf-8')
ANNEX.write_text(annex_text, encoding='utf-8')
(SNAP / '正文-v1.txt').write_text(main_text, encoding='utf-8')
(SNAP / '附录-v1.txt').write_text(annex_text, encoding='utf-8')


def call(label, *args, expected=0):
    p = subprocess.run([sys.executable, str(HELPER), *map(str, args)], capture_output=True, text=True, cwd=RUN)
    LOG.append({'label': label, 'args': list(map(str, args)), 'returncode': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr})
    assert p.returncode == expected, LOG[-1]
    return p.stdout


def read_all(index, version):
    data = json.loads(index.read_text(encoding='utf-8'))
    excerpts = []
    for source in data['sources']:
        covered = []
        for chunk in source['chunks']:
            covered.extend(range(chunk['start_line'], chunk['end_line'] + 1))
            excerpts.append(call(f'{version} {chunk["id"]}', 'read', index, chunk['id']))
        assert covered == list(range(1, source['line_count'] + 1)), source['id']
        actual = ''.join((RUN / 'sources' / Path(source['path']).name).read_text(encoding='utf-8').splitlines(keepends=True))
        assert source['characters'] == len(actual), source['id']
    (WORK / f'read-{version}.txt').write_text('\n'.join(excerpts), encoding='utf-8')
    return data


v1 = WORK / 'index-v1.json'
call('initial build', 'build', MAIN, ANNEX, '--output', v1, '--max-chars', 300)
call('initial verify', 'verify', v1)
old = read_all(v1, 'v1')
assert any(c['oversized'] for s in old['sources'] for c in s['chunks'])
assert not any(h['title'] == '不是标题' for s in old['sources'] for h in s['headings'])
table = next(c for c in old['sources'][1]['chunks'] if c['oversized'])
(WORK / 'oversized-window.txt').write_text('\n'.join(f'{n}: {annex_text.splitlines()[n-1]}' for n in range(table['start_line'], min(table['start_line'] + 6, table['end_line']) + 1)) + '\n', encoding='utf-8')

checkpoint = '''# 中断检查点 v1

选定来源：sources/正文.txt 与 sources/附录 条件.txt；索引 review-work/index-v1.json。
实际读取：两个来源全部 chunk，详见 read-v1.txt；索引覆盖连续性核对通过不等于语义结论。
M01（旧意见“Q2 无支撑任务”）：附录“任务补充”明确 T1 同时支撑 Q1、Q2，应撤销旧意见；稳定编号保留。
M02（仍存在）：正文“时间安排”承诺第3个月用唯一设备 E 采集；附录“资源条件”写第6个月才可使用，并排除替代设备和旧数据。完整两文件未发现其他解释。
M02 最小动作：将采集开始时间改到资源可用之后，并同步其依赖；或者如已有事实表明可更早使用，凭实际情况订正资源到位时间。不能凭空补提前到位事实。
未核验：许可原件、真实执行情况；本测试没有外部验证。
继续时：先验证索引；如源文件改动，重建索引、重新定位上述两端、重查受影响覆盖。不得沿用旧行号或 chunk ID。
'''
(WORK / 'checkpoint-v1.md').write_text(checkpoint, encoding='utf-8')

# Simulated user-selected v2 changes both files and shifts the line positions.
MAIN.write_text('# v2 修订说明\n\n本次根据作者新增资源安排修订附录，正文开始时间不变。\n\n' + main_text.replace('# 选定正文 v1', '# 选定正文 v2'), encoding='utf-8')
ANNEX.write_text('# v2 修订说明\n\n作者称设备已协调提前使用；该陈述没有随附新的许可原件。\n\n' + annex_text.replace('# 附录 v1', '# 附录 v2').replace('项目第6个月才可使用', '项目第2个月即可使用'), encoding='utf-8')
call('reject stale verify', 'verify', v1, expected=1)
call('reject stale read', 'read', v1, 'S01-C001', expected=1)
call('reject existing output', 'build', MAIN, ANNEX, '--output', v1, expected=1)

v2 = WORK / 'index-v2.json'
# Intentionally reverse argument order to demonstrate IDs are not identities.
call('rebuild revised sources', 'build', ANNEX, MAIN, '--output', v2, '--max-chars', 300)
call('revised verify', 'verify', v2)
new = read_all(v2, 'v2')
assert old['sources'][0]['path'] != new['sources'][0]['path']
assert all('Source changed' in item['stderr'] for item in LOG if item['label'].startswith('reject stale'))

(BASE / 'operations.json').write_text(json.dumps(LOG, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'source_count': 2, 'v1_chunks': sum(len(s['chunks']) for s in old['sources']), 'v2_chunks': sum(len(s['chunks']) for s in new['sources']), 'v1_lines': [s['line_count'] for s in old['sources']], 'v2_lines': [s['line_count'] for s in new['sources']], 'oversized_count_v1': sum(c['oversized'] for s in old['sources'] for c in s['chunks']), 'stale_verify_rejected': True, 'stale_read_rejected': True, 'artifact_root': str(BASE)}, ensure_ascii=False, indent=2))
