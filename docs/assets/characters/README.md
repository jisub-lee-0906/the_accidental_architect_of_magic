# Character asset metadata

이 폴더는 캐릭터 기반 에셋 생성을 위한 source-of-truth sidecar를 둔다.

역할 분리:

- `docs/02_character_db.md`: 캐릭터 성격, 말투, 관계, 서사 canon.
- `docs/assets/characters/*.asset.json`: ComfyUI/Ren'Py 에셋 생성을 위한 기계 판독용 캐릭터 메타데이터.
- workflow README: 각 workflow가 metadata의 어떤 subset을 써야 하는지 설명하는 운영 규칙.
- prompt builder script: metadata와 workflow 규칙을 조립해 실제 prompt를 만든다.

운영 규칙:

1. 기존 캐릭터 기반 에셋 생성 전에는 해당 캐릭터의 `.asset.json`을 먼저 읽는다.
2. `identity_anchor.positive`는 캐릭터 동일성의 최소 블록이다. 임의로 삭제하지 않는다.
3. 의상 유지 작업은 `outfits.<outfit_id>.positive`를 고정한다.
4. 표정 작업은 `expression_map.<expression_id>.prompt_tags`만 바꾸고, body/background/camera tag를 섞지 않는다.
5. `scene_event_cg`는 no-ref route이므로 `identity_anchor + outfit_anchor + scene_event_cg framing/staging defaults`를 고정하고, expression/small staging override/background/time/seed만 바꾼다.
6. prompt tag는 루트 workflow pack의 `danbooru_tag.csv`에 존재하는 tag/alias 또는 workflow README가 허용한 wrapper token만 사용한다.
7. QA 전에는 생성 에셋을 production-ready/final이라고 부르지 않는다.

기본 사용 예:

```bash
python /home/jisub-lee/workspace/comfyui-game-asset-workflows/scripts/build_character_prompt.py   --character docs/assets/characters/lia_bel_astrin.asset.json   --workflow scene_event_cg   --outfit academy_uniform_blue_gold   --expression serious   --scene-tags auditorium stage indoors podium spotlight curtains presentation projector window sunlight
```

장소 연속성 주의:

- prologue `magic_demo_hall_03` / 제3마법시연장용 event CG에서는 `classroom`, `chalkboard`, `blackboard`를 proxy로 쓰지 않는다.
- 정확한 canon 장소를 한 단어 tag로 표현할 수 없으면 CSV에 있는 시연장/무대 계열 tag(`auditorium`, `stage`, `podium`, `spotlight`, `curtains`, `presentation`, `projector`, `indoors`)와 별도 background/overlay/Ren'Py staging으로 해결한다.
