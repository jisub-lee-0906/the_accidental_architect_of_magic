# Current VN Production Baseline

Date: 2026-05-19
Project: The Accidental Architect of Magic

## 1. Source of truth

Project root:

```text
/home/jisub-lee/workspace/vn-demo/the_accidental_architect_of_magic
```

Windows UNC path:

```text
\\wsl.localhost\Ubuntu-24.04\home\jisub-lee\workspace\vn-demo\the_accidental_architect_of_magic
```

Kanban board:

```text
vn-accidental-magic
```

Always pass the board explicitly:

```bash
hermes kanban --board vn-accidental-magic ...
```

Reason: the shell may have `HERMES_KANBAN_BOARD=default`, so relying on the current board can route tasks to the wrong place.

ComfyUI workflow pack:

```text
/home/jisub-lee/workspace/comfyui-game-asset-workflows
```

ComfyUI output root:

```text
/mnt/c/Users/Desktop/Documents/ComfyUI/output
```

ComfyUI input root:

```text
/mnt/c/Users/Desktop/Documents/ComfyUI/input
```

Danbooru validator/cache:

```text
/home/jisub-lee/.hermes/cache/vn_comfyui/validate_danbooru_prompt.py
/home/jisub-lee/.hermes/cache/vn_comfyui/danbooru_lookup.sqlite
```

Canonical CSV:

```text
/home/jisub-lee/workspace/comfyui-game-asset-workflows/danbooru_tag.csv
```

The CSV is lookup-only and intentionally contains only:

```text
tag,aliases
```

## 2. Current production seed snapshot

Confirmed project characteristics:

```text
exists: yes
git repo: yes
Ren'Py game/script.rpy: yes
Ren'Py game/options.rpy: yes
```

Important current files:

```text
docs/01_master_lore.md
docs/02_character_db.md
docs/03_route_flowchart.md
docs/04_variable_tracker.md
docs/05_script_format.md
docs/06_asset_manifest.md
docs/scenes/prologue_001_public_demo_collapse.md
docs/scenes/prologue_001a_instinct_hidden.md
docs/scenes/prologue_002_corridor_escape.md
docs/scenes/prologue_003_lia_workshop_inquiry.md
game/script.rpy
game/generated_assets.rpy
```

Checkpoint commit:

```text
f115709 Checkpoint validated VN production foundation
```

This commit freezes the validated production foundation before the production-mode cleanup pass. Treat it as the safe return point for future iterations.

## 3. Current Ren'Py production prologue seed status

`game/script.rpy` currently contains a production prologue seed starting at:

```renpy
label start:
    call prologue_001_public_demo_collapse
    return
```

The current script already uses:

```renpy
scene cg_unstable_magic_structure_demo
scene cg_lia_first_serious_look
```

The first serious Lia CG is inserted after Do-yoon stabilizes the magic structure and before Lia says:

```text
……너.
```

Current insertion intent:

```text
After the structure stabilizes, show Lia losing her playful mask for the first time and focusing on the stabilized structure/Do-yoon's intervention.
```

This is the current first event-CG beat. Treat it as integrated for user review, not final production-ready, until owner-visible QA confirms it.

## 4. VN production roles

Use these profile roles:

```text
supervisor: user-facing control tower / approval gate
director: creative director / release reviewer
writer: scenario and canon/dialogue
coder: Ren'Py integration and lint/smoke checks
artist: ComfyUI candidate generation and prompt audit
qa: scenario QA + asset QA + playtester
default: fallback only; do not assign VN work here
```

Profile readiness smoke test on 2026-05-18 passed for:

```text
director, writer, coder, artist, qa
```

All five were spawned in parallel through `vn-accidental-magic` and completed canary tasks.

## 5. Event CG prompt discipline

The current event CG rule is:

```text
Keep the workflow/model README wrapper exactly.
Only the variable {Prompt} segment is agent-authored.
Inside {Prompt}, use only local danbooru_tag.csv tag/alias terms.
Do not add natural-language chunks or pseudo-tags inside {Prompt}.
If a variable token is rejected by the validator, remove or replace it before ComfyUI submission.
```

Mandatory README positive wrapper:

```text
masterpiece, best quality, amazing quality, 4k, very aesthetic, high resolution, ultra-detailed, absurdres, newest, scenery, {Prompt}, BREAK, depth of field, volumetric lighting
```

Mandatory README negative prompt:

```text
modern, recent, old, oldest, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured, long body, lowres, bad anatomy, bad hands, missing fingers, extra digits, fewer digits, cropped, very displeasing, (worst quality, bad quality:1.2), bad anatomy, sketch, jpeg artifacts, signature, watermark, username, signature, simple background, conjoined, bad ai-generated
```

Do not remove the README/model wrapper just because some wrapper terms are not in the CSV. The CSV restriction applies to the agent-authored `{Prompt}` portion only.

## 6. Current Lia event CG generation baseline

Recommended current baseline from user-liked candidate analysis:

```text
checkpoint: novaAnimeXL_ilV190.safetensors
resolution: 1024x576
sampler: euler_ancestral
scheduler: normal
steps: 30
cfg: 5.2
denoise: 1.0
```

Stable Lia inner prompt skeleton:

```text
1girl, solo, long_hair, wavy_hair, blunt_bangs, sidelocks, pink_hair, purple_eyes, serious, closed_mouth, looking_at_viewer, school_uniform, white_shirt, red_bow, gold_trim, capelet, blue_jacket, upper_body, cowboy_shot, straight-on, window, classroom, light_rays, facing_viewer, {ONE_POSE_TAG}
```

Recommended one-pose tags from user-liked candidates:

```text
arms_behind_back
crossed_arms
hand_on_own_chest
```

Selected-good prompt IDs:

```text
af370b71-fcbe-4392-a597-09d6f5bba4da  arms_behind_back  seed 2105181731
1b8dac52-c578-4f45-bdec-f4b620795188  crossed_arms      seed 2105181711
b46427ce-cec5-4e3e-a86b-b2f518bbabb8  hand_on_own_chest seed 2105181702
face50b3-847d-45bd-953e-52ecf1e9ac4c  straight/chest baseline seed 2105181601
```

Analysis artifact:

```text
/mnt/c/Users/Desktop/Documents/ComfyUI/output/hermes_readme_wrapper_event_cg_20260518_pose_variants/scene_event_cg/selected_prompt_analysis.json
```

## 7. Event CG composition policy

Use event CGs as memory-point illustrations, not generic replacement backgrounds.

Default neutral dialogue/reaction composition:

```text
upper_body, cowboy_shot, straight-on, facing_viewer
```

Use this for ordinary dialogue, emotional reaction, and choice lead-in beats.

Use `from_below` only when the story intentionally needs:

```text
dominance
awe
intimidation
reveal
authority
heroine visually towering over the camera/protagonist
```

Avoid `from_below` for ordinary dialogue/reaction CGs because it tends to make Lia look like she is looking down at the viewer.

Use at most one pose tag at a time unless a controlled test proves a compound pose stable.

Do-yoon / protagonist rule:

```text
Do not show Do-yoon's clear face in event CGs by default.
Use heroine focus, POV, offscreen protagonist, empty foreground, blurred hint, hand/shoulder only, or no protagonist.
```

## 8. Current promoted/candidate distinction

Promoted or integrated in current project state:

```text
bg_academy_demo_hall_afternoon
cg_unstable_magic_structure_demo
cg_lia_first_serious_look
lia_bel_astrin_* sprites/expression assets
```

Still candidate / experimental unless separately promoted:

```text
hermes_readme_wrapper_event_cg_20260518_straight/*
hermes_readme_wrapper_event_cg_20260518_pose_variants/*
hermes_readme_wrapper_event_cg_20260518_choice_batch/*
hermes_readme_wrapper_event_cg_20260518_slight_farther/*
```

Do not copy candidate images into `game/images/generated/` without explicit user approval and coder/QA gate.

## 9. Safe Kanban operating pattern from here

Do not create large new work batches until the current playable slice is verified.

Recommended next graph:

```text
T1 director:
  Map the 4 user-liked Lia CG candidates to scene purposes and recommend whether any should replace/supplement current cg_lia_first_serious_look.

T2 coder:
  Inspect actual Ren'Py project state, generated asset definitions, and lint availability. Do not modify files.

T3 qa:
  Review current integrated CG and the 4 user-liked candidates for identity, composition, protagonist exposure, dialogue-box safety, and story fit. Do not modify files.

T4 director fan-in:
  Synthesize T1/T2/T3 and recommend a single next approved action.
```

After user approval only:

```text
coder integrates one approved change -> qa lint/playtest -> director release review -> supervisor asks for commit approval
```

## 10. Immediate next goal

The next production goal is not “generate more CGs.”

The next goal is:

```text
Verify the current playable prologue slice with the integrated Lia event CG, then decide whether to keep it, replace it with one of the 4 user-liked newer candidates, or use the newer candidates later in a different scene.
```

Only after this playable slice is checked should the team expand more scenes or produce additional event CG batches.
