# Dopamine-First Pivot Audit

Date: 2026-05-18
Project: The Accidental Architect of Magic

## Verdict

Do not throw away the project.

Do not expand the pre-cleanup foundation as-is without applying the production seed direction.

The correct move is:

```text
KEEP the core concept and current asset/canon foundation.
REWORK the first 5 minutes aggressively for short-attention retention.
CUT or defer slow exposition and incomplete branches from the public playable path.
ADD a small interactive structure-line hook before or near the first choice.
```

This is a restructure/pivot, not a total rewrite.

## Evidence inspected

Project root:

```text
/home/jisub-lee/workspace/vn-demo/the_accidental_architect_of_magic
```

Measured files:

```text
CURRENT_VN_PRODUCTION_BASELINE.md                 325 lines
docs/01_master_lore.md                            110 lines
docs/02_character_db.md                           105 lines
docs/03_route_flowchart.md                         59 lines
docs/04_variable_tracker.md                        90 lines
docs/05_script_format.md                          135 lines
docs/06_asset_manifest.md                         355 lines
docs/scenes/prologue_001_public_demo_collapse.md  413 lines
docs/scenes/prologue_001a_instinct_hidden.md      346 lines
docs/scenes/prologue_002_corridor_escape.md       481 lines
docs/scenes/prologue_003_lia_workshop_inquiry.md  518 lines
game/script.rpy                                   542 lines
game/generated_assets.rpy                          24 lines
```

Current Ren'Py script structure:

```text
labels: 7
menus: 1
dialogue-like lines: 353
scene commands: 11
show commands: 49
```

Current generated game assets:

```text
game/images/generated: 13 files
game/images/generated/event_cg: 2 files
game/images/generated/backgrounds: 3 files
game/images/generated/sprites: 7 files
```

Current git status at audit time:

```text
 M docs/06_asset_manifest.md
 M docs/scenes/prologue_001_public_demo_collapse.md
 M game/generated_assets.rpy
 M game/script.rpy
?? CURRENT_VN_PRODUCTION_BASELINE.md
?? DOPAMINE_FIRST_PIVOT_AUDIT.md
?? game/images/generated/event_cg/cg_lia_first_serious_look.png
```

Kanban dopamine-first audit tasks:

```text
t_78ca6e62 director: dopamine-first product direction audit
t_85deafcf writer: dopamine-first script pacing audit
t_1c11e56f qa: dopamine-first player retention risk audit
```

Worker consensus:

```text
Full rewrite: no.
First 5-minute restructure: yes.
Core hook: keep.
Exposition/branch pacing: rework.
Current B/C placeholder branches: retention blocker.
```

## What currently has commercial hook

Keep these.

### 1. Core fantasy hook

```text
A real-world structural-design assistant is thrown into a magic academy and can see structural flaws in magic architecture.
```

This is stronger than a generic isekai magic genius premise because the protagonist's real-world competence maps into a fantasy system.

Short pitch:

```text
마법을 모르는 구조설계 보조원이, 천재 마법사의 붕괴 직전 술식을 구조 계산처럼 고쳐버렸다.
```

### 2. Lia's first reaction

Keep the relationship hook:

```text
Lia is playful/confident.
Do-yoon fixes what she could not fix.
Lia loses her smile for the first time.
```

This is the current best heroine hook.

### 3. First choice axis

Keep the first-choice structure:

```text
A. Hide/minimize: "저도 모르겠는데요. 무너질 것 같아서요."
B. Expose exactly: "그 선이 받치는 게 아니라 비틀고 있었어요."
C. Responsibility/anxiety: "제가 뭘 잘못 건드렸나요?"
```

These map cleanly to:

```text
mc_concealment
mc_exposure
mc_responsibility
```

### 4. Existing visual foundation

Keep current promoted/integrated assets as foundation:

```text
bg_academy_demo_hall_afternoon
cg_unstable_magic_structure_demo
cg_lia_first_serious_look
lia_bel_astrin_* sprites
```

Do not discard the working asset base. Re-stage it.

## What is currently too slow for dopamine-first retention

### 1. First choice arrives too late

QA flagged:

```text
First choice appears after about 92 dialogue blocks.
```

For short-attention players, this is too late unless the opening is extremely visually dynamic.

Target:

```text
First micro-interaction within 60-90 seconds.
First real choice within 3-5 minutes.
```

### 2. The opening explains before it hooks

Current opening does:

```text
location setup -> world context -> protagonist confusion -> structure description -> Lia introduction -> instability
```

Dopamine-first production direction should do:

```text
collapse hook -> wrong line -> Lia pressure -> protagonist acts -> reaction -> explanation later
```

### 3. Later scene expansion is premature

Current script already includes:

```text
prologue_001a_instinct_hidden
prologue_002_corridor_escape
prologue_003_lia_workshop_inquiry
```

These can stay as canon/source, but they should not be the next focus until the opening retention loop works.

### 4. B/C first-choice branches are placeholders

QA flagged this as a retention blocker:

```text
B/C choices currently route to placeholder labels and end quickly.
```

For a dopamine-first playable, either:

```text
- make all three first choices give an immediate satisfying response, or
- temporarily ship only one locked path and hide unfinished branches.
```

Do not expose dead-end placeholder choices in a public-feeling playable.

## New target structure: First 5 Minutes Hook Pass

Goal:

```text
Player understands the game's unique taste within 5 minutes.
```

Target experience:

```text
0:00   Impact image / unstable magic structure.
0:10   "무너진다." Do-yoon notices one wrong line.
0:30   Lia appears confident, playful, dangerous.
0:60   First micro-interaction: player chooses what Do-yoon focuses on.
1:30   Wrong line becomes visually obvious through prop/overlay/cut-in.
2:00   Collapse accelerates; Lia's confidence cracks.
3:00   Do-yoon intervenes.
3:30   Structure stabilizes.
4:00   cg_lia_first_serious_look.
4:30   Lia: "……너."
5:00   First real choice: hide / expose / responsibility.
```

## Recommended cold open sample

Candidate opening direction, not canon yet:

```text
scene cg_unstable_magic_structure_demo
with dissolve

"무너진다."

도윤은 마법을 몰랐다.

주문도, 마력도, 눈앞의 빛나는 구조물이 왜 허공에 떠 있는지도 몰랐다.

그런데 선 하나만은 보였다.

받치는 척하면서, 전체를 비틀고 있는 선.

mc "……저 선이 저기 있으면 안 되는데."
```

Then introduce Lia immediately:

```text
lia_playful "자, 박수는 나중에. 일단 안 무너지는지부터 보자고."
```

This preserves the current line but moves the player into crisis first.

## Add one small gameplay hook

The project should not become a pure passive reader if the target is dopamine-first.

Add a micro-interaction around the structure-line concept.

Example:

```renpy
menu:
    "도윤이 먼저 본 것은?"
    "중심부에서 비틀리는 선":
        $ mc_exposure += 1
        "맞다. 저 선이다."
    "빛이 가장 밝은 장식선":
        $ mc_concealment += 1
        "아니다. 저건 눈속임에 가깝다."
    "아래쪽을 받치는 지지선":
        $ mc_responsibility += 1
        "위험하긴 하지만, 원인은 아니다."
```

This gives the player the feeling:

```text
I saw the flaw.
I participated in the premise.
```

This is more important for this project than adding another heroine CG immediately.

## Visual rhythm policy

For dopamine-first pacing, target:

```text
Visible change every 10-20 dialogue blocks.
A hook or tension beat every 30-60 seconds.
A CG/prop/overlay moment every major emotional or incident beat.
```

The first 5 minutes should use only a few strong visuals:

```text
1. cg_unstable_magic_structure_demo
2. structure-line prop/overlay cut-in, if created
3. cg_lia_first_serious_look
4. Lia sprite expression changes
```

Do not generate many unrelated event CGs before testing this rhythm.

## Keep / Cut / Rework map

### KEEP

```text
Core concept: magic architecture read through structural-design intuition.
Lia/Do-yoon first conflict.
First choice axis: concealment/exposure/responsibility.
Current generated backgrounds and Lia sprites.
Current integrated cg_lia_first_serious_look as a reaction beat.
Current docs as source material/canon bank.
```

### CUT from the first playable path, not necessarily from canon

```text
Long early explanation of academy/faculty/location.
Repeated descriptions before the first crisis lands.
Any branch that ends as obvious placeholder.
Any scene after the first choice until the opening loop is retuned.
```

### REWORK

```text
prologue_001_public_demo_collapse should become a cold-open crisis scene.
game/script.rpy opening should be edited for 30-second hook and 5-minute first choice.
docs/scenes/prologue_001_public_demo_collapse.md should keep full canon but add a dopamine-first playable adaptation section.
B/C branches should either receive short satisfying responses or be hidden for the next public slice.
Asset manifest should add a structure-line prop/overlay as required_visual or high-priority polish.
```

### ADD

```text
A micro-interaction: choose/notice the wrong structure line.
A prop/overlay visual for the wrong line.
A measurable retention QA gate.
```

## Measurable next QA gate

Before expanding story, verify this:

```text
- First striking visual appears at 0:00.
- First mystery/question appears within 3 dialogue lines.
- First player interaction appears within 60-90 seconds.
- First real character relationship shift appears within 3-4 minutes.
- First major choice appears within 5 minutes.
- No exposed placeholder branch in the playable path.
- Ren'Py lint passes.
```

## Recommended next Kanban graph

Do not assign broad rewrite yet.

Use this gated graph:

```text
T1 writer:
  Draft dopamine-first prologue_001 adaptation only.
  Scope: first 5 minutes, cold open, first micro-interaction, first real choice.
  Do not edit files unless separately approved.

T2 director:
  Review T1 for hook strength, Lia character preservation, and VN market fit.

T3 coder:
  After user approval, implement the adaptation in game/script.rpy only.
  Keep original docs/canon intact.

T4 artist:
  Only if T1/T2 confirm need, generate structure-line prop/overlay candidate.

T5 qa:
  Lint + timed playthrough + retention gate checklist.
```

## Final call

The project should be transformed, but not nuked.

The correct pivot is:

```text
From: documentation-heavy linear VN intro
To: crisis-first interactive hook VN intro
```

The current work becomes source material and asset foundation. The public playable path should be aggressively shortened, visually punctuated, and given one small interactive structure-reading mechanic.
