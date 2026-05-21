# VN Profile Orchestration Contract

Date: 2026-05-19
Project: The Accidental Architect of Magic
Board: `vn-accidental-magic`

This document defines how the Hermes VN profiles work together. It is the automation contract for task routing, cross-profile references, review gates, and artifact handoff.

## 1. Available profiles

Use these profiles for VN production:

| Profile | Role | Primary authority | Can edit files? | Final say? |
|---|---|---|---|---|
| `supervisor` | user-facing executive producer / control tower | scope, task graph, user approval, final report | only orchestration/docs unless needed | no; user approval gate |
| `director` | creative director / release reviewer | marketability, pacing, character appeal, KEEP/CUT/REWORK | review docs only unless tasked | creative recommendation |
| `writer` | scenario/canon/dialogue writer | Korean VN prose, choices, route/canon continuity | drafts/docs only unless tasked | no; reviewed by director/QA |
| `coder` | Ren'Py integrator | script implementation, image definitions, lint | yes, after approval/task scope | no; QA verifies |
| `artist` | ComfyUI asset candidate generator | prompt audit, seeds, candidate images/contact sheets | output candidates only | no; cannot promote alone |
| `asset_contract` | asset contract / registry specialist | Ren'Py-safe asset IDs, path/status map, creative-to-build contract | `.analysis/asset_contracts/*` only unless tasked | no; coder/QA consume contract |
| `qa` | scenario/asset/playtest QA | blockers, evidence, lint/playthrough/readability, failure classification | QA reports only unless tasked | can block release |
| `default` | fallback Hermes profile | none for VN | no VN production work | never assign VN tasks |

## 2. Single source of truth

Every VN task must include the project root and read relevant source files. Do not rely on memory alone.

Project root:
`/home/jisub-lee/workspace/renpy-project/the_accidental_architect_of_magic`

Core current-state docs:

- `CURRENT_VN_PRODUCTION_BASELINE.md`
- `DOPAMINE_FIRST_PIVOT_AUDIT.md`
- `VN_PROFILE_ORCHESTRATION_CONTRACT.md`
- `docs/01_master_lore.md`
- `docs/02_character_db.md`
- `docs/03_route_flowchart.md`
- `docs/04_variable_tracker.md`
- `docs/05_script_format.md`
- `docs/06_asset_manifest.md`
- `docs/scenes/*.md`
- `game/script.rpy`
- `game/generated_assets.rpy`

Rule: if a worker needs context from another worker, it should receive either:

1. a parent Kanban task id, and/or
2. exact artifact paths from the parent, and/or
3. a concise quoted summary embedded in the child task body.

Do not say “check previous work” without task id/path.

## 3. Core operating model

### Studio mode / company assumption

Operate the project as a small game studio, not as one assistant writing documents.

- `supervisor` is the executive producer / PM: defines the sprint goal, opens work orders, checks evidence, and brings only high-impact decisions to the user.
- `director` is creative leadership: owns player appeal, pacing, scene purpose, and release recommendations.
- `writer`, `asset_contract`, `artist`, and `coder` are production departments: they produce scoped deliverables, not open-ended commentary.
- `qa` is both the loop classifier and release gate: it can block, route failures to the correct owner, request retest, or approve with warnings based on evidence.
- The user is the publisher / owner: reviews milestone-level choices, not every small implementation detail.

Default behavior in studio mode:

1. Do not create broad documentation for its own sake.
2. Convert docs into work orders, acceptance criteria, QA gates, and playable output.
3. Keep parallel work small enough to verify: one playable slice, one asset beat, or one retention fix at a time.
4. Supervisor should fan-in worker outputs and report decisions, evidence, and next approval point.
5. A task is valuable only if it moves the game toward a better playable build, better asset candidate, or clearer release decision.

The system is not a free-for-all swarm. It is a gated cyclic production line:

```text
default intake
  ↓
supervisor triage / task graph
  ↓
director + writer creative intent
  ↘
   asset_contract asset map/schema  ← reads creative needs
  ↓
contract QA join
  ↓
coder compiler/integrator
  ↓
qa lint/runtime/visual classifier
  ↓
failure-type loopback to coder / writer-director / asset_contract / artist
  ↓
supervisor fan-in → user approval only at meaningful gates
```

Important:

- `supervisor` does not write all content personally; it routes, verifies, and summarizes.
- `writer` does not implement directly into `game/script.rpy` unless the task explicitly allows it.
- `artist` does not promote files into Ren'Py by itself.
- `coder` does not invent story/art direction; it implements approved scope.
- `qa` does not make creative taste calls alone; it provides blockers/evidence.
- `director` can recommend but cannot bypass QA or user approval.

## 4. Canonical task graph patterns

### Pattern 0 — Creative→Asset Contract→Compiler cyclic build

Use this as the default automation graph when a user asks for a scene/script/build change that combines dialogue, assets, and Ren'Py implementation. It replaces the old one-way “write then code then QA catches everything” flow.

```text
T0 supervisor/director: scene purpose and acceptance criteria
  output: hook goal, emotional beat, forbidden changes, required evidence

T1 writer: Creative Agent draft
  parent: T0 when scene purpose is unclear
  output: dialogue/narration, emotional beats, choice intent, natural-language asset needs
  forbidden: final file names, asset IDs, Ren'Py code, ComfyUI prompts

T2 asset_contract: Asset Contract Agent map
  parent: T1, or parallel with T1 if director already supplied exact needs
  output: .analysis/asset_contracts/<scene>_<pass>.yaml
  required fields: asset_id, renpy_id, path, status, usage, source_requirement, owner, qa_notes

T3 qa or director: Contract QA join
  parents: T1 + T2
  output: PASS / ASSET_CONTRACT_MISMATCH / CREATIVE_MISMATCH / NEEDS_FROM_*

T4 coder: Compiler Agent `.rpy` build
  parent: T3 PASS or explicit supervisor approval
  output: changed Ren'Py files, generated asset definitions, lint/static result
  forbidden: story invention, asset ID/path invention outside T2

T5 qa: Lint/Runtime/Visual classifier
  parent: T4 if done; if coder blocks review-required, create independent QA card referencing T4
  output: PASS/BLOCKER/WARNING/EVIDENCE plus failure class

Loopback:
- SYNTAX_REFERENCE → T4 coder
- CREATIVE_MISMATCH → T1 writer or T0 director
- ASSET_CONTRACT_MISMATCH → T2 asset_contract
- VISUAL_DIALOGUE_MISMATCH → T0 director decides writer patch vs asset remap vs artist regen vs coder staging
- ASSET_GENERATION_NEEDED → artist candidate task, then asset_contract update, then QA retest
```

Failure classes are mandatory in QA reports: `SYNTAX_REFERENCE`, `CREATIVE_MISMATCH`, `ASSET_CONTRACT_MISMATCH`, `VISUAL_DIALOGUE_MISMATCH`, `ASSET_GENERATION_NEEDED`, `RUNTIME_BLOCKER`, `WARNING_ONLY`.

Do not route every QA failure to `coder`: only syntax/reference faults belong there; creative faults return to writer/director, asset contract faults return to `asset_contract`, and visual-dialogue faults return to director arbitration.

### Pattern A — Story hook / scene rewrite

Use when changing dialogue, pacing, choices, or scene structure.

```text
T1 writer: draft scene pass
  output: .analysis/drafts/<scene>_<pass>.md

T2 director: creative/market review of T1
  parent: T1
  output: .analysis/reviews/<scene>_director_review.md

T3 qa: retention/canon/variable QA of T1
  parent: T1
  output: .analysis/reviews/<scene>_qa_review.md

T4 supervisor: fan-in decision
  parents: T2 + T3
  output: KEEP / REWORK / CUT / SEND_TO_CODER

T5 coder: implement approved pass
  parent: T4 or explicit supervisor approval
  output: changed Ren'Py files + lint result

T6 qa: implementation QA
  parent: T5 if T5 is done; if coder blocks review-required, create independent QA card referencing T5
  output: PASS/BLOCKER/WARNING/EVIDENCE

T7 director: release review
  parent: T6
  output: GO / PATCH / REVERT recommendation

T8 supervisor: report to user and ask approval for commit/promotion
```

### Pattern B — Asset generation / event CG

Use when creating or selecting images.

```text
T1 director: scene/asset brief
  output: purpose, emotion, camera, must-have/must-not-have, where used in script

T2 artist: generate candidates
  parent: T1
  output: prompt audit, prompt_id, seed, exact paths, contact sheet if possible

T3 qa: asset QA
  parent: T2
  output: identity, composition, safe area, Do-yoon face rule, file evidence

T4 director: select/reject/regenerate recommendation
  parent: T3
  output: KEEP / LATER / REJECT / REGEN brief

T5 supervisor: ask user to approve exact candidate

T6 coder: integrate approved asset only
  parent: explicit user approval
  output: copied file path, generated_assets.rpy diff, script placement, lint

T7 qa: playable/screenshot QA
  parent: T6
```

Rules:

- Candidate asset is not final.
- `artist` must not use non-CSV Danbooru-style prompt tokens inside `{Prompt}`.
- Do-yoon face hidden in event CGs unless explicitly approved otherwise.
- Complex magic/geometry should often be Ren'Py overlay/prop rather than prompt bloat.
- Scene-critical location continuity is a separate gate from character appeal. Do not use a visually different place as a prompt proxy just because its tag exists. For the prologue `magic_demo_hall_03` / 제3마법시연장 beat, `classroom`, `chalkboard`, and `blackboard` are forbidden proxies unless the user explicitly changes canon.
- If the exact canon place has no single CSV tag, first search `danbooru_tag.csv` for adjacent valid staging tokens such as `auditorium`, `stage`, `podium`, `spotlight`, `curtains`, `presentation`, `projector`, `indoors`, `window`, and `sunlight`; if that still fails, solve the location cue through background assets, Ren'Py staging, overlays, or a separate prop/cut-in instead of inventing pseudo-tags.

### Pattern C — Post-assembly asset/dialogue alignment loop

Use after `coder` has assembled a scene with real or candidate assets. This is mandatory whenever a dialogue beat is tied to a CG/sprite/background/prop.

```text
T1 coder: assemble current approved/candidate asset into Ren'Py
  output: changed files, exact image IDs/paths, lint/static result, screenshot paths if feasible

T2 qa: asset-dialogue alignment QA
  parent: T1 if T1 is done; if coder blocks review-required, create an independent QA card referencing T1
  output: PASS / MISMATCH / NEEDS_BETTER_IMAGE / TEXT_PATCH_ONLY / EVIDENCE

T3 director: alignment decision
  parent: T2
  output: KEEP / REQUEST_ARTIST_REGEN / REQUEST_WRITER_TEXT_PATCH / REQUEST_CODER_SWAP / SPLIT_WITH_OVERLAY

T4 artist: regenerate or produce better candidate only when T3 requests image change
  parent: T3
  output: prompt audit, prompt_id, seed, exact paths, contact sheet, why this better matches the line/beat

T5 qa: regenerated asset QA
  parent: T4
  output: identity/composition/Do-yoon-face/readability/alignment verdict

T6 coder: swap to selected asset or add overlay/prop only after director/supervisor approval
  parent: T5 or explicit approval
  output: changed image definition/script placement, lint, screenshots

T7 qa: final playable alignment retest
  parent: T6
```

Alignment QA must check:

- Does the visible pose/gaze/expression match the line currently on screen?
- Does the asset explain the scene beat better than the previous candidate?
- Does the visible location/staging match the canon scene location, not merely the emotion? For prologue demo-hall beats, reject classroom/chalkboard/blackboard reads even if Lia's face/expression is strong.
- Report emotion/identity score and location-continuity score separately so a pretty candidate cannot hide a wrong-place blocker.
- If not, is the cheapest fix text staging, camera/overlay/prop, or a new image?
- Is Do-yoon's face still hidden in event CGs?
- Are magic/geometry beats better handled as Ren'Py overlay/cut-in instead of prompt bloat?

Rules:

- `coder` integrates/switches assets; `artist` only creates candidates.
- `qa` may request artist regeneration when visual/text mismatch is real.
- `director` decides whether mismatch is a creative blocker or acceptable warning.
- `supervisor` should not bring every mismatch to the user; only show the user milestone-level choices or cases where visual direction changes.

### Pattern D — Playable slice release gate

Use before saying a slice is ready.

```text
T1 coder: static/lint check
T2 qa: playthrough/click-through checklist
T3 director: release feel review
T4 supervisor: user-facing release report
T5 user approval: commit or patch
```

Required evidence:

- Ren'Py lint command + exit code.
- All visible choices checked.
- No placeholder path exposed.
- Asset files exist and are defined.
- Screenshot/readability warning status.

### Pattern E — Dopamine-first pivot loop

Use when the user questions whether the game is compelling enough.

```text
T1 director: market/hook audit
T2 writer: first-5-minute pacing audit or draft
T3 qa: retention blocker audit
T4 supervisor: KEEP/CUT/REWORK synthesis
T5 coder or writer: implement next smallest hook change
T6 qa: verify retention gates
```

Retention gates:

- 0:00 strong visual.
- First mystery within 3 player-facing lines.
- First micro-interaction within 60-90 seconds.
- First relationship shift within 3-4 minutes.
- First real choice within 5 minutes.
- No public placeholder branch.

## 5. Cross-profile reference rules

### What every task body must include

Every Kanban card must include:

```text
Project root: /home/jisub-lee/workspace/renpy-project/the_accidental_architect_of_magic
Board: vn-accidental-magic
Role goal: <what this profile should do>
Allowed edits: <exact files or inspect-only>
Read first: <exact files/artifacts>
Output: <exact path or required summary format>
Acceptance criteria: <PASS/BLOCKER or KEEP/REWORK etc.>
Forbidden: <what not to change/claim>
```

### Parent/child dependencies

Use parent links only when the child cannot start without the parent's output.

Good:

```text
writer draft -> director review
artist candidates -> asset QA
coder implementation -> QA verification
```

Do not over-link independent audits:

```text
director market audit + qa retention audit can run in parallel.
```

### Review-required exception

Sometimes `coder` blocks with `review-required` after making changes and linting. Parent-linked QA will not auto-run because parent is blocked, not done.

Policy:

1. `supervisor` reads coder blocked handoff.
2. If handoff contains actual file changes and lint evidence, create a new independent QA card that references the coder task id.
3. QA verifies the diff and writes a report.
4. Supervisor decides whether to complete/unblock/create patch task.

This happened in the dopamine prologue hook implementation and should be treated as normal, not failure.

## 6. Artifact naming conventions

Use `.analysis/` for non-canon working artifacts:

```text
.analysis/plans/<topic>_implementation_order.md
.analysis/asset_contracts/<scene>_<pass>.yaml
.analysis/drafts/<scene>_<pass>.md
.analysis/reviews/<scene>_<role>_review.md
.analysis/reviews/<scene>_implementation_qa.md
.analysis/contact_sheets/<asset_batch>.png
```

Use project-root docs only for durable, user-approved operating contracts:

```text
CURRENT_VN_PRODUCTION_BASELINE.md
DOPAMINE_FIRST_PIVOT_AUDIT.md
VN_PROFILE_ORCHESTRATION_CONTRACT.md
```

Use `docs/` for canon/design docs only when the task explicitly asks to update canon.

## 7. Profile-specific contracts

### supervisor

Owns:

- user conversation
- profile discovery
- board dispatch/polling
- task graph design
- fan-in summaries
- approval gates
- memory/skill/profile updates when durable

Must not:

- bury the user in long worker logs
- ask approval for every tiny internal step
- claim QA/final status without evidence

Typical output:

```text
작업 그래프:
T1 writer ...
T2 director ...
T3 qa ...
현재 gate: user approval / QA / lint
다음 권장 액션: ...
```

### director

Owns:

- story/asset purpose
- marketability and dopamine-first hook strength
- character appeal
- release review
- KEEP/CUT/REWORK decisions

Must read:

- baseline/audit/orchestration contract
- relevant scene draft/script section
- QA report before release recommendation

Output format:

```text
VERDICT
KEEP
REWORK
CUT
BLOCKERS
GO-NO-GO FOR CODER/ARTIST/RELEASE
```

### writer

Owns:

- Korean dialogue and narration
- scene beats
- choice wording
- variable intent at draft level
- canon-preserving adaptation

Must produce self-check:

```text
First 3 lines hook: PASS/WARN/BLOCKER
Micro-interaction timing: PASS/WARN/BLOCKER
First real choice timing: PASS/WARN/BLOCKER
Variables: PASS/WARN/BLOCKER
Placeholder exposure: PASS/WARN/BLOCKER
Lia appeal: PASS/WARN/BLOCKER
Canon preservation: PASS/WARN/BLOCKER
```

Default output path:

```text
.analysis/drafts/<scene>_<pass>.md
```

### asset_contract

Owns:

- asset contract / registry between creative draft and compiler
- `asset_id` / `renpy_id` naming
- exact path/status mapping for existing, candidate, missing, or placeholder assets
- detection of duplicate IDs, unused IDs, unmapped creative needs, and namespace conflicts

Must read:

```text
upstream writer/director artifact
game/generated_assets.rpy
docs/06_asset_manifest.md
relevant game/script.rpy section if asset usage already exists
```

Required result:

```text
ASSET_CONTRACT
CONTRACT_QA
UNMAPPED_CREATIVE_NEEDS
UNUSED_ASSET_IDS
DUPLICATES_OR_CONFLICTS
NEEDS_FROM_writer/director/artist/coder/qa
```

Default output path:

```text
.analysis/asset_contracts/<scene>_<pass>.yaml
```

### coder

Owns:

- `game/script.rpy`
- `game/generated_assets.rpy`
- Ren'Py integration
- lint/static checks

Preflight:

```text
git status --short
read plan/draft/reviews
confirm allowed edits
```

Required result:

```text
FILES CHANGED
KEY DIFF
STATIC CHECKS
LINT COMMAND + EXIT CODE
RISKS
```

### artist

Owns:

- ComfyUI candidate generation
- prompt validation
- output paths/seeds/prompt_id/contact sheets

Must not:

- promote candidates directly into final Ren'Py paths without approval
- use invalid Danbooru-style tokens inside `{Prompt}`
- call output final before QA

Required result:

```text
WORKFLOW
PROMPT AUDIT
PROMPT_ID
SEED
OUTPUT PATHS
CONTACT SHEET
QA RISKS
```

### qa

Owns:

- scenario QA
- asset QA
- implementation QA
- lint/playthrough evidence
- blocker detection

Output format:

```text
PASS
BLOCKER
WARNING
EVIDENCE
RETEST
```

QA can block release even when director likes the result.

## 8. Automation command pattern

Always use explicit board flag:

```bash
BOARD=vn-accidental-magic
PROJECT=/home/jisub-lee/workspace/renpy-project/the_accidental_architect_of_magic

hermes kanban --board "$BOARD" create "writer: ..." \
  --assignee writer \
  --workspace "dir:$PROJECT" \
  --body "Project root: $PROJECT ..." \
  --json

hermes kanban --board "$BOARD" dispatch --max 3 --json
hermes kanban --board "$BOARD" list --json
hermes kanban --board "$BOARD" show <task_id>
```

Never assign VN tasks to `default`. Use `asset_contract` for the asset-schema/registry lane; do not make `coder` guess missing asset IDs.

## 9. Decision gates

### Internal gates supervisor may pass without asking user

- create draft/review/QA tasks
- run lint/static checks
- create `.analysis/` plans/reviews
- ask workers to inspect files
- generate non-promoted candidate assets if user already approved the lane

### User approval required

- destructive rewrites
- canon changes in `docs/`
- promoting/copying asset candidates into game paths
- committing changes
- deleting/renaming large files
- changing main visual direction or protagonist face rule
- declaring a slice public-ready/final

## 10. Current recommended next graph after dopamine hook implementation

Current state:

- `game/script.rpy` has dopamine-first prologue hook implemented.
- Ren'Py lint passed.
- QA says PASS WITH WARNINGS.
- Remaining warning: GUI click-through and screenshot/readability QA not done.

Next graph:

```text
T1 qa: GUI/click-through QA of prologue path
  check: all micro-menu choices, all real-choice branches, no placeholder text

T2 director: release-feel review
  parent: T1
  check: first 5 min dopamine, Lia appeal, whether to patch or keep

T3 supervisor: user playtest handoff
  parent: T2
  output: exact run command, known warnings, commit recommendation
```

Do not expand to new routes/assets until this gate is cleared.
