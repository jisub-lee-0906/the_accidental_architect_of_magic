# 06 Asset Manifest

## Status Legend

- needed: 필요하지만 아직 생성되지 않음
- generated: 생성은 되었으나 QA 전
- qa_pending: QA 필요
- promoted: Ren'Py game directory에 사용 확정 반영됨

## Assets

### bg_academy_demo_hall_afternoon

- asset_id: bg_academy_demo_hall_afternoon
- asset_type: background
- description: 에스텔라 왕립마법학원 제3마법시연장. 학원 내부 연구 발표회가 열리는 마도건축 시연장
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: background_art
- required: required
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/kanban_t_409fa472_20260517_231137/background/bg_academy_demo_hall_afternoon_00001_.png
- promoted_game_path: game/images/generated/backgrounds/bg_academy_demo_hall_afternoon.png
- qa_status: promoted
- notes: 사용자 QA 승인 후 Ren'Py game directory에 promotion 완료. 기존 asset_id는 bg_academy_demo_hall_afternoon을 유지하되, canon 장소명은 magic_demo_hall_03 / 제3마법시연장이다.

### cg_unstable_magic_structure_demo

- asset_id: cg_unstable_magic_structure_demo
- asset_type: event_cg
- description: 리아의 대표 마도건축 구조물이 불안정하게 빛나며 붕괴 직전인 장면
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: event_cg
- required: optional
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/visual_polish_20260518_080656/event_cg/cg_unstable_magic_structure_demo_00001_.png
- promoted_game_path: game/images/generated/event_cg/cg_unstable_magic_structure_demo.png
- qa_status: promoted
- notes: 사용자 피드백(시각적 즐거움/집중도 강화)에 따라 2026-05-18 event_cg로 생성 후 prologue_001 cut-in으로 연결.

### sprite_lia_bel_astrin_base

- asset_id: sprite_lia_bel_astrin_base
- asset_type: character_sprite
- description: 리아 벨 아스트린 기본 스탠딩 CG
- used_in_scene_id: common / prologue
- recommended_workflow: character_anchor_base + transparency_alpha
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
- recommended_workflow: expression_variations + transparency_alpha
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
- recommended_workflow: audio_library_or_manual_composition
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 첫 playable 구현에서는 임시 BGM 또는 무음 대체 가능.

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
- recommended_workflow: background_art
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
- recommended_workflow: background_art
- required: required
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/missing_assets_20260518_075606/background/bg_lia_workshop_afternoon_00001_.png
- promoted_game_path: game/images/generated/backgrounds/bg_lia_workshop_afternoon.png
- qa_status: promoted
- notes: 사용자 진행 승인 후 Ren'Py game directory에 promotion 완료.


### prop_lia_mini_structure_model

- asset_id: prop_lia_mini_structure_model
- asset_type: prop_closeup_cg
- description: 리아 작업실의 투명 판 위에 떠오른 축소 마도구조식 모델. 작은 고리 하나가 반 박자 늦게 움직이는 결함을 암시하는 소품 클로즈업
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: prop_closeup_cg
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
- recommended_workflow: audio_library_or_manual_composition
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 리아가 도윤을 끌고 나가는 복도 장면용. 첫 playable 구현에서는 임시 BGM 또는 무음 대체 가능.

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
