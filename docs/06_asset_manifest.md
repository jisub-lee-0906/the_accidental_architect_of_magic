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
- description: 학원 내부 연구 발표회가 열리는 마도건축 시연장
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: background_art
- required: required
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 캐릭터 없는 16:9 VN 배경.

### cg_unstable_magic_structure_demo

- asset_id: cg_unstable_magic_structure_demo
- asset_type: event_cg
- description: 리아의 대표 마도건축 구조물이 불안정하게 빛나며 붕괴 직전인 장면
- used_in_scene_id: prologue_001_public_demo_collapse
- recommended_workflow: event_cg
- required: optional
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: 캐릭터 포함 여부는 prologue_001 대본 확정 후 결정.

### sprite_lia_bel_astrin_base

- asset_id: sprite_lia_bel_astrin_base
- asset_type: character_sprite
- description: 리아 벨 아스트린 기본 스탠딩 CG
- used_in_scene_id: common / prologue
- recommended_workflow: character_anchor_base
- required: required
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: source/base/anchor image 필요.

### sprite_lia_bel_astrin_expressions

- asset_id: sprite_lia_bel_astrin_expressions
- asset_type: character_expression_set
- description: 리아 표정 세트 playful, curious, surprised, anxious, serious, forced_smile
- used_in_scene_id: common / prologue
- recommended_workflow: expression_variations + transparency_alpha
- required: required
- source_path: none
- generated_output_path: none
- promoted_game_path: none
- qa_status: needed
- notes: dialogue sprite는 source/outfit -> expression -> alpha 흐름으로 제작.

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
- description: 주인공이 단상 아래로 뛰어드는 발소리
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
- notes: 주인공의 구조 감각 발현 순간.

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
