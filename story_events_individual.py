from story_data import StoryEvent

# 개별 이벤트들
INDIVIDUAL_EVENTS = [
    # 최시은 개별 이벤트
    StoryEvent(
        id="choi_individual",
        chapter=5,
        background="club_room_evening",
        characters=["CHOI", "KANG"],
        dialogs=[
            "금요일 저녁 7시, F&B 동아리방",
            "강재호가 동아리방에서 혼자 과제를 하고 있을 때, 최시은이 들어온다.",
            "최시은: 아직도 여기 있네? 다들 집에 갔는데.",
            "강재호: 네, 포인터 과제가 너무 어려워서...",
            "최시은: (강재호 옆에 앉으며) 봐줄까? 포인터는 내 전문 분야야.",
            "최시은이 강재호 바로 옆에 앉아 모니터를 함께 본다. 어깨가 닿을 정도로 가깝다.",
            "최시은: 여기 봐. 포인터는 직접 참조하는 거야. 마치... 내가 너를 바라보는 것처럼.",
            "강재호: 저를 바라본다고요?",
            "최시은: (얼굴 빨개지며) 아, 아니! 그게 아니라... 포인터는 말이야, 중요한 데이터를 가리키잖아?",
            "강재호: 네...",
            "최시은: 너도... 내게는 중요한... 어? 이게 아니라!",
            "최시은이 당황해서 키보드를 잘못 눌러 화면에 하트 모양이 출력된다.",
            "강재호: 선배... 하트가 출력됐어요.",
            "최시은: (더 당황하며) 버그야! 이건 버그라고!"
        ],
        choices=[
            {"text": "같이 디버깅해볼까요?", "effect": {"CHOI": 10}, "next_event": "choi_polite"},
            {"text": "귀여운 버그네요. 고치지 말아요.", "effect": {"CHOI": 20}, "next_event": "choi_romantic"},
            {"text": "선배도 가끔 실수하시는구나.", "effect": {"CHOI": -5}, "next_event": "choi_tease"}
        ]
    ),
    
    StoryEvent(
        id="choi_romantic",
        chapter=5,
        background="club_room_evening",
        characters=["CHOI", "KANG"],
        dialogs=[
            "최시은: (얼굴 빨개지며) 미... 미안. 근데 이 버그...",
            "강재호: 고치지 말라고 했잖아요.",
            "최시은: 왜? 버그는 고쳐야 하는 거 아니야?",
            "강재호: 이 버그는... 선배 마음의 아름다운 컴파일 에러 같아요.",
            "최시은: (심장이 뛰며) 컴파일 에러가... 아름답다고?",
            "강재호: 네. 완벽한 코드보다 선배의 솔직한 마음이 더 좋아요.",
            "최시은: (속삭이며) 너... 정말 내 논리 회로를 단락시키는구나.",
            "강재호: 그럼... 저도 선배 때문에 무한루프에 빠진 것 같아요.",
            "최시은: (가까이 다가가며) while(true) { 재호_생각(); } 이런 거?",
            "강재호: 정확해요.",
            "그때 화면의 하트가 깜빡거린다.",
            "최시은: (웃으며) 이 버그... 의외로 귀엽네.",
            "둘이 서로를 바라보며 미소 짓는다."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "park_individual"}
        ]
    ),
    
    StoryEvent(
        id="choi_polite",
        chapter=5,
        background="club_room_evening",
        characters=["CHOI", "KANG"],
        dialogs=[
            "최시은: (약간 아쉬워하며) 너 참 예의바르구나.",
            "강재호: 그럼요. 선배니까요.",
            "최시은: 너무 딱딱하지 말고... 가끔은 편하게 해도 돼.",
            "강재호: 네, 알겠어요.",
            "최시은: 그럼... 계속 공부하자.",
            "강재호: 네, 선배. 포인터 개념 정말 잘 알려주세요.",
            "최시은: (약간 미소지으며) 그래? 그럼 더 열심히 가르쳐줄게.",
            "둘이 다시 코딩에 집중한다. 분위기가 조금 더 편안해졌다."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "park_individual"}
        ]
    ),
    
    StoryEvent(
        id="choi_tease",
        chapter=5,
        background="club_room_evening",
        characters=["CHOI", "KANG"],
        dialogs=[
            "최시은: (미간을 찌푸리며) 뭐? 나를 놀리는 거야?",
            "강재호: 아니에요! 그냥...",
            "최시은: 완벽주의자라고 싫어하는 사람들 많아서... 민감해.",
            "강재호: 죄송해요. 그런 뜻이 아니었어요.",
            "최시은: (한숨) 괜찮아. 그냥... 조심해서 말해줘.",
            "강재호: 네, 정말 죄송해요. 선배 기분 상하게 하려던 게 아니었어요.",
            "최시은: (조금 누그러지며) 알아. 너는 그런 애가 아니라는 거 알고 있어.",
            "강재호: 앞으로 더 신중하게 말할게요.",
            "최시은: (작은 미소) 그래, 고마워. 그럼 다시 공부하자."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "park_individual"}
        ]
    ),
    
    # 박이선 개별 이벤트
    StoryEvent(
        id="park_individual",
        chapter=5,
        background="park",
        characters=["PARK", "KANG"],
        dialogs=[
            "토요일 오후 2시, 유성대 근처 한빛공원",
            "박이선이 강재호에게 문자를 보낸다.",
            "'재호야~ 날씨 좋은데 공원에서 Python 자연어 처리 해볼래? 피크닉 도시락도 준비했어!'",
            "박이선: 와줘서 고마워! 도시락도 list comprehension으로 효율적으로 만들었어.",
            "강재호: list comprehension으로 도시락을요?",
            "박이선: (웃으며) 농담이야! 그런데 정말 Python처럼 간단하게 만들려고 노력했어.",
            "점심을 먹고 나무 그늘에서 쉬고 있다.",
            "박이선: 재호야, 여기 누워봐. 하늘 보면서 자연어 처리 생각해보자.",
            "둘이 나란히 풀밭에 누워 하늘을 본다. 박이선이 강재호 쪽으로 몸을 돌린다.",
            "박이선: 저기 구름들 봐. 마치 data = ['행복', '설렘', '따뜻함'] 같지 않아?",
            "강재호: (박이선을 바라보며) 정말 그런 것 같아요. 근데 선배가 더 아름다워요.",
            "박이선: (얼굴 빨개지며) 어? 갑자기 왜 그래? 내가 아름다운 데이터라는 거야?",
            "갑자기 소나기가 내리기 시작한다."
        ],
        choices=[
            {"text": "비도 자연의 일부니까 잠깐 감상해요", "effect": {"PARK": 15}, "next_event": "park_romantic2"},
            {"text": "빨리 피해요! (박이선 손 잡고 뛰기)", "effect": {"PARK": 20}, "next_event": "park_romantic"},
            {"text": "도시락 먼저 챙겨야죠!", "effect": {"PARK": -10}, "next_event": "park_practical"}
        ]
    ),
    
    StoryEvent(
        id="park_romantic",
        chapter=5,
        background="park",
        characters=["PARK", "KANG"],
        dialogs=[
            "박이선의 손을 잡고 정자로 뛰어간다.",
            "이 순간, 두 사람의 손이 맞닿았다. 따뜻한 온기가 전해진다.",
            "박이선: (숨을 헐떡이며) 와... 심장이 터질 것 같아!",
            "강재호: 괜찮아요?",
            "박이선: (강재호를 바라보며) 응... 너랑 손 잡고 뛰니까 심박수가 exponential하게 증가해.",
            "강재호: 저도... 선배 손잡기() 함수 실행했더니 return값이 '행복'이었어요.",
            "정자에서 비를 피하며 둘이 가까이 앉는다.",
            "박이선: (젖은 머리를 넘기며) 우리... 완전 wet_data 상태네.",
            "강재호: 선배... 괜찮아요? exception handling 필요하지 않아요?",
            "박이선: (강재호에게 더 가까이 붙으며) 추워... warmth.append(재호_체온) 해줘.",
            "얼굴이 가까워진다. 심장이 빠르게 뛴다.",
            "강재호: 그럼 제가 body_heat_sharing() 함수를 실행할게요.",
            "박이선: (안긴 채로) 이렇게 있으니까... temperature += 100 느낌이야.",
            "강재호: 선배는 정말 pandas처럼 다루기 쉽고 유용해요.",
            "박이선: (고개를 들어 강재호를 바라보며) 재호야... 너는 내 코드의 perfect_match()야.",
            "둘이 서로를 바라보며 미소 짓는다."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jang_individual"}
        ]
    ),
    
    StoryEvent(
        id="park_romantic2",
        chapter=5,
        background="park",
        characters=["PARK", "KANG"],
        dialogs=[
            "박이선: 에? 비 맞으면 감기 걸려!",
            "강재호: 가끔은 이런 것도 좋잖아요.",
            "박이선: (웃으며) 너 의외로 로맨틱하구나!",
            "비를 맞으며 웃는 둘.",
            "박이선: 이런 추억도 나쁘지 않네!",
            "강재호: 선배와 함께라서 더 특별한 것 같아요.",
            "박이선: (웃으며) 그래? 그럼 다음에도 이런 자연스러운 데이트 해볼까?",
            "강재호: 네! 정말 좋아요!",
            "비가 그치고 둘이 함께 집으로 돌아간다."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jang_individual"}
        ]
    ),
    
    StoryEvent(
        id="park_practical",
        chapter=5,
        background="park",
        characters=["PARK", "KANG"],
        dialogs=[
            "박이선: (어이없어하며) 지금 그게 중요해?!",
            "강재호: 아, 선배가 정성껏 만드신 거잖아요.",
            "박이선: 그래도... 사람이 먼저지. 좀 실망이야.",
            "강재호: 죄송해요...",
            "박이선: (한숨) 괜찮아. 그냥... 다음엔 우선순위를 생각해봐.",
            "강재호: 정말 죄송해요. 선배가 더 중요한데...",
            "박이선: (조금 누그러지며) 알겠어. 그래도 도시락 챙기는 마음은 이해해.",
            "강재호: 다음엔 선배를 먼저 생각할게요.",
            "박이선: (작은 미소) 그래, 그럼 됐어. 집에 가자."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jang_individual"}
        ]
    ),
    
    # 장바영 개별 이벤트
    StoryEvent(
        id="jang_individual",
        chapter=5,
        background="library_seminar",
        characters=["JANG", "KANG"],
        dialogs=[
            "일요일 오전 10시, 중앙도서관 개인 스터디룸",
            "장바영이 강재호에게 정중하게 제안한다.",
            "장바영: 재호님, 시간 되시면 함께 객체지향 스터디 하시는 건 어떨까요? 조용한 환경에서요.",
            "강재호: 좋아요! 바영 선배와 함께하면 코드 효율성도 올라갈 것 같아요.",
            "오후가 되어 강재호가 졸기 시작한다.",
            "강재호: (눈 비비며) 죄송해요... 좀 졸려요. sleep() 메소드가 호출된 것 같아요.",
            "장바영: 괜찮아요. 제 어깨를 temporary_pillow로 사용하세요.",
            "강재호가 장바영 어깨에 기댄다. 장바영이 강재호의 머리를 조심스럽게 쓰다듬는다.",
            "장바영: (속삭이며) 잠든 재호님... 마치 peaceful_state 객체 같네요.",
            "20분 후 강재호가 깨어나며 장바영이 자신의 노트에 뭔가 적고 있는 걸 본다."
        ],
        choices=[
            {"text": "죄송해요, 제가 sleep() 너무 오래 했나요?", "effect": {"JANG": 20}, "next_event": "jang_polite"},
            {"text": "선배, 뭐 쓰고 계세요?", "effect": {"JANG": 15}, "next_event": "jang_curious"},
            {"text": "조용히 일어나서 노트를 본다", "effect": {"JANG": -8}, "next_event": "jang_peek"}
        ]
    ),
    
    StoryEvent(
        id="jang_curious",
        chapter=5,
        background="library_seminar",
        characters=["JANG", "KANG"],
        dialogs=[
            "장바영: (얼굴 빨개지며) 아... 그냥... 재호님이 자고있는거...",
            "강재호: 그렇구나요.",
            "장바영: 재호님... 잘 주무시는 모습이 평화로워 보여서...",
            "강재호: 그런 걸 적으셨던 거예요?",
            "장바영: (수줍게) 네... 이상하죠?",
            "강재호: 아니에요. 오히려... 따뜻한 마음이 느껴져서 좋았어요.",
            "장바영: (얼굴 더 빨개지며) 정말... 그렇게 생각하세요?",
            "강재호: 네. 선배의 세심한 관찰력이 정말 대단해요.",
            "장바영: (미소지으며) 감사해요... 그럼 다음에도 이렇게 함께 공부할까요?",
            "강재호: 물론이죠! 바영 선배와 함께하는 시간이 정말 좋아요."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jason_individual"}
        ]
    ),
    
    StoryEvent(
        id="jang_polite",
        chapter=5,
        background="library_seminar",
        characters=["JANG", "KANG"],
        dialogs=[
            "장바영: (미소지으며) 20분 정도요. sleep() 메소드가 성공적으로 실행됐나요?",
            "강재호: 네, 덕분에 system refresh가 완료됐어요. 정말 고마워요.",
            "장바영: 천만에요. 가끔은 garbage collection도 필요하죠.",
            "강재호: 선배 덕분에 정말 메모리가 최적화된 느낌이에요.",
            "장바영: (부드럽게) 그럼... 다음에도 이렇게 pair programming 할까요?",
            "강재호: 네, 정말 좋아요. 그런데 선배...",
            "장바영: 네?",
            "강재호: 제가 sleep()할 때... private 메소드 실행하고 계셨죠?",
            "장바영: (얼굴 빨개지며) 그, 그냥... head_patting() 메소드를 호출했을 뿐이에요.",
            "조심스럽게 머리를 쓰다듬는다. 부드러운 손길이 느껴진다.",
            "강재호: 느꼈어요. 정말 comfortable_feeling을 return 했어요.",
            "장바영: (더 가까이 다가가며) 재호님... 정말 sleep_mode일 때 peaceful_object 같았어요.",
            "강재호: 선배와 함께 있으면 항상 stable_state예요.",
            "장바영: (손을 뻗어 강재호의 뺨을 살짝 만지며) 그럼... 언제든 제 support_method를 호출하세요."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jason_individual"}
        ]
    ),
    
    StoryEvent(
        id="jang_peek",
        chapter=5,
        background="library_seminar",
        characters=["JANG", "KANG"],
        dialogs=[
            "노트에는 '재호님 옆모습 - 속눈썹이 길다'라고 적혀있다.",
            "장바영: (깜짝 놀라며) 재, 재호님?!",
            "강재호: 죄송해요... 그런데 이게...",
            "장바영: (당황하여) 개인적인 건데... 왜 몰래 보세요?",
            "강재호: 정말 죄송해요.",
            "장바영: (차갑게) 다음부터는 허락받고 보세요.",
            "강재호: 정말 죄송해요... 앞으로 조심하겠습니다.",
            "장바영: (한숨을 쉬며) 괜찮아요. 그냥... 개인적인 일기 같은 거라서요.",
            "강재호: 네, 이해해요. 다시는 그런 일 없을 거예요.",
            "장바영: (조금 누그러지며) 그럼... 계속 공부하죠."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jason_individual"}
        ]
    ),
    
    # 제이슨 개별 이벤트
    StoryEvent(
        id="jason_individual",
        chapter=5,
        background="pc_cafe",
        characters=["JASON", "KANG"],
        dialogs=[
            "토요일 오후 3시, 캠퍼스 근처 PC방",
            "제이슨과 함께 PC방에 왔다.",
            "제이슨: 으으! 너무 아쉽다! 내가 이길수 있었는데!",
            "강재호: 하하 절 이기려면 아직 멀었네요",
            "제이슨: 다시해!",
            "치열한 코딩 게임 끝, 무승부! 둘 다 헥헥거리며 웃는다.",
            "제이슨: 와, 진짜 재밌었다! 너 정말 실력 좋은데?",
            "강재호: 제이슨도 정말 대단해요. 특히 알고리즘 최적화 부분은...",
            "제이슨이 흥미진진하게 강재호 쪽으로 몸을 기울이며 듣는다.",
            "제이슨: 어? 그 부분 어떻게 했어? 좀 더 자세히 알려줘!",
            "강재호가 화면을 가리키려는 순간, 제이슨도 동시에 같은 곳을 보려고 한다.",
            "둘의 손이 마우스 위에서 겹쳐진다.",
            "강재호: (깜짝 놀라며) 어... 죄송해요!",
            "제이슨: (얼굴 빨개지며) 아, 아니야! 내가 너무 급하게...",
            "강재호: (두근거리며) 괜찮아요, 제이슨 씨.",
            "제이슨: (작게 웃으며) 이런 것도 memory에 저장되는 거니까, 그치?",
            "옆 자리에서 다른 학생들이 수군댄다.",
            "'쟤네 DOM 조작하나 봐.' '쟤네  pair programming 하나?'"
        ],
        choices=[
            {"text": "addEventListener('타인시선', ignore)로 설정했어요.", "effect": {"JASON": 20}, "next_event": "jason_confident"},
            {"text": "다른 자리로 옮길길까요?", "effect": {"JASON": 10}, "next_event": "jason_move"},
            {"text": "저희 좀 떨어질까요?", "effect": {"JASON": -10}, "next_event": "jason_distance"}
        ]
    ),
    
    StoryEvent(
        id="jason_confident",
        chapter=5,
        background="pc_cafe",
        characters=["JASON", "KANG"],
        dialogs=[
            "강재호: addEventListener('타인시선', ignore)로 설정했어요.",
            "제이슨: (활짝 웃으며) 와, 역시 재호 event handling 완벽해! 내가 좋아하는 coding style!",
            "강재호: (당황) 좋...아하는 스타일?",
            "제이슨: (장난스럽게 눈 찡긋) 응. clean code랑 efficient function 쓰는 거!",
            "제이슨이 강재호에게 더 가까이 다가간다.",
            "제이슨: (속삭이며) 재호... 너 정말 unique_function이야.",
            "강재호: 제이슨도... special_variable이에요.",
            "제이슨: (강재호의 손을 잡으며) 그럼... 우리 relationship을 upgrade하는 건 어때?",
            "강재호: (심장이 뛰며) 그게... 어떤 version이에요?",
            "제이슨: (윙크하며) 알면서~ 더 interactive한 거지!",
            "제이슨이 강재호의 손에 작은 하트를 그린다.",
            "강재호: (얼굴 빨개지며) 제이슨!",
            "제이슨: (활짝 웃으며) 히히, 놀랐지? 이게 내 마음의 visual effect야!"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "conflict_event"}
        ]
        ),
      
    StoryEvent(
        id="jason_move",
        chapter=5,
        background="pc_cafe",
        characters=["JASON", "KANG"],
        dialogs=[
            "강재호: 다른 자리로 옮길까요?",
            "제이슨: 왜? 여기 딱 좋은데?",
            "강재호: 그냥... 시끄러운 것 같아서요.",
            "제이슨: (고개 끄덕이며) 그래~ 조용한 곳이 더 집중 잘 되긴 하지!",
            "살짝 거리감이 있지만 감정선은 유지된다.",
            "조용한 자리로 옮긴 후, 둘이 다시 코딩에 집중한다.",
            "제이슨: 여기가 훨씬 좋네! 집중도 잘 되고!",
            "강재호: 네, 제이슨 덕분에 좋은 자리 찾았어요.",
            "제이슨: (웃으며) 그럼 계속 코딩 배틀 해볼까?"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "conflict_event"}
        ]
    ),
    
    StoryEvent(
        id="jason_distance",
        chapter=5,
        background="pc_cafe",
        characters=["JASON", "KANG"],
        dialogs=[
            "강재호: 좀 떨어져 앉을까요?",
            "제이슨: (표정 굳어지며) 어...? 나... 너무 다가간 건가?",
            "강재호: 그런 건 아닌데, 그냥... 사람들이 너무 쳐다봐서...",
            "제이슨: (작게 한숨) 그냥 재밌게 놀고 싶었는데, 미안.",
            "분위기가 냉각된다.",
            "강재호: 아니에요, 제이슨. 제가 너무 의식한 것 같아요.",
            "제이슨: (고개를 들며) 정말?",
            "강재호: 네. 사실 제이슨과 함께 있는 시간이 정말 즐거워요.",
            "제이슨: (조금 밝아지며) 그래? 그럼... 다음에도 같이 놀자!",
            "강재호: 네, 꼭요!"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "conflict_event"}
        ]
    )
]

# 추가 호감도 이벤트들 - 갈등 해결 후
ADDITIONAL_ROMANCE_EVENTS = [
    # 최시은 추가 이벤트 - 야근 중 C언어 플러팅
    StoryEvent(
        id="choi_extra_romance",
        chapter=7,
        background="club_room_late_night",
        characters=["CHOI", "KANG"],
        dialogs=[
            "밤 12시, 동아리방에 최시은과 강재호만 남아있다.",
            "큰 프로젝트의 메모리 누수 버그를 찾고 있다.",
            "최시은: (화면을 보며) 이상해... 메모리가 계속 증가하고 있어.",
            "강재호: 어디선가 free()를 안 했나요?",
            "최시은: (강재호를 바라보며) 너 정말 포인터같은 친구야.",
            "강재호: 포인터요?",
            "최시은: 응. 직접적으로 내 마음 속 주소를 가리키고 있어.",
            "갑자기 정전이 된다. 비상등만 켜진 어둠 속.",
            "강재호: 어? 정전이네요.",
            "최시은: (당황하며) 앗! 세이브 안 했는데!",
            "강재호: 괜찮아요. 자동저장 켜놨잖아요.",
            "최시은: (안도하며) 다행이다... 근데 너 없으면 내 프로그램이 segmentation fault 날 것 같아.",
            "강재호: 선배... 그건 너무 위험한 에러 아닌가요?",
            "최시은: (가까이 다가가며) 그러니까... 너는 내 코드에서 꼭 필요한 변수야. malloc으로 동적할당해서 절대 해제하면 안 되는.",
            "강재호: 선배... 그런 식으로 말하면 제가 메모리 누수 일으킬 뻔했어요.",
            "최시은: (웃으며) 너라면... 메모리 누수도 기꺼이 감수할게."
        ],
        choices=[
            {"text": "그럼 저는 선배의 안전한 참조가 되겠습니다", "effect": {"CHOI": 20}, "next_event": "choi_romantic_response2"},
            {"text": "저도 선배를 dangling pointer로 만들고 싶지 않아요", "effect": {"CHOI": 25}, "next_event": "choi_romantic_response1"},
            {"text": "전기 들어오면 계속 디버깅해요", "effect": {"CHOI": 5}, "next_event": "choi_practical_response"}
        ]
    ),
    
    # 최시은 선택지 반응들
    StoryEvent(
        id="choi_romantic_response1",
        chapter=7,
        background="club_room_late_night",
        characters=["CHOI", "KANG"],
        dialogs=[
            "최시은: (감동하며) dangling pointer... 그래, 너는 정말 내 마음을 이해하는구나.",
            "강재호: 선배의 마음이 허공을 가리키게 하고 싶지 않아요.",
            "최시은: (가까이 다가가며) 그럼... 우리 서로의 안전한 참조가 되어줄래?",
            "강재호: 네, 영원히 유효한 포인터가 되겠습니다.",
            "최시은: (웃으며) 너 정말... 내 심장을 overflow 시키는구나.",
            "그때 전기가 다시 들어온다.",
            "최시은: 전기는 들어왔지만... 내 마음의 전원은 이미 너에게 연결되어 있어.",
            "강재호: 저도... 선배 없으면 시스템이 다운될 것 같아요.",
            "둘이 서로를 바라보며 미소 짓는다."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "park_extra_romance"}
        ]
    ),
    
    StoryEvent(
        id="choi_romantic_response2",
        chapter=7,
        background="club_room_late_night",
        characters=["CHOI", "KANG"],
        dialogs=[
            "최시은: (따뜻하게 웃으며) 안전한 참조... 그거 좋네.",
            "강재호: 선배가 언제든 접근할 수 있는 안정적인 메모리가 되고 싶어요.",
            "최시은: 그럼 나도... 너의 신뢰할 수 있는 라이브러리가 되어줄게.",
            "강재호: 정말요?",
            "최시은: (고개 끄덕이며) 응. 너에게는 모든 함수를 public으로 열어줄게.",
            "전기가 다시 들어오자 화면이 밝아진다.",
            "최시은: 이제 화면도 밝아졌으니... 우리 관계도 더 명확해진 것 같아.",
            "강재호: 네, 이제 컴파일 에러 없이 잘 돌아갈 것 같아요.",
            "최시은: (장난스럽게) 그럼 우리 코드 리뷰도 같이 해볼까?"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "park_extra_romance"}
        ]
    ),
    
    StoryEvent(
        id="choi_practical_response",
        chapter=7,
        background="club_room_late_night",
        characters=["CHOI", "KANG"],
        dialogs=[
            "최시은: (약간 아쉬워하며) 아... 그래, 일단 디버깅이 우선이지.",
            "강재호: 죄송해요. 너무 실용적으로 생각했나요?",
            "최시은: (한숨) 아니야. 너답긴 해. 항상 효율성을 생각하는 게.",
            "강재호: 하지만 선배와의 시간이 더 중요해요.",
            "최시은: (조금 밝아지며) 정말?",
            "강재호: 네. 디버깅은 언제든 할 수 있지만, 이런 순간은 다시 오지 않을 것 같아요.",
            "전기가 다시 들어온다.",
            "최시은: (미소지으며) 그래... 그럼 디버깅은 나중에 하고, 지금은 우리 시간을 가져볼까?",
            "강재호: 좋아요!"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "park_extra_romance"}
        ]
    ),
    
    # 박이선 추가 이벤트 - Python으로 요리 레시피 코딩
    StoryEvent(
        id="park_extra_romance",
        chapter=7,
        background="park_home",
        characters=["PARK", "KANG"],
        dialogs=[
            "박이선이 강재호를 자신의 원룸으로 초대했다.",
            "박이선: 오늘은 특별한 걸 보여줄게! 요리도 코딩처럼 할 수 있어!",
            "강재호: 요리를 코딩으로요?",
            "박이선: (노트북을 켜며) 봐봐! 파이썬으로 요리 레시피 짰어!",
            "[CODE_IMAGE:cooking_recipe.png]",
            "강재호: (웃으며) 선배... 'ingredients'에 '마음'이 들어가 있는데요?",
            "박이선: (얼굴 빨개지며) 어? 그, 그게 들켰네... 은밀한 재료였는데!",
            "함께 요리하며 대화한다.",
            "박이선: 자, 이제 import love를 해볼까?",
            "강재호: import love요?",
            "박이선: (가까이 다가가며) 응. 근데 이 모듈은... 너랑 함께 있을 때만 정상 작동해.",
            "강재호: 그럼 제가 없으면 ImportError가 나는 건가요?",
            "박이선: (윙크하며) 정확해! 너는 내 코드의 핵심 dependency야.",
            "식사 후 소파에서 함께 코딩한다.",
            "박이선: (어깨에 기대며) 이렇게 pair programming 하니까... while True: 행복해 상태네."
        ],
        choices=[
            {"text": "저도 선배와 함께하면 exception handling 필요 없어요", "effect": {"PARK": 25}, "next_event": "park_romantic_response1"},
            {"text": "그럼 우리 relationship을 git commit 할까요?", "effect": {"PARK": 20}, "next_event": "park_romantic_response2"},
            {"text": "코드 리뷰 먼저 해볼까요?", "effect": {"PARK": 5}, "next_event": "park_practical_response"}
        ]
    ),
    
    # 박이선 선택지 반응들
    StoryEvent(
        id="park_romantic_response1",
        chapter=7,
        background="park_home",
        characters=["PARK", "KANG"],
        dialogs=[
            "박이선: (눈을 반짝이며) 정말? exception handling이 필요 없다고?",
            "강재호: 네. 선배와 함께 있으면 모든 게 자연스럽게 처리돼요.",
            "박이선: (가까이 다가가며) 그럼... 우리 사이에는 try-catch 블록이 필요 없겠네?",
            "강재호: 네, 선배와는 항상 smooth execution이에요.",
            "박이선: (웃으며) 너 정말... 내 코드를 최적화시켜주는구나.",
            "강재호: 선배도 제 프로그램을 더 효율적으로 만들어줘요.",
            "박이선: (어깨에 더 기대며) 그럼 우리... 영원히 버그 없는 관계 유지할까?",
            "강재호: 물론이죠. 선배와 함께라면 무한루프도 행복할 것 같아요.",
            "박이선: (키스하듯 가까워지며) while(True): 사랑해();",
            "강재호: return 행복;"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jang_extra_romance"}
        ]
    ),
    
    StoryEvent(
        id="park_romantic_response2",
        chapter=7,
        background="park_home",
        characters=["PARK", "KANG"],
        dialogs=[
            "박이선: (깜짝 놀라며) git commit? 우리 관계를?",
            "강재호: 네! 이 소중한 순간을 영구히 저장하고 싶어요.",
            "박이선: (감동하며) 그럼... commit message는 뭘로 할까?",
            "강재호: 'feat: 박이선과의 완벽한 호환성 추가'는 어때요?",
            "박이선: (웃으며) 아니면 'fix: 외로움 버그 완전 해결'은?",
            "강재호: 둘 다 좋네요!",
            "박이선: (노트북을 열며) 그럼 진짜로 commit 해볼까?",
            "박이선이 실제로 git 명령어를 입력한다.",
            "박이선: git add 우리의_추억.py",
            "박이선: git commit -m 'feat: 재호와의 달콤한 시간 추가'",
            "강재호: (웃으며) 이제 우리 관계가 버전 관리되네요!",
            "박이선: (손을 잡으며) 그럼 다음은 git push origin 사랑 브랜치?"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jang_extra_romance"}
        ]
    ),
    
    StoryEvent(
        id="park_practical_response",
        chapter=7,
        background="park_home",
        characters=["PARK", "KANG"],
        dialogs=[
            "박이선: (약간 아쉬워하며) 아... 코드 리뷰를 먼저 하고 싶구나.",
            "강재호: 죄송해요. 습관적으로 그런 말이...",
            "박이선: (한숨) 괜찮아. 너 성격이 그렇긴 하지. 꼼꼼하고 체계적인 게.",
            "강재호: 하지만 지금은 선배와의 시간이 더 중요해요.",
            "박이선: (조금 밝아지며) 정말?",
            "강재호: 네. 코드는 언제든 리뷰할 수 있지만, 이런 달콤한 시간은 지금뿐이에요.",
            "박이선: (미소지으며) 그래... 그럼 코드 리뷰는 나중에 하고, 지금은 우리만의 시간을 가져볼까?",
            "강재호: 네! 그게 더 좋을 것 같아요.",
            "박이선: (장난스럽게) 그럼 지금부터는 코드 말고 내 마음을 리뷰해줘!"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jang_extra_romance"}
        ]
    ),
    
    # 장바영 추가 이벤트 - Java 객체지향 별밤 데이트
    StoryEvent(
        id="jang_extra_romance",
        chapter=7,
        background="observatory",
        characters=["JANG", "KANG"],
        dialogs=[
            "장바영이 강재호를 대학 천체관측대로 데려왔다.",
            "장바영: 여기서 객체지향 개념을 설명해드리고 싶었어요.",
            "강재호: 별보며 공부하는 건가요?",
            "장바영: (노트북을 꺼내며) 네. 별들도 하나의 객체라고 생각해보세요.",
            "[CODE_IMAGE:star_class.png]",
            "강재호: 이 코드... 저를 위한 건가요?",
            "장바영: (얼굴 빨개지며) 객체지향 예제입니다... 다만 private 변수가 조금 특별할 뿐이에요.",
            "강재호: private 변수요?",
            "장바영: (조심스럽게) 네. 제 마음 같은 것들이요... 보통은 외부에서 접근할 수 없지만...",
            "강재호: 하지만요?",
            "장바영: 재호님께는... getter 메소드를 허용할 수 있을 것 같아요.",
            "찬바람이 불자 장바영이 강재호에게 가까이 다가간다.",
            "장바영: 음... 이렇게 가까이 있으니까 encapsulation이 깨지는 것 같아요.",
            "강재호: 캡슐화가 깨진다고요?",
            "장바영: (웃으며) 네. 제 private 감정들이 public으로 노출되고 있어요.",
            "강재호: 그럼... 제가 예외처리를 해드릴게요.",
            "장바영: (고개를 들어) try-catch로 제 마음을 안전하게 다뤄주실 건가요?"
        ],
        choices=[
            {"text": "우리 relationship을 상속받아 확장해볼까요?", "effect": {"JANG": 22}, "next_event": "jang_romantic_response2"},
            {"text": "네, 선배 마음에 NullPointerException은 없을 거예요", "effect": {"JANG": 25}, "next_event": "jang_romantic_response1"},
            {"text": "코드 컴파일 먼저 확인해보죠", "effect": {"JANG": 10}, "next_event": "jang_practical_response"}
        ]
    ),
    
    # 장바영 선택지 반응들
    StoryEvent(
        id="jang_romantic_response1",
        chapter=7,
        background="observatory",
        characters=["JANG", "KANG"],
        dialogs=[
            "장바영: (감동하며) NullPointerException이 없다고... 정말 안전하게 다뤄주시겠다는 거죠?",
            "강재호: 네. 선배의 마음을 null로 만들 일은 절대 없을 거예요.",
            "장바영: (눈물이 글썽이며) 재호님... 그동안 제가 얼마나 조심스러웠는지 아세요?",
            "강재호: 왜요?",
            "장바영: 마음을 열었다가 상처받을까봐... 항상 private으로 숨겨두었거든요.",
            "강재호: 이제는 걱정하지 마세요. 제가 선배의 마음을 안전하게 지켜드릴게요.",
            "장바영: (가까이 다가가며) 그럼... 저도 재호님께 모든 권한을 드릴게요.",
            "강재호: 정말요?",
            "장바영: (고개 끄덕이며) public access modifier로 모든 걸 열어드릴게요.",
            "별빛 아래에서 둘이 손을 잡는다.",
            "장바영: 이제... 우리 사이에는 접근 제한자가 없어요."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jason_extra_romance"}
        ]
    ),
    
    StoryEvent(
        id="jang_romantic_response2",
        chapter=7,
        background="observatory",
        characters=["JANG", "KANG"],
        dialogs=[
            "장바영: (놀라며) relationship을 상속받아서... 확장하자고요?",
            "강재호: 네! 기존의 좋은 관계를 바탕으로 더 발전시켜보는 거예요.",
            "장바영: (생각하며) 그럼... class 우리의관계 extends 친구관계 {...}",
            "강재호: 맞아요! 그리고 새로운 메소드들을 추가하는 거죠.",
            "장바영: (웃으며) 어떤 메소드들을요?",
            "강재호: 손잡기(), 포옹하기(), 함께웃기()... 이런 것들요.",
            "장바영: (얼굴 빨개지며) 그럼... 키스하기() 메소드도 있나요?",
            "강재호: (당황하며) 그, 그건... 나중에 구현해볼까요?",
            "장바영: (장난스럽게) 그럼 지금은 베타 버전이네요?",
            "강재호: 네, 계속 업데이트하면서 완성해나가요!",
            "장바영: (손을 잡으며) 좋아요. 우리만의 특별한 클래스를 만들어봐요."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jason_extra_romance"}
        ]
    ),
    
    StoryEvent(
        id="jang_practical_response",
        chapter=7,
        background="observatory",
        characters=["JANG", "KANG"],
        dialogs=[
            "장바영: (약간 실망하며) 아... 컴파일부터 확인하고 싶으시는군요.",
            "강재호: 죄송해요. 습관적으로...",
            "장바영: (한숨) 괜찮아요. 재호님다운 대답이에요. 항상 안정성을 우선시하시니까.",
            "강재호: 하지만 지금은 선배와의 시간이 더 중요해요.",
            "장바영: (조금 밝아지며) 정말요?",
            "강재호: 네. 코드는 나중에 컴파일해도 되지만, 이 별빛은 지금뿐이에요.",
            "장바영: (미소지으며) 그래요... 그럼 컴파일은 나중에 하고, 지금은 이 순간을 즐겨볼까요?",
            "강재호: 네! 그게 더 좋을 것 같아요.",
            "장바영: (별을 가리키며) 저 별들도 컴파일 없이 그냥 빛나고 있잖아요."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "jason_extra_romance"}
        ]
    ),
    
    # 제이슨 추가 이벤트 - JavaScript 비동기 놀이공원
    StoryEvent(
        id="jason_extra_romance",
        chapter=7,
        background="amusement_park",
        characters=["JASON", "KANG"],
        dialogs=[
            "제이슨이 강재호를 놀이공원으로 데려왔다.",
            "제이슨: 와! 놀이공원이다! 여기서 실시간 JavaScript 코딩 해볼까?",
            "강재호: 놀이공원에서 코딩이요?",
            "제이슨: (노트북을 꺼내며) 응! 봐봐, 놀이공원도 이벤트 기반이야!",
            "[CODE_IMAGE:amusement_park.png]",
            "강재호: 제이슨... 이 코드는 또 뭐예요?",
            "제이슨: (윙크) 너 때문에 내 심장이 계속 이벤트 리스너 등록하고 있어!",
            "바이킹을 타며 제이슨이 무서워한다.",
            "제이슨: 으아아악! 이거 완전 callback hell이야!",
            "강재호: 콜백 지옥이요?",
            "제이슨: (강재호 팔을 잡으며) 응! 무서워서 무서워서... 근데 너 잡으니까 Promise.resolve()됐어!",
            "따뜻한 포옹 속에서 모든 걱정이 사라진다.",
            "관람차에서 야경을 본다.",
            "제이슨: 와... 이 뷰 정말 예쁘다. 마치 CSS로 background-image 설정한 것 같아!",
            "강재호: 제이슨은 정말 모든 걸 코딩으로 비유하네요.",
            "제이슨: (가까이 다가가며) 그럼 이건 어때? setTimeout(() => { 너와_함께_있고_싶어(); }, 영원히);",
            "강재호: 영원히 timeout 설정이요?",
            "제이슨: (손을 잡으며) 응! 비동기 처리지만... 너랑 있으면 시간이 멈춘 것 같거든!",
            "함께 밤하늘을 올려다본다. 별빛 아래 두 사람.",
            "강재호: 그럼 제가 clearTimeout 하면 안 되겠네요.",
            "제이슨: (활짝 웃으며) 절대 안 돼! 그건 fatal error야!"
        ],
        choices=[
            {"text": "우리 관계를 local storage에 저장할까요?", "effect": {"JASON": 20}, "next_event": "jason_romantic_response2"},
            {"text": "저도 제이슨과 함께하는 모든 순간이 async/await이에요", "effect": {"JASON": 25}, "next_event": "jason_romantic_response1"},
            {"text": "DOM 조작부터 배워야겠어요", "effect": {"JASON": 15}, "next_event": "jason_practical_response"}
        ]
    ),
    
    # 제이슨 선택지 반응들
    StoryEvent(
        id="jason_romantic_response1",
        chapter=7,
        background="amusement_park",
        characters=["JASON", "KANG"],
        dialogs=[
            "제이슨: (눈을 반짝이며) 정말? 너도 async/await 느낌이야?",
            "강재호: 네! 제이슨과 함께 있으면 모든 게 완벽하게 동기화돼요.",
            "제이슨: (감동하며) 와... 그럼 우리 사이에는 callback hell이 없겠네!",
            "강재호: 네, 항상 smooth한 비동기 처리예요.",
            "제이슨: (가까이 다가가며) 그럼... 우리 Promise.all()로 모든 걸 함께 처리할까?",
            "강재호: 좋아요! 제이슨과 함께라면 어떤 비동기 작업도 두렵지 않아요.",
            "제이슨: (손을 잡으며) 그럼 이제부터 우리는 perfect async couple이야!",
            "강재호: await 제이슨_사랑(); 이 항상 성공할 것 같아요.",
            "제이슨: (웃으며) return Promise.resolve('영원한_행복');",
            "관람차에서 내려와 둘이 함께 걸으며 손을 꼭 잡는다.",
            "제이슨: 이제 우리 관계는 완전히 비동기 처리 완료!"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "group_bonding_event"}
        ]
    ),
    
    StoryEvent(
        id="jason_romantic_response2",
        chapter=7,
        background="amusement_park",
        characters=["JASON", "KANG"],
        dialogs=[
            "제이슨: (깜짝 놀라며) local storage에? 우리 관계를?",
            "강재호: 네! 브라우저를 닫아도 사라지지 않게요.",
            "제이슨: (감동하며) 와... 그럼 영구 저장이네!",
            "강재호: 맞아요. session storage가 아니라 local storage니까요.",
            "제이슨: (노트북을 꺼내며) 그럼 진짜로 저장해볼까?",
            "제이슨이 실제로 코드를 입력한다.",
            "제이슨: localStorage.setItem('우리의_사랑', JSON.stringify({",
            "제이슨:   시작일: '오늘',",
            "제이슨:   상태: '진행중',",
            "제이슨:   행복도: Infinity",
            "제이슨: }));",
            "강재호: (웃으며) 이제 우리 사랑이 브라우저에 영구 저장됐네요!",
            "제이슨: (손을 잡으며) 그리고 localStorage.getItem()으로 언제든 불러올 수 있어!",
            "강재호: 제이슨과의 추억은 절대 삭제되지 않을 거예요."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "group_bonding_event"}
        ]
    ),
    
    StoryEvent(
        id="jason_practical_response",
        chapter=7,
        background="amusement_park",
        characters=["JASON", "KANG"],
        dialogs=[
            "제이슨: (약간 아쉬워하며) 아... DOM 조작부터 배우고 싶구나.",
            "강재호: 죄송해요. 기초부터 차근차근 하고 싶어서...",
            "제이슨: (한숨) 괜찮아. 너답긴 해. 항상 기초를 중요하게 생각하니까.",
            "강재호: 하지만 지금은 제이슨과의 시간이 더 중요해요.",
            "제이슨: (조금 밝아지며) 정말?",
            "강재호: 네. DOM은 나중에 조작해도 되지만, 이 순간은 지금뿐이에요.",
            "제이슨: (미소지으며) 그래... 그럼 DOM 조작은 나중에 하고, 지금은 우리만의 시간을 가져볼까?",
            "강재호: 네! 그게 더 좋을 것 같아요.",
            "제이슨: (장난스럽게) 그럼 지금부터는 DOM 말고 내 마음을 조작해줘!"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "group_bonding_event"}
        ]
    ),
    
    # 단체 유대감 강화 이벤트
    StoryEvent(
        id="group_bonding_event",
        chapter=7,
        background="pension",
        characters=["CHOI", "PARK", "JANG", "JASON", "KANG"],
        dialogs=[
            "F&B 동아리 MT 둘째 날 밤",
            "펜션 거실에서 다섯 명이 모여 코딩 토크쇼를 한다.",
            "최시은: 자, 오늘은 각자 언어의 특징으로 재호를 표현해보자!",
            "박이선: 오! 재밌겠다! 나부터 할게!",
            "박이선: 재호는 완전 import happiness! 그냥 있기만 해도 내 코드가 더 행복해져!",
            "장바영: 저는... 재호님을 Student 클래스로 만들고 싶어요. private 마음을 public으로 공개하고 싶게 만드는...",
            "제이슨: 나는 재호가 addEventListener 같아! 내 심장에 이벤트 리스너 등록해서 계속 두근거리게 만들어!",
            "최시은: (얼굴 빨개지며) 나는... 재호가 내 포인터야. 내 마음 주소를 정확히 가리키고 있어.",
            "모든 시선이 강재호에게 집중된다.",
            "강재호: (당황하며) 와... 다들 정말 창의적이시네요...",
            "최시은: 그럼 너는 우리를 어떤 코드로 표현할 거야?",
            "박이선: 궁금해! 우리도 각자 다른 언어잖아!",
            "장바영: 재호님의 개발자적 관점이 궁금해요.",
            "제이슨: 맞아! 우리를 어떻게 코딩할 건지!",
            "강재호: 음... 사실 여러분은 각자 다른 언어지만, 모두 제게 꼭 필요한 라이브러리 같아요.",
            "최시은: 라이브러리?",
            "강재호: 네! 시은 선배는 stdio.h 같은 기본 라이브러리, 이선 선배는 pandas 같은 데이터 처리 라이브러리...",
            "강재호: 바영 선배는 Spring Framework 같은 안정적인 프레임워크, 제이슨은 React 같은 동적인 라이브러리요!",
            "박이선: 우와! 그럼 우리가 모여야 완전한 프로그램이 되는 거네?",
            "강재호: (고개 끄덕이며) 맞아요! 각자 없으면... 컴파일 에러가 날 것 같아요.",
            "제이슨: 와! 그럼 우리는 재호의 개발 환경인 거야!",
            "장바영: 체계적으로 버전 관리하면서 함께 개발하면 좋을 것 같아요.",
            "최시은: 그럼... 우리가 하나의 큰 프로젝트를 함께 하는 건가?",
            "박이선: 각자 다른 모듈을 담당하면서!",
            "제이슨: 완전 혁신적인 아키텍처다!",
            "강재호: 정말... 그런 팀 프로젝트 하고 싶어요!",
            "모든 멤버: Git push!/commit!/merge!/deploy!"
        ],
        choices=[
            {"text": "먼저 요구사항 분석부터 해야겠어요", "effect": {"CHOI": 10, "PARK": 10, "JANG": 10, "JASON": 10}, "next_event": "festival_event"},
            {"text": "그럼 우리 모두 하나의 레포지토리에서 협업할까요?", "effect": {"CHOI": 20, "PARK": 20, "JANG": 20, "JASON": 20}, "next_event": "festival_event"},
            {"text": "각자 브랜치 만들어서 나중에 merge 하죠!", "effect": {"CHOI": 25, "PARK": 25, "JANG": 25, "JASON": 25}, "next_event": "festival_event"}
        ]
    )
]

# 기존 INDIVIDUAL_EVENTS에 추가 이벤트들 합치기
INDIVIDUAL_EVENTS.extend(ADDITIONAL_ROMANCE_EVENTS) 