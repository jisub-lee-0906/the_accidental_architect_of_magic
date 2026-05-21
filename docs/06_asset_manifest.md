# 06 Asset Manifest

## Status Legend

- needed: 필요하지만 아직 생성되지 않음
- generated: 생성은 되었으나 QA 전
- qa_pending: QA 필요
- promoted: Ren'Py game directory에 사용 확정 반영됨

## Character Metadata Contract

기존 캐릭터 기반 에셋을 새로 생성할 때는 이 manifest의 자연어 설명이나 과거 ComfyUI PNG metadata를 직접 복붙하지 않는다. 먼저 캐릭터별 machine-readable sidecar를 읽고, workflow별로 필요한 subset만 prompt로 조립한다.

- Lia sidecar: `docs/assets/characters/lia_bel_astrin.asset.json`
- sidecar guide: `docs/assets/characters/README.md`
- reusable prompt builder: `/home/jisub-lee/workspace/comfyui-game-asset-workflows/scripts/build_character_prompt.py`

2026-05-21 foundation-lock rule: Lia sidecar must follow the current promoted visual anchor (`pink_hair`, `purple_eyes`, long/wavy hair, blue-gold academy uniform). Do not revert to earlier brown/green/white-serafuku placeholder metadata.

기본 분리:

- `identity_anchor`: 캐릭터 머리/눈/기본 동일성 태그
- `outfits`: 유지하거나 교체할 의상 태그 block
- `expression_map`: 표정별 face-local prompt tags
- `framing_defaults`: workflow별 기본 구도/카메라 subset
- `staging_defaults`: workflow별 기본 자세/작은 연출 subset
- `qa_policy`: sprite/event CG별 drift 허용 범위

## Assets

### bg_academy_demo_hall_afternoon

- asset_id: bg_academy_demo_hall_afternoon
- asset_type: background
- description: 에스텔라 왕립마법학원 제3마법시연장. 학원 내부 연구 발표회가 열리는 마도건축 시연장
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: scene_background
- required: required
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/kanban_t_409fa472_20260517_231137/background/bg_academy_demo_hall_afternoon_00001_.png
- promoted_game_path: game/images/generated/backgrounds/bg_academy_demo_hall_afternoon.png
- qa_status: promoted
- notes: 사용자 QA 승인 후 Ren'Py game directory에 promotion 완료. 기존 asset_id는 bg_academy_demo_hall_afternoon을 유지하되, canon 장소명은 magic_demo_hall_03 / 제3마법시연장이다.

### cg_unstable_magic_structure_demo

- asset_id: cg_unstable_magic_structure_demo
- asset_type: scene_event_cg
- description: 리아의 대표 마도건축 구조물이 불안정하게 빛나며 붕괴 직전인 장면
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: scene_event_cg
- required: optional
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/visual_polish_20260518_080656/scene_event_cg/cg_unstable_magic_structure_demo_00001_.png
- promoted_game_path: game/images/generated/event_cg/cg_unstable_magic_structure_demo.png
- qa_status: superseded_by_v2
- notes: 2026-05-18 scene_event_cg로 생성 후 prologue_001 cut-in으로 연결했으나, 조립 후 asset/dialogue alignment QA에서 리아 portrait 중심 구도와 안정적 마법 원 느낌이 `무너진다`/`세 갈래의 빛`/micro-choice beat와 약하게 맞는다고 판단되어 v2로 대체.

### cg_unstable_magic_structure_demo_v2

- asset_id: cg_unstable_magic_structure_demo_v2
- asset_type: scene_event_cg
- description: 제3마법시연장의 불안정한 마도건축 구조물이 금색 균열과 비틀린 구조선으로 붕괴 직전임을 보여주는 장면. 인물 중심이 아니라 구조물/기둥/공간 중심.
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: scene_event_cg
- required: required_visual
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/kanban_t_84689645_unstable_structure_20260519_0800/A_structure_first_seed846896452_00001_.png
- promoted_game_path: game/images/generated/event_cg/cg_unstable_magic_structure_demo_v2.png
- qa_status: promoted_for_user_review
- notes: 자율 제작 모드에서 director/QA 추천 A2 후보를 promotion. 도윤 얼굴 노출 없음. 첫 cut-in과 micro-choice base CG로 사용.

### overlay_three_structural_lines

- asset_id: overlay_three_structural_lines
- asset_type: transparent_overlay
- description: micro-choice에서 `중심부에서 조용히 비틀리는 선`, `가장 밝게 빛나는 장식선`, `아래쪽을 떠받치는 굵은 지지선` 세 후보를 화면상으로 구분시키는 투명 구조선 overlay
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: renpy_overlay/manual_composite
- required: required_visual
- source_path: none
- generated_output_path: pruned_after_promotion
- promoted_game_path: game/images/generated/overlays/overlay_three_structural_lines.png
- qa_status: promoted_for_user_review
- notes: A2 base CG 위에 menu beat 동안만 표시. 중앙 cyan 비틀림선/상단 gold 장식선/하단 blue 지지선을 분리해 첫 micro-choice의 선택 감각을 강화. 2026-05-19 runtime QA warning에 따라 상단 gold 장식선은 선택지 band 위로 올리고 하단 blue 지지선은 dialogue box 위로 올린 polish overlay로 교체. `.analysis` source/backup PNG는 promoted asset 확인 후 cleanup에서 제거.

### cg_lia_first_serious_look

- asset_id: cg_lia_first_serious_look
- asset_type: scene_event_cg
- description: 구조물 안정화 직후, 리아가 처음으로 웃음을 잃고 진지하게 도윤의 개입과 안정화된 구조선을 바라보는 cut-in
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: scene_event_cg
- required: required_visual
- source_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/hermes_vn_lia_serious_demo_hall_fix_20260521/manifest_lia_serious_demo_hall_fix.json
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/hermes_vn_lia_serious_demo_hall_fix_20260521/A2_no_magic_curtain_window_seed260521602_00001_.png
- promoted_game_path: game/images/generated/event_cg/cg_lia_first_serious_look.png
- qa_status: integrated_local_candidate_pending_post_swap_qa
- notes: 2026-05-21 director/QA top-pick A2 local integration candidate로 교체 반영. source prompt_id 25b94215-a24b-4f95-9514-888c12b55266 / seed 260521602 / contact_sheet `/mnt/c/Users/Desktop/Documents/ComfyUI/output/hermes_vn_lia_serious_demo_hall_fix_20260521/contact_sheets/lia_serious_demo_hall_fix_contact_sheet.png`. 기존 logical id와 Ren'Py path는 유지하고 파일 내용만 A2로 승계했다. 직전 A1 후보는 `.analysis/backups/20260521_t_0fa1ecc9/cg_lia_first_serious_look_before_A2_replacement.png`에 교체 전 백업으로 보존. cg_unstable_magic_structure_demo를 대체하지 않고 보완하는 리아 반응 CG. 삽입 위치는 구조물 안정화와 정적 이후, 리아의 “……너.” 직전. 리아 단독 중심 16:9 구도, serious/focused expression, quiet eye contact, no clear male face/couple shot/romance pose. A2는 제3마법시연장 stage/presentation read를 목표로 하되 generic academy stage 잔여 리스크가 있어 최종 game-ready 판정 전 runtime screenshot 및 asset-dialogue/location QA 필요.

### sprite_lia_bel_astrin_base

- asset_id: sprite_lia_bel_astrin_base
- asset_type: character_sprite
- description: 리아 벨 아스트린 기본 스탠딩 CG
- used_in_scene_id: common / prologue
- recommended_workflow: char_base + char_alpha
- required: required
- source_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/kanban_t_409fa472_20260517_231137/character/sprite_lia_bel_astrin_base_00001_.png
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/kanban_t_409fa472_20260517_231137/alpha/lia_base_alpha_00001_.png
- promoted_game_path: game/images/generated/sprites/lia_bel_astrin_base.png
- qa_status: promoted
- notes: 사용자 QA 승인 후 transparent alpha sprite를 Ren'Py game directory에 promotion 완료.

### sprite_lia_bel_astrin_expressions

- asset_id: sprite_lia_bel_astrin_expressions
- asset_type: character_expression_set
- description: 리아 표정 세트
- expression_tags: playful, curious, surprised, anxious, serious, forced_smile
- used_in_scene_id: common / prologue
- recommended_workflow: char_expression + char_alpha
- required: required
- source_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/kanban_t_409fa472_20260517_231137/expression/*_composited_00001_.png
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/kanban_t_409fa472_20260517_231137/alpha/lia_{playful,serious,surprised,curious,forced_smile}_alpha_00001_.png; /mnt/c/Users/Desktop/Documents/ComfyUI/output/missing_assets_20260518_075606/alpha/lia_anxious_alpha_00001_.png
- promoted_game_path: game/images/generated/sprites/lia_bel_astrin_{playful,serious,surprised,curious,forced_smile,anxious}.png
- qa_status: promoted
- notes: 사용자 QA/진행 승인 후 expression_tags 전체 transparent alpha sprite promotion 완료. 코드/asset_id/자동화 필드의 canonical expression tags는 영어 snake_case만 사용하고, 플레이어에게 보이는 speaker name은 항상 `리아`로 고정한다. 현재 스크립트 필요 표정은 playful, curious, surprised, serious, forced_smile이며 anxious는 보유/예비 에셋이다.

### bgm_academic_wonder

- asset_id: bgm_academic_wonder
- asset_type: bgm
- description: 학원 연구 발표회의 신비롭고 기대감 있는 배경음
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_bgm_ace + final_edit_ace_bgm_loop
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: ACE-Step 원본 MP3 후보를 만든 뒤 `comfyui-game-asset-workflows/scripts/final_edit_ace_bgm_loop.py`로 무음 trim/fade/OGG/loop preview를 생성하고 청감 QA 후 promotion한다. 첫 playable 구현에서는 임시 BGM 또는 무음 대체 가능.

### sfx_crowd_murmur_soft

- asset_id: sfx_crowd_murmur_soft
- asset_type: sfx
- description: 연구 발표회 관객의 낮은 웅성거림
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 시연장 분위기용.

### sfx_magic_structure_hum

- asset_id: sfx_magic_structure_hum
- asset_type: sfx
- description: 마도건축 구조물이 작동할 때 나는 낮은 마력 진동음
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library_or_sound_design
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 구조물 첫 등장 및 작동음.

### sfx_magic_pulse_light

- asset_id: sfx_magic_pulse_light
- asset_type: sfx
- description: 마법 구조물이 한 층 더 밝게 점등될 때의 짧은 마력 펄스음
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library_or_sound_design
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 리아의 시연 연출용.

### sfx_magic_structure_hum_louder

- asset_id: sfx_magic_structure_hum_louder
- asset_type: sfx
- description: 구조물 불안정이 커지며 마력 진동음이 강해지는 소리
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library_or_sound_design
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 사고 직전 긴장감 강화용.

### sfx_magic_crack

- asset_id: sfx_magic_crack
- asset_type: sfx
- description: 마력 구조가 균열처럼 갈라지는 소리
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library_or_sound_design
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 붕괴 직전 위험 신호.

### sfx_footstep_rush

- asset_id: sfx_footstep_rush
- asset_type: sfx
- description: 이도윤이 단상 아래로 뛰어드는 발소리
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 행동 전환 박자용.

### sfx_magic_distortion

- asset_id: sfx_magic_distortion
- asset_type: sfx
- description: 비틀린 마법 구조가 왜곡되는 소리
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library_or_sound_design
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 손을 뻗기 직전 긴장 연출.

### sfx_magic_snap

- asset_id: sfx_magic_snap
- asset_type: sfx
- description: 잘못 놓인 설계선이 옮겨지는 순간의 짧은 소리
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library_or_sound_design
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 이도윤의 구조 감각 발현 순간.

### sfx_magic_structure_stabilize

- asset_id: sfx_magic_structure_stabilize
- asset_type: sfx
- description: 불안정한 마법 구조가 안정화되는 맑은 공명음
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: audio_library_or_sound_design
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 사고 수습 직후 정적 전환 전 사용.

### bg_estella_academy_corridor_afternoon

- asset_id: bg_estella_academy_corridor_afternoon
- asset_type: background
- description: 에스텔라 왕립마법학원 제3마법시연장 인근 복도. 높은 창, 오후 빛, 학원 문장과 연구 성과 액자가 보이는 복도
- used_in_scene_id: prologue_002_corridor_escape
- recommended_workflow: scene_background
- required: required
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/kanban_t_409fa472_20260517_231137/background/bg_estella_academy_corridor_afternoon_00001_.png
- promoted_game_path: game/images/generated/backgrounds/bg_estella_academy_corridor_afternoon.png
- qa_status: promoted
- notes: 사용자 QA 승인 후 Ren'Py game directory에 promotion 완료.

### bg_lia_workshop_afternoon

- asset_id: bg_lia_workshop_afternoon
- asset_type: background
- description: 리아의 작업실. 마도건축 도면, 설계지, 마법석, 실험 도구, 왕립학원 연구 자료가 쌓인 오후의 작업실
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: scene_background
- required: required
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/missing_assets_20260518_075606/background/bg_lia_workshop_afternoon_00001_.png
- promoted_game_path: game/images/generated/backgrounds/bg_lia_workshop_afternoon.png
- qa_status: promoted
- notes: 사용자 진행 승인 후 Ren'Py game directory에 promotion 완료.


### prop_lia_mini_structure_model

- asset_id: prop_lia_mini_structure_model
- asset_type: scene_prop_cg
- description: 리아 작업실의 투명 판 위에 떠오른 축소 마도구조식 모델. 작은 고리 하나가 반 박자 늦게 움직이는 결함을 암시하는 소품 클로즈업
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: scene_prop_cg
- required: optional
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/visual_polish_20260518_080656/prop/prop_lia_mini_structure_model_00001_.png
- promoted_game_path: game/images/generated/props/prop_lia_mini_structure_model.png
- qa_status: promoted
- notes: 사용자 피드백(소품 확대/cut-in 필요)에 따라 2026-05-18 생성 후 prologue_003의 축소 모델 설명 beat에 연결.

### bgm_light_panic

- asset_id: bgm_light_panic
- asset_type: bgm
- description: 코미디성 혼란과 가벼운 도주 분위기의 BGM
- used_in_scene_id: prologue_002_corridor_escape
- recommended_workflow: audio_bgm_ace + final_edit_ace_bgm_loop
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 리아가 도윤을 끌고 나가는 복도 장면용. ACE-Step 원본 MP3 후보를 만든 뒤 `comfyui-game-asset-workflows/scripts/final_edit_ace_bgm_loop.py`로 무음 trim/fade/OGG/loop preview를 생성하고 청감 QA 후 promotion한다. 첫 playable 구현에서는 임시 BGM 또는 무음 대체 가능.

### sfx_crowd_murmur_fade

- asset_id: sfx_crowd_murmur_fade
- asset_type: sfx
- description: 시연장 관객의 웅성거림이 문 너머로 줄어드는 효과음
- used_in_scene_id: prologue_002_corridor_escape
- recommended_workflow: audio_library
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 시연장 밖 복도로 전환되는 공간감 연출.

### sfx_door_open

- asset_id: sfx_door_open
- asset_type: sfx
- description: 시연장 문이 열리는 소리
- used_in_scene_id: prologue_002_corridor_escape
- recommended_workflow: audio_library
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 시연장 탈출/복도 전환용.

### sfx_door_close

- asset_id: sfx_door_close
- asset_type: sfx
- description: 시연장 문이 닫히는 소리
- used_in_scene_id: prologue_002_corridor_escape
- recommended_workflow: audio_library
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 시연장 소음 차단 및 장면 전환용.

### sfx_footsteps_corridor

- asset_id: sfx_footsteps_corridor
- asset_type: sfx
- description: 왕립마법학원 복도 발소리
- used_in_scene_id: prologue_002_corridor_escape
- recommended_workflow: audio_library
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 복도 이동감 연출용.

## Workflow Pack Reference

Canonical ComfyUI workflow pack:

- WSL: /home/jisub-lee/workspace/comfyui-game-asset-workflows
- Windows UNC: \wsl.localhost\Ubuntu-24.04\home\jisub-lee\workspace\comfyui-game-asset-workflows

에셋 생성 전에는 다음 문서를 우선 확인한다.

1. README.md
2. WORKFLOW_INDEX.json
3. AGENTS.md
4. target workflow folder의 README.md
5. target *_workflow_api.json

## Notes

- 생성 이미지는 workflow pack 내부에 저장하지 않는다.
- 실제 생성 후에는 /history/{prompt_id} 또는 output folder scan으로 exact output path를 확인한다.
- QA 후 실제 게임에 사용할 이미지만 Ren'Py project의 game/images 또는 별도 promoted asset folder로 복사한다.
