# prologue_001a_instinct_hidden

## Metadata

- scene_id: prologue_001a_instinct_hidden
- route: common
- branch: first_choice_a_concealment
- location: academy_demo_hall
- canon_location_name: 에스텔라 왕립마법학원 제3마법시연장
- canon_location_id: magic_demo_hall_03
- time: afternoon
- status: canon_confirmed
- script_status: not_implemented
- last_updated: 2026-05-17

## Purpose

- 첫 선택지 A의 결과를 반영한다.
- 도윤의 은폐/회피 성향을 보여준다.
- 리아가 도윤의 “모른다”는 답을 오히려 더 흥미로운 단서로 받아들이게 한다.
- 교수진이 도윤을 신원 불명의 외부인으로 경계하기 시작한다.
- 리아가 도윤을 비공식 시연 보조자라고 우기며 교수진의 즉각적인 통제에서 빼내려 한다.

## Applied Choice

A. “저도 모르겠는데요. 무너질 것 같아서요.”

- lia_affection +1
- mc_concealment +1
- flag_architecture_instinct_hidden = true

## Canon Scene

[SCENE_ID: prologue_001a_instinct_hidden]
[ROUTE: common]
[BRANCH: first_choice_a_concealment]
[LOCATION: academy_demo_hall]
[CANON_LOCATION: magic_demo_hall_03 / 에스텔라 왕립마법학원 제3마법시연장]
[TIME: afternoon]

[BG: bg_academy_demo_hall_afternoon]
[BGM: stop]
[SFX: sfx_crowd_murmur_soft]

[CHOICE_SELECTED]
A. “저도 모르겠는데요. 무너질 것 같아서요.”
   - lia_affection +1
   - mc_concealment +1
   - flag_architecture_instinct_hidden = true

[도윤]
“저도 모르겠는데요. 무너질 것 같아서요.”

[지문]
말하고 나서, 도윤은 곧바로 후회했다.

너무 솔직했다.

아니, 솔직한 척하면서 아무것도 설명하지 않은 대답이었다.

현실에서라면 회의록에 남기기 가장 나쁜 종류의 문장.

[도윤]
“그러니까, 정확히는…… 위험해 보여서요.”

[SHOW: lia_bel_astrin serious center]

리아:
“위험해 보였다.”

[지문]
리아는 그 말을 천천히 되풀이했다.

시연장은 여전히 조용했다.

교수들은 서로 눈빛을 주고받고 있었고, 학생들은 도윤과 리아 사이에 보이지 않는 선이라도 생긴 것처럼 물러서 있었다.

리아:
“내 설계식이?”

[도윤]
“제가 그걸 설계식이라고 부르는 게 맞는지도 모르겠는데요.”

리아:
“그럼 넌 뭘 봤는데?”

[지문]
도윤은 공중에 멈춰 선 빛의 구조물을 바라보았다.

방금 자신이 옮긴 선은 다른 선들 사이에 조용히 섞여 있었다.

마치 처음부터 그 자리에 있었던 것처럼.

[도윤]
“그냥…… 선이 이상했습니다.”

[SHOW: lia_bel_astrin surprised center]

리아:
“선?”

[도윤]
“받치는 것처럼 보였는데, 실제론 비틀고 있었어요. 그래서 무너질 것 같았고요.”

[지문]
도윤은 말을 멈췄다.

모른다고 해놓고, 너무 많이 설명했다.

[도윤]
“아니, 그러니까 제 말은…… 그냥 감입니다. 감.”

[SHOW: lia_bel_astrin curious center]

리아:
“감.”

[지문]
리아의 눈이 다시 빛났다.

이번에는 시연장의 마법 구조물보다 훨씬 위험한 방식으로.

리아:
“마법을 모르는 사람이, 내 설계식의 결함을 감으로 보고, 손으로 고쳤다?”

[도윤]
“그렇게 정리하시면 제가 많이 불리해지는데요.”

[SHOW: lia_bel_astrin playful center]

리아:
“좋아. 그럼 더 재밌네.”

[지문]
리아의 입가에 웃음이 돌아왔다.

하지만 이번 웃음은 아까와 달랐다.

시연장을 가볍게 휘어잡던 웃음이 아니라, 눈앞의 수수께끼를 절대 놓치지 않겠다는 연구자의 웃음이었다.

교수:
“리아 아스트린. 그 인물에게서 물러나라.”

리아:
“학생인지 아닌지도 아직 모르는데요?”

교수:
“그래서 더 문제다. 신원 불명의 외부인이 왕립학원의 시연식에 개입했다.”

[지문]
그 말에 도윤은 뒤늦게 현실감을 되찾았다.

왕립학원.
신원 불명.
시연식 개입.

어느 단어 하나도 가볍지 않았다.

[도윤]
“잠깐만요. 저는 일부러 들어온 게 아니라—”

리아:
“맞아. 일부러 들어온 게 아니지.”

[지문]
리아가 도윤의 말을 가로챘다.

그리고 아주 자연스럽게, 도윤의 소매를 붙잡았다.

리아:
“내가 데려온 거니까.”

[도윤]
“네?”

교수:
“리아 아스트린.”

리아:
“시연 보조자예요. 비공식이지만.”

[지문]
도윤은 리아를 보았다.

리아는 웃고 있었다.

분명 웃고 있었지만, 손끝에는 힘이 들어가 있었다.

도윤을 놓치지 않겠다는 듯이.

[도윤]
“저기요. 방금 처음 뵌 사이인데요.”

리아:
“그러니까 조용히 해. 지금 잡혀가면 너도 귀찮고, 나도 귀찮아.”

[도윤]
“이미 충분히 귀찮은 것 같은데요.”

리아:
“에스텔라에 온 걸 환영해. 원래 여긴 더 귀찮아.”

[SFX: sfx_crowd_murmur_soft]

[지문]
시연장 전체가 다시 웅성거리기 시작했다.

교수진은 도윤을 경계했고, 학생들은 리아가 또 사고를 쳤다는 표정이었다.

그리고 리아는 그 모든 시선을 무시한 채 도윤의 소매를 잡고 있었다.

리아:
“자, 이도윤.”

[도윤]
“제 이름은 어떻게—”

리아:
“몰라. 방금 네가 중얼거렸어.”

[지문]
도윤은 기억나지 않았다.

하지만 지금 중요한 건 그게 아니었다.

리아가 한 걸음 가까이 다가왔다.

리아:
“네가 정말 아무것도 모른다면, 더 좋아.”

[SHOW: lia_bel_astrin serious center]

리아:
“선입견이 없다는 뜻이니까.”

[지문]
그 말은 장난처럼 들리지 않았다.

도윤은 다시 공중의 구조물을 올려다보았다.

조용히 안정된 빛의 선들 사이에서, 자신이 옮긴 한 줄이 희미하게 떨리고 있었다.

마치 아직 끝나지 않았다고 말하는 것처럼.

[도윤]
“저, 혹시 집에 가는 방법부터 물어봐도 됩니까?”

리아:
“물어보는 건 자유야.”

[지문]
리아가 환하게 웃었다.

리아:
“대답해준다는 말은 안 했지만.”

[END_SCENE]

## Branch Effects

- lia_affection: 1
- mc_concealment: 1
- mc_exposure: 0
- mc_responsibility: 0
- active_flags:
  - flag_architecture_instinct_hidden
- inactive_or_planned_flags:
  - flag_architecture_talent_exposed
  - flag_mc_cautious

## Required Assets

### bg_academy_demo_hall_afternoon

- asset_id: bg_academy_demo_hall_afternoon
- type: background
- required: required
- current_status: needed
- notes: 기존 에셋 재사용. canon 장소명은 에스텔라 왕립마법학원 제3마법시연장.

### sprite_lia_bel_astrin_expressions

- asset_id: sprite_lia_bel_astrin_expressions
- type: character_expression_set
- required: required
- current_status: needed
- needed_expressions: serious, surprised, curious, playful, forced_smile

### sfx_crowd_murmur_soft

- asset_id: sfx_crowd_murmur_soft
- type: sfx
- required: optional
- current_status: needed
- notes: 기존 에셋 후보 재사용.

## Doc Update Notes

### docs/04_variable_tracker.md update proposal

Current Progress:

- last_confirmed_scene_id: prologue_001a_instinct_hidden
- current_route: common
- current_branch: first_choice_a_concealment
- current_time: afternoon

Affection:

- lia_affection: 1

Protagonist Axes:

- mc_concealment: 1
- mc_exposure: 0
- mc_responsibility: 0

Active Flags:

- flag_architecture_instinct_hidden

Inactive / Planned Flags:

- flag_architecture_talent_exposed
- flag_mc_cautious

Confirmed Canon Summary에 추가할 내용:

- 도윤은 첫 질문에 “저도 모르겠는데요. 무너질 것 같아서요.”라고 답하며 자신의 감각을 축소한다.
- 하지만 도윤은 곧 “선이 이상했다 / 받치는 게 아니라 비틀고 있었다”고 말해버려 자신의 감각을 완전히 숨기지는 못한다.
- 리아는 도윤의 “모른다”는 답을 오히려 더 위험하고 흥미로운 단서로 받아들인다.
- 리아는 도윤을 “비공식 시연 보조자”라고 주장하며 교수진의 즉각적인 통제에서 빼내려 한다.

### docs/06_asset_manifest.md update proposal

현재 이 씬에서 새 이미지 에셋은 없다.

다음 씬이 시연장 밖으로 이동하면 아래 배경이 필요할 수 있다.

- asset_id: bg_estella_academy_corridor_afternoon
- asset_type: background
- description: 에스텔라 왕립마법학원 마도건축학부로 이어지는 복도
- used_in_scene_id: 다음 후속 씬 후보
- recommended_workflow: scene_background
- required: required if next scene moves outside demo hall
- qa_status: needed
