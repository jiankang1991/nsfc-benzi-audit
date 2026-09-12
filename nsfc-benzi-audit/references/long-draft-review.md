# Long Drafts And Interrupted Reviews

Use when the selected material spans many sections/files or a review resumes after interruption. Keep the core [finding decisions](benzi-logic.md) unchanged. The purpose is to retain distant evidence and unfinished work, not to require a report for each chunk.

## Source Map

Identify the selected version, readable source files and original figures/attachments. Map where claims, models, tasks, validation, prior work and resource conditions actually occur, including appendices. A heading or search hit locates evidence; it does not replace reading its surrounding argument. Preserve a compact record of unresolved candidates and their source locations as you read.

For UTF-8 Markdown/text, the optional [review_index.py](../scripts/review_index.py) creates a source hash, heading map and non-overlapping line chunks. Python 3 is sufficient; no third-party dependency is required. It neither extracts PDF/DOCX nor reads original figures. Without Python, maintain equivalent source/section notes using available tools; the helper is not a prerequisite for diagnosis.

```bash
python3 <skill-dir>/scripts/review_index.py build draft.md appendix.md --output review-work/index-v1.json
python3 <skill-dir>/scripts/review_index.py read review-work/index-v1.json S01-C001
python3 <skill-dir>/scripts/review_index.py verify review-work/index-v1.json
```

The output directory is for local working artifacts. Input paths in the index are relative to its location. Chunk IDs belong to that snapshot, not to the application across revisions. The source hash identifies bytes, not the authoritative version; the user's selected original still determines which extraction is relevant. A large uninterrupted paragraph, table or code fence can exceed the target chunk size and is marked `oversized`; read it in suitable line windows rather than silently skipping it.

## Reading And Counterevidence

For a complete review, read every requested source range, including relevant annexes. Read in dependency order when useful; do not diagnose each chunk in isolation. Carry forward only facts needed for cross-section checks, candidate findings and unresolved evidence locations. Search for terms, aliases or equation identifiers to return to a passage after its role is known.

For each consequential candidate, find both the claimed result and its actual support or counterevidence. A later restriction can resolve an earlier concern; it can also expose two incompatible specifications. Check which scope and version the restriction governs before closing the finding. Keep a root issue intact across chapters and do not turn the same mismatch into several numbered defects.

## Resume Without Overclaiming

Before interruption or handoff, keep a short working checkpoint beside the report only when needed:

- The selected source versions or index location.
- Ranges actually read and ranges still unread. A generated index, successful `verify`, or retrieved chunk alone does not establish semantic review.
- Open finding IDs with claim/support locations, the strongest counterevidence found, and the next unresolved check.
- Closed or withdrawn earlier opinions and the source supporting their status.

When resuming, verify the selected sources. If any source changed, regenerate the index and revisit affected evidence and coverage; do not transfer old chunk IDs or treat old line locations as current. The helper checks source bytes before retrieval and stops on a mismatch. It cannot verify a human/agent's reading record or the truth of its notes.

## Make The Output Actionable

Honor the requested report length independently of reading depth. Give the main report a short conclusion and one action per distinct issue, with a precise source locator and the smallest repair. If several valid repair branches exist, state their consequences without selecting a new research objective for the applicant.

Keep detailed claim/support passages and coverage in a separate appendix when the main report would otherwise become unwieldy. Cross-reference existing issue IDs; the appendix should supply additional evidence, not repeat the entire recommendation. If the user requested a compact report, positive coverage can be summarized rather than listing a long defense of every acceptable arrangement.

Close with actual unexamined material and unresolved checks. Partial access limits the completeness claim; it does not turn unread chapters or unavailable attachments into applicant defects.
