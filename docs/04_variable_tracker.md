# 04 Variable Tracker

## Current Progress

- last_confirmed_scene_id: prologue_002_corridor_escape
- current_route: common
- current_branch: first_choice_a_concealment
- current_date: undecided
- current_time: afternoon

## Affection

- lia_affection: 1

## Protagonist Axes

- mc_concealment: 1
- mc_exposure: 0
- mc_responsibility: 0

## Active Flags

- flag_architecture_instinct_hidden

## Inactive / Planned Flags

- flag_architecture_talent_exposed
- flag_mc_cautious

## Items

- none

## Confirmed Canon Summary

- 작품 톤은 코미디로 시작해 점점 진지해지는 성장형 판타지이다.
- 주인공은 이도윤 / lee_do_yoon이며, Ren'Py 화자 id는 mc를 사용한다.
- 이도윤은 남성 26세, 현실 세계 구조설계 사무소 계약직 보조 설계원 출신 이세계 전이자이다.
- 이도윤은 야근 중 붕괴 위험 표시가 난 구조 검토 모델을 수정하다가, 모니터 속 도면 선과 마법진 선이 겹치며 이세계로 전이한다.
- 이도윤은 지친 현실주의자지만 구조적 위험 앞에서는 집요하게 움직이는 타입이다.
- 학원명은 에스텔라 왕립마법학원 / estella_royal_magic_academy이다.
- 리아가 소속된 학부는 마도건축학부 / faculty_of_arcane_architecture이다.
- 프롤로그 실제 장소명은 에스텔라 왕립마법학원 제3마법시연장 / magic_demo_hall_03이다.
- 첫 번째 히로인은 리아 벨 아스트린 / lia_bel_astrin이다.
- 리아는 문제아 천재 마도건축가이며, 겉은 가볍지만 속은 불안한 천재이다.
- 리아는 자신이 만든 대표 설계가 불완전하다는 걸 알고 있다.
- 주인공과 리아의 관계 구도는 “멈추는 법을 아는 사람과, 멈추지 못하는 사람”이다.
- 프롤로그 사건은 에스텔라 왕립마법학원 제3마법시연장에서 열리는 학원 내부 연구 발표회의 공개 시연장 붕괴 직전 사건이다.
- prologue_001_public_demo_collapse에서 이도윤은 리아의 마도건축 구조물이 붕괴 직전인 원인을 “비틀림”으로 알아보고, 설계선 또는 마력 흐름을 안정화한다.
- 리아는 도윤이 자신이 고치지 못한 결함을 알아봤다는 사실 때문에 처음으로 웃음을 잃는다.
- 씬은 리아의 질문 “너, 방금 뭘 한 거야?”와 첫 선택지로 종료된다.
- 첫 선택지는 리아의 “너, 방금 뭘 한 거야?” 질문 직후 등장한다.
- 선택지 A가 적용되어, 도윤은 “저도 모르겠는데요. 무너질 것 같아서요.”라고 답하며 자신의 감각을 축소한다.
- 하지만 도윤은 곧 “선이 이상했다 / 받치는 게 아니라 비틀고 있었다”고 말해버려 자신의 감각을 완전히 숨기지는 못한다.
- 리아는 도윤의 “모른다”는 답을 오히려 더 위험하고 흥미로운 단서로 받아들인다.
- 리아는 도윤을 “비공식 시연 보조자”라고 주장하며 교수진의 즉각적인 통제에서 빼내려 한다.
- 리아는 도윤을 데리고 제3마법시연장 밖 복도로 빠져나간다.
- 리아는 도윤에게 “받치는 게 아니라 비틀고 있었다”는 말을 아무에게나 하지 말라고 경고한다.
- 리아는 도윤이 본 것을 누가 먼저 해석하느냐에 따라 도윤이 천재가 될 수도, 범죄자가 될 수도 있다고 말한다.
- 도윤은 구조물을 눈으로만 본 것이 아니라 머릿속에 도면처럼 떠올랐다고 말한다.
- 리아는 이 대답을 듣고 도윤을 자신의 작업실로 데려가기로 한다.

## Planned First Choice Effects

### A. "저도 모르겠는데요. 무너질 것 같아서요."

- lia_affection +1
- mc_concealment +1
- flag_architecture_instinct_hidden = true

### B. "그 선이 받치는 게 아니라 비틀고 있었어요."

- lia_affection +2
- mc_exposure +1
- flag_architecture_talent_exposed = true

### C. "제가 뭘 잘못 건드렸나요?"

- lia_affection 0
- mc_responsibility +1
- flag_mc_cautious = true

## Future Decisions / Pending Implementation

- prologue_001 실제 대본: docs/scenes/prologue_001_public_demo_collapse.md에 canon_confirmed 상태로 저장됨
- prologue_001a 선택지 A 후속 대본: docs/scenes/prologue_001a_instinct_hidden.md에 canon_confirmed 상태로 저장됨
- prologue_002 복도 이동 대본: docs/scenes/prologue_002_corridor_escape.md에 canon_confirmed 상태로 저장됨
- 리아 외 주요 캐릭터
- 리아 루트 조건
- 에셋 생성 및 promotion 상태
