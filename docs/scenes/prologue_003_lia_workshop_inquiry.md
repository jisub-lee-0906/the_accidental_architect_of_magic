# prologue_003_lia_workshop_inquiry

## Metadata

- scene_id: prologue_003_lia_workshop_inquiry
- label: prologue_003_lia_workshop_inquiry
- route: common
- branch: first_choice_a_concealment
- location: lia_workshop
- canon_location_name: 에스텔라 왕립마법학원 마도건축학부 리아의 작업실
- time: afternoon
- status: canon_candidate_for_vertical_slice
- script_status: placeholder_implemented_in_game_script
- last_updated: 2026-05-17

## Canon / Candidate / Deferred Boundary

### Confirmed canon inputs

- 이도윤 / lee_do_yoon은 현실 세계 구조설계 사무소 계약직 보조 설계원 출신 이세계 전이자이다.
- 현재 분기는 first_choice_a_concealment이다.
- active flag는 flag_architecture_instinct_hidden이다.
- 현재 변수 상태는 lia_affection 1, mc_concealment 1, mc_exposure 0, mc_responsibility 0이다.
- prologue_002_corridor_escape의 끝에서 리아는 도윤을 자신의 작업실로 데려가기로 했다.
- 도윤은 구조물을 눈으로만 본 것이 아니라 머릿속에 도면처럼 떠올랐다고 말했다.
- 리아는 도윤이 본 것을 누가 먼저 해석하느냐에 따라 도윤이 천재가 될 수도, 범죄자가 될 수도 있다고 경고했다.

### Candidate in this scene card

- 리아의 작업실 첫 인상과 구체적 배치.
- 작업실 문에 교수진의 즉각적인 감청을 막는 얇은 마법 차단막이 걸린다는 연출.
- 리아가 축소 마도구조식 모델로 도윤의 구조 감각을 확인한다는 장면.
- 도윤이 작은 결함을 “보인다”기보다 “불편하다 / 신경 쓰인다”로 감지한다는 표현.
- 도윤이 당장 집에 갈 수 없음을 받아들이고, 위험하면 멈춘다는 조건으로 설명을 시작하는 엔드 비트.

### Deferred / not canon here

- 리아 외 주요 캐릭터 이름과 역할.
- 리아 루트 진입 조건.
- 도윤의 능력 원리, 전이 원인, 후반 세계관 진실.
- 작업실의 정식 호실명, 학부 내 행정 구조, 교수진 이름.
- 새 시스템 flag 확정. 필요하면 later route gate에서 별도 검토한다.

## Purpose

- prologue_001~003 playable vertical slice의 마지막 대화/확인 장면으로 기능한다.
- 리아의 작업실이라는 새 배경 장소를 도입한다.
- 도윤의 구조 감각이 기존 마법 이론만으로 설명되지 않을 수 있음을 암시한다.
- 리아가 도윤을 이용하려는 흥미와 보호하려는 불안을 동시에 보이게 한다.
- 도윤이 집에 가고 싶어하지만, 당장 혼자 떠날 수 없고 리아와 협력해야 한다는 방향을 받아들이게 한다.
- 다음 선택지 또는 협력관계의 기반을 만든다.

## Current State Before Scene

- last_confirmed_scene_id: prologue_002_corridor_escape
- current_route: common
- current_branch: first_choice_a_concealment
- current_date: undecided
- current_time: afternoon
- lia_affection: 1
- mc_concealment: 1
- mc_exposure: 0
- mc_responsibility: 0
- active_flags:
  - flag_architecture_instinct_hidden
- inactive_or_planned_flags:
  - flag_architecture_talent_exposed
  - flag_mc_cautious

## Canon Scene

Scene card status:

- 아래 본문은 prologue_001~003 vertical slice용 scene card 후보이다.
- 기존 확정 canon과 충돌하지 않는다.
- 작업실 세부 배치, 차단막, 축소 모델은 이 씬 안에서만 쓰는 후보 설정이며, director confirmation 전까지 broader world canon으로 확장하지 않는다.
- Ren'Py 구현 또는 ComfyUI 실행은 포함하지 않는다.

```text
[SCENE_ID: prologue_003_lia_workshop_inquiry]
[ROUTE: common]
[BRANCH: first_choice_a_concealment]
[LOCATION: lia_workshop]
[CANON_LOCATION: 에스텔라 왕립마법학원 마도건축학부 리아의 작업실]
[TIME: afternoon]

[BG: bg_lia_workshop_afternoon]
[BGM: bgm_curious_investigation]
[SFX: sfx_door_unlock_magic]
```

### Beat 1. 작업실 도착

리아는 도윤을 작업실 안으로 데려온다. 작업실은 정돈된 연구실이 아니라 사고 직전의 설계 현장처럼 보인다.

Visual notes:

- 벽면: 마도건축 도면, 실패한 설계식 메모, 붉은 수정 표시.
- 책상: 설계지, 마법석, 반쯤 식은 찻잔, 자, 필기구.
- 바닥: 말린 도면과 작은 구조 모형 부품.
- 위험물은 과장하지 않는다. 초반 코미디용으로만 보여준다.

Key dialogue:

```text
도윤:
“여기가 작업실입니까, 사고 수습 전 현장입니까?”

리아:
“둘 다 비슷한 말이야.”

도윤:
“그 말이 제 불안을 전혀 줄여주지 않는데요.”
```

### Beat 2. 감청 방지와 도윤의 미세 감각

리아는 문에 얇은 마법 차단막을 건다. 이 장면은 대규모 결계 설정을 확정하지 않는다. 작업실 대화를 교수진이 바로 듣지 못하게 하는 간단한 연출로만 사용한다.

Key action:

- 리아가 손가락으로 문 근처의 허공을 긋는다.
- 문틀에 얇은 빛의 선이 생겼다가 사라진다.
- 도윤은 문틀 위쪽이 미세하게 떨리는 것을 “보는” 것이 아니라 “불편하게 느낀다.”

Key dialogue:

```text
도윤:
“문틀 위쪽이 좀 떨리는데요.”

리아:
“보여?”

도윤:
“보인다기보다는…… 불편합니다.”

리아:
“좋아. 그 표현, 아주 마음에 들어.”

도윤:
“저는 마음에 안 듭니다.”
```

Function:

- 도윤의 감각이 시각 정보만이 아니라 구조적 불편감에 가깝다는 점을 암시한다.
- 리아는 이를 연구 대상으로 보면서도, 교수진에게 넘기면 위험하다는 점을 알고 있다.

### Beat 3. 리아의 흥미와 불안

리아는 도윤을 앉히지 않고 바로 작은 확인을 준비한다. 그러나 “실험체”처럼 잔혹하게 다루지 않는다. 리아의 말투는 장난스럽지만, 도윤이 다칠 수 있는 상황은 피하려 한다.

Key dialogue:

```text
리아:
“좋은 소식부터 말할까, 나쁜 소식부터 말할까?”

도윤:
“집에 가는 방법부터 말해주시면 안 됩니까?”

리아:
“그건 지금 내가 제일 못 하는 대답이야.”

도윤:
“그러면 좋은 소식이 없다는 뜻 같은데요.”

리아:
“좋은 소식은, 네가 아직 교수님들 손에 안 넘어갔다는 거.”

도윤:
“나쁜 소식은요?”

리아:
“내 손에 넘어왔다는 거?”

도윤:
“분류가 이상합니다.”
```

Function:

- 리아는 도윤을 이용하려는 흥미를 숨기지 않는다.
- 동시에 교수진이 먼저 해석하면 도윤이 위험해질 수 있다는 불안을 드러낸다.
- 도윤은 귀가를 요구하지만, 당장 답이 없다는 현실을 처음 받아들이기 시작한다.

### Beat 4. 축소 마도구조식 모델

리아는 책상 위의 투명 판 또는 작은 구조 모형을 꺼낸다. 이 모델은 prologue_001의 대형 구조물과 같은 계열이지만, playable vertical slice에서는 대사와 지문만으로 구현 가능해야 한다.

Key action:

- 투명 판 위에 작은 빛의 선들이 떠오른다.
- 리아는 위험하지 않은 범위라고 설명한다.
- 도윤은 마법 용어를 이해하지 못하지만, 구조 흐름의 지연을 알아본다.

Key dialogue:

```text
리아:
“이건 아까 시연식의 축소 모델이야. 훨씬 작고, 훨씬 덜 위험한 버전.”

도윤:
“덜 위험하다는 말은 위험하다는 뜻이죠?”

리아:
“이제 잘 알아듣네.”

도윤:
“칭찬처럼 들리지 않습니다.”

리아:
“그럼 봐. 마법으로 보려고 하지 말고, 네 방식으로.”

도윤:
“저는 원래 마법으로 볼 줄 모릅니다.”

리아:
“그러니까 좋은 거야.”
```

### Beat 5. 기존 마법 이론으로 설명되지 않는 감각 암시

도윤은 축소 모델의 작은 고리 또는 연결부 하나가 전체보다 반 박자 늦게 따라오는 것을 짚는다. 이 지점은 리아가 아무에게도 말하지 않았던 결함이다.

Key dialogue:

```text
도윤:
“저 작은 고리요. 전체가 같이 돌아야 안정적인 것 같은데, 저 부분만 반 박자 늦습니다.”

리아:
“……그걸 봤어?”

도윤:
“보였다기보다는, 거기만 계속 신경 쓰입니다.”

리아:
“그건 내가 아무에게도 말 안 한 부분이야.”

도윤:
“그럼 저는 못 들은 걸로 하겠습니다.”

리아:
“이미 봤잖아.”
```

Function:

- 도윤의 감각이 기존 마법 이론 검증과 다른 방식으로 결함을 포착한다는 점을 암시한다.
- “왜 가능한가”는 설명하지 않는다. 후반 원리 확장은 보류한다.

### Beat 6. 협력관계의 시작

리아는 도윤에게 마법 용어가 아니라 건축/구조 방식으로 설명해달라고 요청한다. 도윤은 집으로 돌아가고 싶지만, 현재 상황에서는 리아와 협력하는 것이 가장 덜 위험하다고 판단한다.

Key dialogue:

```text
리아:
“마법으로는 못 찾았어. 그러니까 네 방식으로 설명해줘.”

도윤:
“제가 설명할 수 있는 종류인지 모르겠습니다.”

리아:
“그럼 설명할 수 있는 모양으로 바꿔.”

도윤:
“종이 있습니까?”

리아:
“종이?”

도윤:
“그림으로 설명하는 게 빠를 것 같습니다.”

리아:
“좋아.”

도윤:
“그리고 그 다음엔 집에 가는 방법을 알아봅니다.”

리아:
“응. 그 다음엔.”

도윤:
“방금 대답이 매우 불안했습니다.”

리아:
“불안해도 지금은 여기 있는 게 제일 안전해.”
```

End beat:

도윤은 잠시 문 쪽을 본다. 교수진에게 넘겨지는 것, 신원 불명자로 붙잡히는 것, 아무것도 모른 채 혼자 나가는 것. 어느 쪽도 집으로 돌아가는 길처럼 보이지 않는다. 도윤은 펜을 잡는다.

```text
도윤:
“좋습니다. 설명은 해보겠습니다. 대신 위험하면 멈춥니다.”

리아:
“그 말, 마음에 들어.”

[END_SCENE]
```

## Branch Effects

No new variable changes are recommended for this scene card.

Current branch state remains:

- lia_affection: 1
- mc_concealment: 1
- mc_exposure: 0
- mc_responsibility: 0
- active_flags:
  - flag_architecture_instinct_hidden

Do not add these as active flags yet:

- flag_mc_blueprint_vision_confirmed
- flag_lia_hidden_defect_confirmed
- flag_lia_workshop_access

Reason:

- The scene establishes the cooperation basis for the vertical slice.
- Additional flags should wait until a later explicit choice or route-gating need.
- For the playable vertical slice, the existing A branch state is enough.

## Required Assets

### required_visual

#### bg_lia_workshop_afternoon

- asset_id: bg_lia_workshop_afternoon
- asset_type: background
- description: 리아의 작업실. 마도건축 도면, 설계지, 마법석, 실험 도구, 왕립학원 연구 자료가 어지럽게 쌓인 오후의 작업실
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: background_art
- required: required
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/missing_assets_20260518_075606/background/bg_lia_workshop_afternoon_00001_.png
- promoted_game_path: game/images/generated/backgrounds/bg_lia_workshop_afternoon.png
- qa_status: promoted
- notes: 사용자 진행 승인 후 Ren'Py game directory에 promotion 완료.

#### sprite_lia_bel_astrin_expressions

- asset_id: sprite_lia_bel_astrin_expressions
- asset_type: character_expression_set
- description: 리아 표정 세트
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: expression_variations + transparency_alpha
- required: required
- qa_status: promoted
- needed_expressions: playful, curious, surprised, anxious, serious, forced_smile
- promoted_game_path: game/images/generated/sprites/lia_bel_astrin_{playful,curious,surprised,anxious,serious,forced_smile}.png
- notes: 기존 manifest 항목 재사용. expression_tags 전체 promotion 완료.

### optional_audio

#### bgm_curious_investigation

- asset_id: bgm_curious_investigation
- asset_type: bgm
- description: 작업실에서 리아가 도윤의 구조 감각을 확인하는 장면용. 호기심, 조사, 가벼운 긴장감
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: audio_library_or_manual_composition
- required: optional
- qa_status: needed
- notes: 첫 구현에서는 무음 또는 임시 BGM 가능.

#### sfx_door_unlock_magic

- asset_id: sfx_door_unlock_magic
- asset_type: sfx
- description: 작업실 문에 감청 방지 마법을 거는 짧은 효과음
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: audio_library_or_sound_design
- required: optional
- qa_status: needed

#### sfx_cup_rattle

- asset_id: sfx_cup_rattle
- asset_type: sfx
- description: 작업실 잡동사니 또는 찻잔이 흔들리는 가벼운 효과음
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: audio_library
- required: optional
- qa_status: needed

### later_polish

#### prop_lia_mini_structure_model

- asset_id: prop_lia_mini_structure_model
- asset_type: prop_closeup_cg
- description: 투명 판 위에 빛의 선들이 떠 있는 축소 마도구조식 모델. 작은 고리 하나가 반 박자 늦게 움직이는 결함을 암시
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: prop_closeup_cg
- required: optional
- source_path: none
- generated_output_path: /mnt/c/Users/Desktop/Documents/ComfyUI/output/visual_polish_20260518_080656/prop/prop_lia_mini_structure_model_00001_.png
- promoted_game_path: game/images/generated/props/prop_lia_mini_structure_model.png
- qa_status: promoted_and_wired
- notes: 사용자 피드백에 따라 첫 playable polish로 승격. prologue_003의 축소 모델 설명 beat에 close-up cut-in으로 연결.

#### cg_lia_workshop_blueprint_explanation

- asset_id: cg_lia_workshop_blueprint_explanation
- asset_type: event_cg
- description: 도윤이 리아 앞에서 종이에 구조를 그려 설명하기 시작하는 장면
- used_in_scene_id: prologue_003_lia_workshop_inquiry
- recommended_workflow: event_cg
- required: optional
- qa_status: needed
- notes: vertical slice 필수 아님. 체험판 연출 강화용 후보.

## Completion Criteria

### Scene-level criteria

- 리아 작업실 도착이 명확하다.
- 도윤이 집에 가고 싶어하지만 당장 떠날 수 없다는 현실을 받아들이는 방향이 드러난다.
- 리아가 도윤을 이용하려는 흥미와 보호하려는 불안을 모두 보인다.
- 도윤의 구조 감각은 “기존 마법 이론으로 설명되지 않을 수 있음”까지만 암시하고 원리는 설명하지 않는다.
- 후반 루트, 새 히로인, 대규모 세계관 진실을 추가하지 않는다.
- 다음 선택지 또는 협력관계로 이어질 수 있다.

### Implementation-readiness criteria

- Ren'Py label 후보는 scene_id와 동일하게 `prologue_003_lia_workshop_inquiry`를 사용한다.
- 필수 visual은 `bg_lia_workshop_afternoon`과 리아 표정 sprite 세트뿐이다.
- `prop_lia_mini_structure_model`은 later_polish로 남겨도 씬 진행이 가능하다.
- 새 시스템 변수나 flag 없이 현재 A branch 상태만으로 구현 가능하다.

## Doc Update Notes

### docs/04_variable_tracker.md update proposal

Only apply after director confirms this scene card as canon.

Current Progress:

- last_confirmed_scene_id: prologue_003_lia_workshop_inquiry
- current_route: common
- current_branch: first_choice_a_concealment
- current_time: afternoon

Variable state:

- lia_affection: 1
- mc_concealment: 1
- mc_exposure: 0
- mc_responsibility: 0
- active_flags:
  - flag_architecture_instinct_hidden

Confirmed Canon Summary에 추가할 내용:

- 리아는 도윤을 자신의 작업실로 데려가 교수진이 바로 대화를 듣지 못하게 한다.
- 도윤은 작업실 문틀의 미세한 떨림을 “보인다”기보다 “불편하다”고 느끼며 다시 구조 감각을 보인다.
- 리아는 축소 마도구조식 모델을 보여주고, 도윤은 작은 고리가 반 박자 늦게 움직이는 점을 알아본다.
- 리아는 그 부분이 자신이 아무에게도 말하지 않은 결함임을 인정한다.
- 리아는 도윤에게 마법이 아닌 그의 방식으로 결함을 설명해달라고 부탁한다.
- 도윤은 당장 집에 갈 수 없음을 받아들이고, 위험하면 멈춘다는 조건으로 설명을 시작한다.

Future Decisions / Pending Implementation에 추가할 내용:

- prologue_003 작업실 심문/설명 scene card: docs/scenes/prologue_003_lia_workshop_inquiry.md에 저장됨
- 리아 작업실 세부 배경 에셋 생성 및 QA 필요

### docs/06_asset_manifest.md update proposal

Only apply after director confirms this scene card as canon or when asset planning is promoted.

Add required_visual:

- bg_lia_workshop_afternoon

Reuse required_visual:

- sprite_lia_bel_astrin_expressions

Add optional_audio:

- bgm_curious_investigation
- sfx_door_unlock_magic
- sfx_cup_rattle

Add later_polish:

- prop_lia_mini_structure_model
- cg_lia_workshop_blueprint_explanation

### docs/03_route_flowchart.md update proposal

Only apply after director confirms this scene card as canon.

Common Route에 추가:

- prologue_003_lia_workshop_inquiry
  - route: common
  - branch: first_choice_a_concealment
  - event: 리아가 도윤을 작업실로 데려가 그의 구조 감각을 확인하고, 도윤이 당장 떠날 수 없음을 받아들이며 협력 기반이 생김.
  - result: 다음 선택지 또는 협력관계 장면으로 연결

## Canon Conflict Check

- 발견된 canon 충돌: none
- 주의점: `lia_workshop`, `bg_lia_workshop_afternoon`, 차단막, 축소 마도구조식 모델은 현재 scene card 후보이며, director confirmation 전까지 master lore 또는 route canon으로 승격하지 않는다.
- 새 heroine, late route, 대규모 세계관 확장은 추가하지 않았다.
