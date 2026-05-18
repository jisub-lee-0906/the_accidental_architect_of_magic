# The Accidental Architect of Magic - placeholder playable slice
# Generated from docs canon scenes. Docs are source of truth; do not edit canon text here first.

# Promoted visual assets are defined in game/generated_assets.rpy.
# Remaining placeholder-only images stay there until generated/approved.

define mc = Character("도윤", color="#c8d8ff")
define lia = Character("리아", color="#ffc8f0")
define lia_playful = Character("리아", color="#ffc8f0")
define lia_curious = Character("리아", color="#ffc8f0")
define lia_surprised = Character("리아", color="#ffc8f0")
define lia_serious = Character("리아", color="#ffc8f0")
define lia_forced_smile = Character("리아", color="#ffc8f0")
define lia_low = Character("리아", color="#ffc8f0")
define professor = Character("교수", color="#dddddd")
define student_a = Character("학생 A", color="#c8ffc8")
define student_b = Character("학생 B", color="#c8ffc8")

default lia_affection = 0
default mc_concealment = 0
default mc_exposure = 0
default mc_responsibility = 0
default flag_architecture_instinct_hidden = False
default flag_architecture_talent_exposed = False
default flag_mc_cautious = False

label start:
    call prologue_001_public_demo_collapse
    return

label prologue_001_public_demo_collapse:
    # [SCENE_ID: prologue_001_public_demo_collapse]
    # [ROUTE: common]
    # [LOCATION: academy_demo_hall]
    # [CANON_LOCATION: magic_demo_hall_03 / 에스텔라 왕립마법학원 제3마법시연장]
    # [TIME: afternoon]
    scene bg_academy_demo_hall_afternoon
    # TODO audio asset pending: [BGM: bgm_academic_wonder]
    # TODO audio asset pending: [SFX: sfx_crowd_murmur_soft]
    "높은 천장 아래, 반투명한 마법진들이 허공에 층층이 떠 있었다."
    "누군가에게는 에스텔라 왕립마법학원의 내부 연구 발표회였고, 누군가에게는 후원자를 설득하기 위한 제3마법시연장이었다."
    "그리고 이도윤에게는—"
    mc "……여긴 또 어디야."
    "방금 전까지 분명 형광등이 깜빡이는 사무실에 있었다."
    "책상 위에는 밀린 구조 검토표가 쌓여 있었고, 모니터에는 빨간색으로 표시된 수정 요청이 떠 있었다."
    "그런데 지금 눈앞에는 돌기둥, 로브를 입은 학생들, 공중에 떠 있는 거대한 빛의 구조물이 있었다."
    # TODO audio asset pending: [SFX: sfx_magic_structure_hum]
    "공중의 구조물은 아름다웠다."
    "빛으로 만든 다리 같기도 했고, 뒤집힌 돔 같기도 했다."
    "하지만 도윤은 그 아름다움보다 먼저, 어긋난 선 하나를 보았다."
    mc "……저거, 왜 저렇게 받치고 있지?"
    show lia_bel_astrin_playful at right
    lia_playful "자, 박수는 나중에 쳐도 돼. 일단 안 무너지는지부터 보자고."
    "단상 위의 소녀가 웃으며 손가락을 튕겼다."
    "그 순간, 허공의 구조물이 한 층 더 밝게 빛났다."
    "관객석에서 낮은 감탄이 흘러나왔다."
    student_a "저게 리아 벨 아스트린의 신규 설계식……."
    student_b "교수님들이 금지할 뻔했다던 그거?"
    lia_playful "정확히는 아직 금지 안 됐어. 그래서 지금 하는 거지."
    # TODO audio asset pending: [SFX: sfx_magic_pulse_light]
    "가벼운 웃음이 시연장에 번졌다."
    "리아도 웃고 있었다."
    "하지만 도윤은 그 웃음보다, 구조물 중심부에서 미세하게 어긋나는 빛의 선을 보고 있었다."
    mc "아니, 잠깐."
    "빛의 선 하나가 다른 선을 받치고 있는 것처럼 보였다."
    "하지만 실제로는 받치고 있는 게 아니었다."
    "비틀고 있었다."
    "그 비틀림은 아직 작았다."
    "작지만, 익숙했다."
    "현장 사진 속 희미한 균열처럼."
    "도면 위에서 몇 밀리미터 어긋난 기둥 중심선처럼."
    "누구도 문제 삼지 않았지만, 계속 보고 있으면 속이 불편해지는 종류의 오류처럼."
    # TODO audio asset pending: [SFX: sfx_magic_structure_hum_louder]
    lia_playful "좋아, 세 번째 층위 개방. 다들 눈 크게 떠. 이건 교과서에는 안 나오는 방식이니까."
    "리아가 다시 손을 들어 올렸다."
    scene cg_unstable_magic_structure_demo
    with dissolve
    "구조물 중심부의 빛이 한 번 크게 출렁였다."
    "관객석의 웅성거림이 멎었다."
    professor "리아 아스트린. 출력이 불안정하다. 즉시 중단해라."
    scene bg_academy_demo_hall_afternoon
    show lia_bel_astrin_forced_smile at right
    with dissolve
    lia_forced_smile "괜찮아요. 아직 허용 범위 안이에요."
    "리아는 여전히 웃고 있었다."
    "하지만 도윤은 보았다."
    "그 웃음이 아주 잠깐, 얇게 굳어지는 것을."
    # TODO audio asset pending: [SFX: sfx_magic_crack]
    student_a "방금 소리…… 들었어?"
    student_b "마력 균열이야?"
    professor "전원 뒤로 물러나라!"
    "구조물의 중심부가 접히기 시작했다."
    "무너지는 것이 아니라, 안쪽으로 말려 들어가고 있었다."
    "사람들은 마력 폭주라고 외쳤다."
    "술식 오류라고 했다."
    "시전자를 멈추라고 했다."
    "하지만 도윤에게는 다르게 보였다."
    mc "저건 받치고 있는 게 아니라……."
    "생각보다 몸이 먼저 움직였다."
    "도윤은 단상 아래로 뛰어들었다."
    "누군가 붙잡으려 했지만, 이미 늦었다."
    mc "비틀고 있잖아!"
    # TODO audio asset pending: [SFX: sfx_footstep_rush]
    # TODO audio asset pending: [SFX: sfx_magic_distortion]
    show lia_bel_astrin_surprised at right
    lia_surprised "어, 잠깐! 너 누구—"
    "도윤은 공중에 떠 있는 빛의 선을 향해 손을 뻗었다."
    "마법을 쓸 줄 아는 것은 아니었다."
    "주문도 몰랐다."
    "그저 눈앞의 구조가 너무 불안해서, 그대로 둘 수 없었다."
    mc "이 선이 여기 있으면 안 돼."
    "손끝이 빛에 닿았다."
    "순간, 머릿속에 보이지 않는 도면이 펼쳐졌다."
    "기둥."
    "보."
    "하중."
    "균열."
    "지지선."
    "그리고 그 모든 것을 억지로 붙들고 있던, 잘못 놓인 하나의 선."
    mc "옮긴다면…… 이쪽."
    # TODO audio asset pending: [SFX: sfx_magic_snap]
    # TODO audio asset pending: [SFX: sfx_magic_structure_stabilize]
    # TODO audio asset pending: [BGM: stop]
    "소리가 사라졌다."
    "무너지려던 구조물은 허공에서 멈췄다."
    "비틀리던 중심부가 천천히 펴지고, 빛의 선들이 새로운 균형을 찾았다."
    "누군가 숨을 삼켰다."
    "교수도, 학생들도, 후원자들도 아무 말도 하지 못했다."
    "리아 역시 그랬다."
    show lia_bel_astrin_surprised at right
    lia_surprised "……너."
    "리아의 얼굴에서 웃음이 사라져 있었다."
    "처음으로, 완전히."
    show lia_bel_astrin_serious at right
    lia_serious "방금 뭘 한 거야?"
    "도윤은 자신의 손끝을 내려다보았다."
    "방금 만진 빛은 아직도 희미하게 떨리고 있었다."
    mc "저도 그걸 좀 알고 싶은데요."
    show lia_bel_astrin_serious at right
    lia_serious "아니. 모르는 척하지 마."
    "리아가 한 걸음 다가왔다."
    "방금 전까지 장난처럼 시연장을 휘어잡던 목소리는 낮아져 있었다."
    lia_serious "너, 방금…… 내가 못 고친 걸 고쳤어."
    "도윤은 주변을 둘러보았다."
    "교수들은 굳은 얼굴로 자신을 보고 있었다."
    "학생들은 한 발씩 물러서 있었다."
    "리아만이 반대로 다가오고 있었다."
    show lia_bel_astrin_surprised at right
    lia_surprised "너, 방금 뭘 한 거야?"

    menu:
        "저도 모르겠는데요. 무너질 것 같아서요.":
            $ lia_affection += 1
            $ mc_concealment += 1
            $ flag_architecture_instinct_hidden = True
            call prologue_001a_instinct_hidden
            call prologue_002_corridor_escape
            call prologue_003_lia_workshop_inquiry
            return

        "그 선이 받치는 게 아니라 비틀고 있었어요.":
            $ lia_affection += 2
            $ mc_exposure += 1
            $ flag_architecture_talent_exposed = True
            call prologue_first_choice_b_placeholder
            return

        "제가 뭘 잘못 건드렸나요?":
            $ mc_responsibility += 1
            $ flag_mc_cautious = True
            call prologue_first_choice_c_placeholder
            return

label prologue_001a_instinct_hidden:
    # [SCENE_ID: prologue_001a_instinct_hidden]
    # [ROUTE: common]
    # [BRANCH: first_choice_a_concealment]
    # [LOCATION: academy_demo_hall]
    # [CANON_LOCATION: magic_demo_hall_03 / 에스텔라 왕립마법학원 제3마법시연장]
    # [TIME: afternoon]
    scene bg_academy_demo_hall_afternoon
    # TODO audio asset pending: [BGM: stop]
    # TODO audio asset pending: [SFX: sfx_crowd_murmur_soft]
    mc "저도 모르겠는데요. 무너질 것 같아서요."
    "말하고 나서, 도윤은 곧바로 후회했다."
    "너무 솔직했다."
    "아니, 솔직한 척하면서 아무것도 설명하지 않은 대답이었다."
    "현실에서라면 회의록에 남기기 가장 나쁜 종류의 문장."
    mc "그러니까, 정확히는…… 위험해 보여서요."
    show lia_bel_astrin_serious at right
    lia_serious "위험해 보였다."
    "리아는 그 말을 천천히 되풀이했다."
    "시연장은 여전히 조용했다."
    "교수들은 서로 눈빛을 주고받고 있었고, 학생들은 도윤과 리아 사이에 보이지 않는 선이라도 생긴 것처럼 물러서 있었다."
    lia_serious "내 설계식이?"
    mc "제가 그걸 설계식이라고 부르는 게 맞는지도 모르겠는데요."
    lia_serious "그럼 넌 뭘 봤는데?"
    "도윤은 공중에 멈춰 선 빛의 구조물을 바라보았다."
    "방금 자신이 옮긴 선은 다른 선들 사이에 조용히 섞여 있었다."
    "마치 처음부터 그 자리에 있었던 것처럼."
    mc "그냥…… 선이 이상했습니다."
    show lia_bel_astrin_surprised at right
    lia_surprised "선?"
    mc "받치는 것처럼 보였는데, 실제론 비틀고 있었어요. 그래서 무너질 것 같았고요."
    "도윤은 말을 멈췄다."
    "모른다고 해놓고, 너무 많이 설명했다."
    mc "아니, 그러니까 제 말은…… 그냥 감입니다. 감."
    show lia_bel_astrin_curious at right
    lia_curious "감."
    "리아의 눈이 다시 빛났다."
    "이번에는 시연장의 마법 구조물보다 훨씬 위험한 방식으로."
    lia_curious "마법을 모르는 사람이, 내 설계식의 결함을 감으로 보고, 손으로 고쳤다?"
    mc "그렇게 정리하시면 제가 많이 불리해지는데요."
    show lia_bel_astrin_playful at right
    lia_playful "좋아. 그럼 더 재밌네."
    "리아의 입가에 웃음이 돌아왔다."
    "하지만 이번 웃음은 아까와 달랐다."
    "시연장을 가볍게 휘어잡던 웃음이 아니라, 눈앞의 수수께끼를 절대 놓치지 않겠다는 연구자의 웃음이었다."
    professor "리아 아스트린. 그 인물에게서 물러나라."
    lia_playful "학생인지 아닌지도 아직 모르는데요?"
    professor "그래서 더 문제다. 신원 불명의 외부인이 왕립학원의 시연식에 개입했다."
    "그 말에 도윤은 뒤늦게 현실감을 되찾았다."
    "왕립학원."
    "신원 불명."
    "시연식 개입."
    "어느 단어 하나도 가볍지 않았다."
    mc "잠깐만요. 저는 일부러 들어온 게 아니라—"
    lia_playful "맞아. 일부러 들어온 게 아니지."
    "리아가 도윤의 말을 가로챘다."
    "그리고 아주 자연스럽게, 도윤의 소매를 붙잡았다."
    lia_playful "내가 데려온 거니까."
    mc "네?"
    professor "리아 아스트린."
    show lia_bel_astrin_forced_smile at right
    lia_forced_smile "시연 보조자예요. 비공식이지만."
    "도윤은 리아를 보았다."
    "리아는 웃고 있었다."
    "분명 웃고 있었지만, 손끝에는 힘이 들어가 있었다."
    "도윤을 놓치지 않겠다는 듯이."
    mc "저기요. 방금 처음 뵌 사이인데요."
    lia_low "그러니까 조용히 해. 지금 잡혀가면 너도 귀찮고, 나도 귀찮아."
    mc "이미 충분히 귀찮은 것 같은데요."
    show lia_bel_astrin_playful at right
    lia_playful "에스텔라에 온 걸 환영해. 원래 여긴 더 귀찮아."
    # TODO audio asset pending: [SFX: sfx_crowd_murmur_soft]
    "시연장 전체가 다시 웅성거리기 시작했다."
    "교수진은 도윤을 경계했고, 학생들은 리아가 또 사고를 쳤다는 표정이었다."
    "그리고 리아는 그 모든 시선을 무시한 채 도윤의 소매를 잡고 있었다."
    show lia_bel_astrin_curious at right
    lia_curious "자, 이도윤."
    mc "제 이름은 어떻게—"
    show lia_bel_astrin_playful at right
    lia_playful "몰라. 방금 네가 중얼거렸어."
    "도윤은 기억나지 않았다."
    "하지만 지금 중요한 건 그게 아니었다."
    "리아가 한 걸음 가까이 다가왔다."
    show lia_bel_astrin_curious at right
    lia_curious "네가 정말 아무것도 모른다면, 더 좋아."
    show lia_bel_astrin_serious at right
    lia_serious "선입견이 없다는 뜻이니까."
    "그 말은 장난처럼 들리지 않았다."
    "도윤은 다시 공중의 구조물을 올려다보았다."
    "조용히 안정된 빛의 선들 사이에서, 자신이 옮긴 한 줄이 희미하게 떨리고 있었다."
    "마치 아직 끝나지 않았다고 말하는 것처럼."
    mc "저, 혹시 집에 가는 방법부터 물어봐도 됩니까?"
    show lia_bel_astrin_playful at right
    lia_playful "물어보는 건 자유야."
    "리아가 환하게 웃었다."
    lia_playful "대답해준다는 말은 안 했지만."
    # [END_SCENE]
    return

label prologue_002_corridor_escape:
    # [SCENE_ID: prologue_002_corridor_escape]
    # [ROUTE: common]
    # [BRANCH: first_choice_a_concealment]
    # [LOCATION: estella_academy_corridor]
    # [CANON_LOCATION: 에스텔라 왕립마법학원 제3마법시연장 인근 복도]
    # [TIME: afternoon]
    scene bg_estella_academy_corridor_afternoon
    # TODO audio asset pending: [BGM: bgm_light_panic]
    # TODO audio asset pending: [SFX: sfx_crowd_murmur_fade]
    "리아는 도윤의 소매를 잡은 채 시연장 출구로 걸어갔다."
    "아니, 걸어갔다기보다는 끌고 갔다."
    mc "잠깐만요. 저 지금 어딜 가는 겁니까?"
    show lia_bel_astrin_playful at right
    lia_playful "복도."
    mc "그건 저도 압니다."
    lia_playful "그럼 질문 하나 아꼈네."
    "등 뒤에서 교수의 목소리가 날아왔다."
    professor "리아 아스트린! 멈춰라!"
    lia_playful "교수님, 시연장은 안정화됐고, 관객 대피도 끝났고, 저는 원인 분석하러 갑니다!"
    professor "그 원인 분석 대상이 네 옆에 있는 신원 불명 인물이다!"
    lia_playful "그러니까 제가 데려가는 거죠!"
    mc "저기요, 저는 분석 대상이 아닌데요."
    lia_low "지금은 맞아."
    mc "그걸 본인 앞에서 그렇게 말해도 됩니까?"
    lia_low "네가 도망치면 곤란하거든."
    # TODO audio asset pending: [SFX: sfx_door_open]
    scene bg_estella_academy_corridor_afternoon
    # TODO audio asset pending: [SFX: sfx_door_close]
    "두 사람이 시연장 밖으로 나오자, 웅성거리던 소리가 두꺼운 문 너머로 낮아졌다."
    "복도는 의외로 조용했다."
    "높은 창으로 오후 빛이 길게 들어오고, 벽면에는 에스텔라 왕립마법학원의 문장과 오래된 연구 성과들이 액자처럼 걸려 있었다."
    "도윤은 그제야 자신이 정말로 다른 세계에 와 있다는 사실을 실감했다."
    mc "……꿈은 아니겠죠?"
    show lia_bel_astrin_playful at right
    lia_playful "아까 손으로 마도구조식 만졌잖아. 보통 꿈이면 그쯤에서 깨."
    mc "현실이어도 그쯤에서 깨고 싶었습니다."
    show lia_bel_astrin_playful at right
    lia_playful "적응 빠르네. 좋아."
    mc "어느 부분이요?"
    lia_playful "불평하는 방식."
    "리아는 웃으며 복도를 빠르게 걸었다."
    "도윤은 따라갈 수밖에 없었다."
    "정확히는, 소매를 붙잡혀 있어서 선택권이 별로 없었다."
    mc "일단 이것부터 확인합시다. 저는 여기 학생도 아니고, 보조자도 아니고, 당신이 데려온 사람도 아닙니다."
    lia_playful "셋 중 하나는 곧 맞게 될 수도 있어."
    mc "싫은 예고네요."
    lia_playful "괜찮아. 에스텔라에서는 대부분 싫은 일이 먼저 와."
    "리아는 모퉁이를 돌기 직전, 갑자기 걸음을 멈췄다."
    "도윤은 거의 그녀의 등에 부딪힐 뻔했다."
    mc "왜 갑자기—"
    show lia_bel_astrin_serious at right
    lia_serious "방금 네가 말한 거."
    "리아의 목소리가 낮아졌다."
    "복도에 있던 장난기가 한순간 사라졌다."
    lia_serious "‘받치는 게 아니라 비틀고 있었다’는 말. 그거 아무한테나 하지 마."
    mc "왜요?"
    lia_serious "그걸 알아들으면 위험한 사람이고, 못 알아들으면 더 위험한 사람이거든."
    mc "둘 다 위험하면 저는 누구랑 얘기해야 합니까?"
    lia_serious "나."
    "리아는 조금의 망설임도 없이 대답했다."
    "그 대답이 너무 빨라서, 오히려 농담처럼 들리지 않았다."
    mc "방금까지 저를 분석 대상이라고 하신 분이요?"
    show lia_bel_astrin_playful at right
    lia_playful "분석 대상 겸 보호 대상?"
    mc "둘 다 싫습니다."
    lia_playful "그럼 공범."
    mc "더 싫습니다."
    "리아는 다시 웃었다."
    "하지만 손은 여전히 도윤의 소매를 놓지 않았다."
    show lia_bel_astrin_forced_smile at right
    lia_forced_smile "농담처럼 들리게 말했지만, 반쯤은 진심이야."
    mc "어느 반쪽이요?"
    lia_forced_smile "네가 본 걸 누가 먼저 해석하느냐에 따라, 넌 천재가 될 수도 있고, 범죄자가 될 수도 있어."
    "도윤은 말문이 막혔다."
    "방금 전까지는 이상한 학원에서 이상한 천재에게 붙잡힌 상황이라고 생각했다."
    "하지만 리아의 표정은 그보다 더 복잡한 것을 말하고 있었다."
    "이곳에는 규칙이 있고, 권력이 있고, 누군가가 정한 위험의 이름이 있었다."
    mc "저는 그냥 무너질 것 같아서 손댄 건데요."
    show lia_bel_astrin_serious at right
    lia_serious "알아."
    "리아는 짧게 대답했다."
    "그리고 아주 잠깐, 시선을 피했다."
    lia_serious "그래서 내가 널 먼저 데려가는 거야."
    mc "저를 보호하려고요?"
    show lia_bel_astrin_playful at right
    lia_playful "그렇게 말하면 너무 착해 보이잖아."
    mc "그럼 정확히는요?"
    show lia_bel_astrin_curious at right
    lia_curious "네가 뭘 봤는지, 내가 먼저 알아내려고."
    mc "역시 보호가 아니었군요."
    show lia_bel_astrin_playful at right
    lia_playful "겸사겸사 보호도 해줄게."
    mc "부가 서비스처럼 말하지 마세요."
    # TODO audio asset pending: [SFX: sfx_footsteps_corridor]
    "복도 끝에서 몇몇 학생들이 고개를 내밀었다."
    "그들은 리아와 도윤을 보자마자 수군거리기 시작했다."
    student_a "리아가 또 사람 끌고 가는데?"
    student_b "이번엔 살아 있는 사람이네."
    mc "이번엔?"
    lia_playful "전에 끌고 간 건 자동계단이었어."
    mc "자동계단은 사람이 아닙니다."
    lia_playful "그래서 살아 있지 않았지."
    mc "아니, 그런 뜻이 아니라……"
    "도윤은 말하다가 포기했다."
    "상대가 너무 자연스럽게 이상했다."
    "그리고 더 문제는, 이 이상한 사람이 지금 자신을 이 세계에서 유일하게 설명해줄 수 있을 것 같다는 점이었다."
    show lia_bel_astrin_curious at right
    lia_curious "자, 도윤. 마지막으로 하나만 확인하자."
    mc "대답하면 집에 보내줍니까?"
    show lia_bel_astrin_playful at right
    lia_playful "아니."
    mc "그럼 왜 대답해야 하죠?"
    show lia_bel_astrin_curious at right
    lia_curious "대답 안 하면 내가 멋대로 가설을 세울 거거든."
    mc "그건 더 위험해 보이네요."
    show lia_bel_astrin_serious at right
    lia_serious "맞아. 그러니까 대답해."
    "리아는 도윤의 소매를 놓았다."
    "처음으로."
    "하지만 도윤은 도망치지 못했다."
    "리아의 눈이 묻고 있었다."
    "도망칠 수 있으면 도망쳐 보라고."
    lia_serious "네가 그 선을 봤을 때, 그냥 눈으로 본 거야?"
    "도윤은 잠시 침묵했다."
    "공중에 펼쳐졌던 보이지 않는 도면."
    "기둥."
    "보."
    "하중."
    "균열."
    "지지선."
    "그 감각은 아직 손끝에 남아 있었다."
    mc "……눈으로만 본 건 아니었습니다."
    show lia_bel_astrin_serious at right
    lia_serious "그럼?"
    mc "머릿속에 도면처럼…… 떠올랐습니다."
    "리아의 표정이 굳었다."
    "이번에는 놀라서가 아니었다."
    "무언가를 확인한 사람의 얼굴이었다."
    lia_serious "좋아."
    mc "안 좋은 ‘좋아’ 같은데요."
    lia_serious "응."
    "리아는 다시 도윤의 소매를 잡았다."
    "이번에는 아까보다 조금 더 조심스럽게."
    lia_serious "작업실로 가자."
    mc "제가 싫다고 하면요?"
    show lia_bel_astrin_playful at right
    lia_playful "그러면 교수님들한테 넘겨야지."
    mc "작업실이 어디죠?"
    lia_playful "적응 정말 빠르다니까."
    # [END_SCENE]
    return

label prologue_003_lia_workshop_inquiry:
    # [SCENE_ID: prologue_003_lia_workshop_inquiry]
    # [ROUTE: common]
    # [BRANCH: first_choice_a_concealment]
    # [LOCATION: lia_workshop]
    # [CANON_LOCATION: 에스텔라 왕립마법학원 마도건축학부 리아의 작업실]
    # [TIME: afternoon]
    # TODO canon candidate: docs/scenes/prologue_003_lia_workshop_inquiry.md status is canon_candidate_for_vertical_slice.
    # Keep workshop layout, door shielding, and mini model details local to this scene until director confirmation.
    scene bg_lia_workshop_afternoon
    # TODO audio asset pending: [BGM: bgm_curious_investigation]
    # TODO audio asset pending: [SFX: sfx_door_unlock_magic]
    "리아는 도윤을 작업실 안으로 데려온다."
    "작업실은 정돈된 연구실이 아니라 사고 직전의 설계 현장처럼 보인다."
    "벽면에는 마도건축 도면, 실패한 설계식 메모, 붉은 수정 표시가 붙어 있었다."
    "책상 위에는 설계지, 마법석, 반쯤 식은 찻잔, 자와 필기구가 어지럽게 놓여 있었다."
    "바닥에는 말린 도면과 작은 구조 모형 부품이 굴러다녔다."
    mc "여기가 작업실입니까, 사고 수습 전 현장입니까?"
    show lia_bel_astrin_playful at right
    lia_playful "둘 다 비슷한 말이야."
    mc "그 말이 제 불안을 전혀 줄여주지 않는데요."

    "리아는 손가락으로 문 근처의 허공을 그었다."
    "문틀에 얇은 빛의 선이 생겼다가 사라졌다."
    "도윤은 문틀 위쪽이 미세하게 떨리는 것을 보았다."
    "아니, 보았다기보다는 불편하게 느꼈다."
    mc "문틀 위쪽이 좀 떨리는데요."
    show lia_bel_astrin_curious at right
    lia_curious "보여?"
    mc "보인다기보다는…… 불편합니다."
    lia_curious "좋아. 그 표현, 아주 마음에 들어."
    mc "저는 마음에 안 듭니다."

    show lia_bel_astrin_playful at right
    lia_playful "좋은 소식부터 말할까, 나쁜 소식부터 말할까?"
    mc "집에 가는 방법부터 말해주시면 안 됩니까?"
    show lia_bel_astrin_serious at right
    lia_serious "그건 지금 내가 제일 못 하는 대답이야."
    mc "그러면 좋은 소식이 없다는 뜻 같은데요."
    lia_serious "좋은 소식은, 네가 아직 교수님들 손에 안 넘어갔다는 거."
    mc "나쁜 소식은요?"
    show lia_bel_astrin_curious at right
    lia_curious "내 손에 넘어왔다는 거?"
    mc "분류가 이상합니다."

    "리아는 도윤을 앉히지 않고 바로 작은 확인을 준비했다."
    scene prop_lia_mini_structure_model
    with dissolve
    "책상 위의 투명 판 위로 작은 빛의 선들이 떠올랐다."
    scene bg_lia_workshop_afternoon
    show lia_bel_astrin_serious at right
    with dissolve
    lia_serious "이건 아까 시연식의 축소 모델이야. 훨씬 작고, 훨씬 덜 위험한 버전."
    mc "덜 위험하다는 말은 위험하다는 뜻이죠?"
    show lia_bel_astrin_playful at right
    lia_playful "이제 잘 알아듣네."
    mc "칭찬처럼 들리지 않습니다."
    show lia_bel_astrin_serious at right
    lia_serious "그럼 봐. 마법으로 보려고 하지 말고, 네 방식으로."
    mc "저는 원래 마법으로 볼 줄 모릅니다."
    show lia_bel_astrin_curious at right
    lia_curious "그러니까 좋은 거야."

    "도윤은 축소 모델의 작은 고리 하나가 전체보다 반 박자 늦게 따라오는 것을 짚었다."
    mc "저 작은 고리요. 전체가 같이 돌아야 안정적인 것 같은데, 저 부분만 반 박자 늦습니다."
    show lia_bel_astrin_surprised at right
    lia_surprised "……그걸 봤어?"
    mc "보였다기보다는, 거기만 계속 신경 쓰입니다."
    show lia_bel_astrin_serious at right
    lia_serious "그건 내가 아무에게도 말 안 한 부분이야."
    mc "그럼 저는 못 들은 걸로 하겠습니다."
    lia_serious "이미 봤잖아."

    lia_serious "마법으로는 못 찾았어. 그러니까 네 방식으로 설명해줘."
    mc "제가 설명할 수 있는 종류인지 모르겠습니다."
    lia_serious "그럼 설명할 수 있는 모양으로 바꿔."
    mc "종이 있습니까?"
    show lia_bel_astrin_curious at right
    lia_curious "종이?"
    mc "그림으로 설명하는 게 빠를 것 같습니다."
    lia_curious "좋아."
    mc "그리고 그 다음엔 집에 가는 방법을 알아봅니다."
    show lia_bel_astrin_forced_smile at right
    lia_forced_smile "응. 그 다음엔."
    mc "방금 대답이 매우 불안했습니다."
    show lia_bel_astrin_serious at right
    lia_serious "불안해도 지금은 여기 있는 게 제일 안전해."

    "도윤은 잠시 문 쪽을 본다."
    "교수진에게 넘겨지는 것, 신원 불명자로 붙잡히는 것, 아무것도 모른 채 혼자 나가는 것."
    "어느 쪽도 집으로 돌아가는 길처럼 보이지 않는다."
    "도윤은 펜을 잡는다."
    mc "좋습니다. 설명은 해보겠습니다. 대신 위험하면 멈춥니다."
    lia_serious "그 말, 마음에 들어."
    # [END_SCENE]
    return

label prologue_first_choice_b_placeholder:
    # TODO: Implement canon follow-up scene for first choice B after docs are confirmed.
    mc "그 선이 받치는 게 아니라 비틀고 있었어요."
    lia_serious "그 대답은, 그냥 넘기기 어렵겠네."
    "B 선택지 후속 씬은 아직 canon scene 문서가 없어 placeholder로 종료합니다."
    return

label prologue_first_choice_c_placeholder:
    # TODO: Implement canon follow-up scene for first choice C after docs are confirmed.
    mc "제가 뭘 잘못 건드렸나요?"
    show lia_bel_astrin_playful at right
    lia_playful "책임부터 걱정하는 타입이구나. 그것도 꽤 귀찮은데."
    "C 선택지 후속 씬은 아직 canon scene 문서가 없어 placeholder로 종료합니다."
    return
