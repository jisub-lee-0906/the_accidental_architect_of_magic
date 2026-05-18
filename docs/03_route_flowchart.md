# 03 Route Flowchart

## Current Route Structure

- common route: planned
- lia route: undecided
- other routes: undecided
- true route: undecided

## Common Route

### prologue_001_public_demo_collapse

- route: common
- event: 리아 벨 아스트린의 대표 마도건축 구조물이 에스텔라 왕립마법학원 제3마법시연장의 내부 연구 발표회에서 붕괴 직전까지 불안정해짐.
- location: academy_demo_hall
- canon_location_name: 에스텔라 왕립마법학원 제3마법시연장
- canon_location_id: magic_demo_hall_03
- time: undecided
- mc_action: 이도윤이 구조적 비틀림을 알아보고 설계선 또는 마력 흐름을 안정화함.
- result:
  - 구조물은 안정화된다.
  - 리아는 처음으로 웃음을 잃는다.
  - 교수진은 이도윤을 정체불명의 위험한 인물로 본다.
  - 이도윤은 자신이 한 일을 안전 조치 정도로 이해한다.

## First Choice

리아: "너, 방금 뭘 한 거야?"

### A. "저도 모르겠는데요. 무너질 것 같아서요."

- lia_affection +1
- mc_concealment +1
- flag_architecture_instinct_hidden = true
- meaning: 이도윤이 자기 능력을 축소하고 상황을 피하려 한다.
- route_note: 은폐/회피 성향. 초반 코미디와 오해 유지에 유리.

### B. "그 선이 받치는 게 아니라 비틀고 있었어요."

- lia_affection +2
- mc_exposure +1
- flag_architecture_talent_exposed = true
- meaning: 이도윤이 본 것을 그대로 말한다.
- route_note: 리아와의 연결이 가장 강해진다. 교수진/감시자 주목 가능.

### C. "제가 뭘 잘못 건드렸나요?"

- lia_affection 0
- mc_responsibility +1
- flag_mc_cautious = true
- meaning: 이도윤이 책임 문제를 먼저 걱정한다.
- route_note: 행정관/감시자 서브라인으로 연결하기 좋다.

## Undecided Routes

- 리아 루트 진입 조건 미정.
- 다른 히로인/조력자 루트 미정.
- 진엔딩 조건 미정.
