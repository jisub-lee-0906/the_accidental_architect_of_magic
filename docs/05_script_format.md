# 05 Script Format

## Purpose

이 문서는 Ren'Py로 옮기기 쉬운 씬 대본 작성 형식을 정의한다.

씬 본문은 줄글 소설이 아니라 배경, 음악, 효과음, 캐릭터 표시, 표정, 대사, 선택지를 분리한 대본 형태로 작성한다.

## Scene Header

```text
[SCENE_ID: prologue_001_public_demo_collapse]
[ROUTE: common]
[LOCATION: academy_demo_hall]
[TIME: afternoon]
```

## Direction Format

```text
[BG: bg_academy_demo_hall_afternoon]
[BGM: bgm_academic_wonder]
[SFX: sfx_magic_structure_hum]
```

## Character Show Format

문서용 지시문에서는 캐릭터와 표정/위치를 분리해 적는다. 표정 태그는 영어 snake_case만 사용하며, 한국어 감정명은 태그로 쓰지 않는다.

```text
[SHOW: lia_bel_astrin playful center]
[SHOW: lia_bel_astrin surprised center]
[HIDE: lia_bel_astrin]
```

Ren'Py 구현에서는 promoted image name을 그대로 사용한다.

```renpy
show lia_bel_astrin_playful at center
show lia_bel_astrin_surprised at center
hide lia_bel_astrin_playful
```

## Dialogue Format

```text
리아: "와. 방금 그거, 교수님들이 싫어할 방식이네. 마음에 들어."
주인공: "천재라서 한 게 아니라, 위험해서 한 겁니다."
```

운영 규칙:

- 플레이어에게 보이는 이름에는 표정/감정 태그를 붙이지 않는다. 예: `리아(장난)` 금지, `리아` 사용.
- 표정은 `[SHOW: ...]` 또는 Ren'Py `show lia_bel_astrin_<expression>`로만 관리한다.
- 표정 asset_id와 코드 태그는 영어 snake_case만 사용하고, 문서 설명은 한국어를 사용한다.
- canonical expression tags: `base`, `playful`, `curious`, `surprised`, `serious`, `forced_smile`, `anxious`.
- expression tag 의미: `base`=기본, `playful`=장난/가벼움, `curious`=흥미/호기심, `surprised`=놀람, `serious`=진지, `forced_smile`=억지 미소/불안 은폐, `anxious`=불안.
- 새 감정이 필요하지만 exact asset이 없으면 먼저 가장 가까운 canonical expression tag로 대체하고, 반복적으로 필요할 때만 char_expression로 새 에셋을 생성한다.

## Choice Format

```text
[CHOICE]
A. "저도 모르겠는데요. 무너질 것 같아서요."
   - lia_affection +1
   - mc_concealment +1
   - flag_architecture_instinct_hidden = true

B. "그 선이 받치는 게 아니라 비틀고 있었어요."
   - lia_affection +2
   - mc_exposure +1
   - flag_architecture_talent_exposed = true

C. "제가 뭘 잘못 건드렸나요?"
   - lia_affection 0
   - mc_responsibility +1
   - flag_mc_cautious = true
```

## Ren'Py Conversion Example

```renpy
label prologue_001_public_demo_collapse:
    scene bg_academy_demo_hall_afternoon
    play music "audio/bgm/bgm_academic_wonder.ogg"
    play sound "audio/sfx/sfx_magic_structure_hum.ogg"

    show lia_bel_astrin_playful at center

    lia "와. 방금 그거, 교수님들이 싫어할 방식이네. 마음에 들어."
    mc "천재라서 한 게 아니라, 위험해서 한 겁니다."

    menu:
        "저도 모르겠는데요. 무너질 것 같아서요.":
            $ lia_affection += 1
            $ mc_concealment += 1
            $ flag_architecture_instinct_hidden = True

        "그 선이 받치는 게 아니라 비틀고 있었어요.":
            $ lia_affection += 2
            $ mc_exposure += 1
            $ flag_architecture_talent_exposed = True

        "제가 뭘 잘못 건드렸나요?":
            $ mc_responsibility += 1
            $ flag_mc_cautious = True
```

## Naming Rules

- scene_id: snake_case
- label: snake_case
- variable: snake_case
- asset_id: snake_case
- character_id: snake_case
- route_id: snake_case

## Current Naming Candidates

Protagonist note: character_id is `lee_do_yoon`; Ren'Py speaker id remains `mc` for implementation convenience.

- prologue_001_public_demo_collapse
- academy_demo_hall
- bg_academy_demo_hall_afternoon
- cg_unstable_magic_structure_demo
- lee_do_yoon
- mc
- lia_bel_astrin
- lia_affection
- mc_concealment
- mc_exposure
- mc_responsibility
- flag_architecture_instinct_hidden
- flag_architecture_talent_exposed
- flag_mc_cautious
