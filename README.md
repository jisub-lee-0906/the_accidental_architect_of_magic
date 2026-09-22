# The Accidental Architect of Magic

Ren'Py 판타지 비주얼 노벨의 프로덕션 프롤로그 시드입니다. 현실의 구조 설계자 도윤이 마법 구조물 붕괴를 멈춘 뒤, 리아 아스트린과 함께 능력의 정체를 조사하는 공통 루트를 구현합니다.

## 구조

- `game/script.rpy`: 프롤로그의 실행 가능한 공통 루트
- `game/generated_assets.rpy`: 승격된 이미지 자산의 Ren'Py 이름 매핑
- `game/images/generated/`: 현재 스크립트가 사용하는 승격 이미지
- `docs/`: 세계관, 캐릭터, 변수, 포맷, 자산과 장면 원문
- `CURRENT_VN_PRODUCTION_BASELINE.md`: 현 프로덕션 기준선과 검토 상태
- `VN_PROFILE_ORCHESTRATION_CONTRACT.md`: 역할 및 운영 계약 기록

## 실행

1. Ren'Py Launcher에서 이 저장소 루트를 프로젝트로 추가합니다.
2. `Launch Project`를 선택합니다.

CLI 실행은 설치한 Ren'Py SDK의 프로젝트 실행 방식에 따릅니다. SDK는 저장소에 포함되어 있지 않습니다.

## 현재 범위와 한계

- 플레이 가능한 범위는 `start`에서 시작하는 프롤로그 공통 스파인과 작업실 도착까지입니다.
- 장면 원문은 `docs/scenes/`가 기준이며, `game/script.rpy`는 그 원문을 통합한 실행본입니다.
- 일부 오디오 큐는 명시적 TODO로 남아 있으며 오디오 자산은 아직 통합되지 않았습니다.
- 생성 이미지와 기존 검토 기록은 보존 대상입니다. 이 저장소는 출시 또는 public-ready 상태를 주장하지 않습니다.
- 이 환경에서는 Ren'Py SDK를 찾지 못해 런타임 플레이테스트는 수행하지 못했습니다.
