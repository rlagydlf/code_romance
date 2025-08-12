from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class StoryEvent:
    id: str
    chapter: int
    background: str
    characters: List[str]
    dialogs: List[str]
    choices: List[Dict] = None
    
    def __post_init__(self):
        if self.choices is None:
            self.choices = []

# 스토리 이벤트들
STORY_EVENTS = [
    # Chapter 1: 첫 만남
    StoryEvent(
        id="intro",
        chapter=1,
        background="campus",
        characters=["CHOI", "KANG"],
        dialogs=[
            "유성대 캠퍼스",
            "강재호가 컴퓨터과학과 신입생 오리엔테이션 자료를 들고 캠퍼스를 둘러보고 있다.",
            "강재호: (혼잣말로) 동아리 가입은 어디서 하는 거지? 프로그래밍 관련 동아리가 있을까?",
            "그때, 뒤에서 누군가의 목소리가 들린다.",
            "???: 어머, 너 에러 안 나게 생겼다. 우리 동아리 들어올래?",
            "강재호: (뒤돌아보며) 네? 누구세요?",
            "최시은: (당당하게) 나는 F&B의 회장 최시은이야.",
            "강재호: F&B이요?",
            "최시은: 우리 학교 최고의 프로그래밍 동아리지. 보통 사람들은 받아주지 않는데...",
            "최시은이 강재호를 위아래로 훑어본다.",
            "최시은: 너는... 뭔가 포인터 같은 느낌이야. 직접적이고 효율적일 것 같은?",
            "강재호: (당황하며) 저... 프로그래밍은 아직 초보라서...",
            "최시은: (웃으며) C언어처럼, 기초가 탄탄하면 뭐든 할 수 있어. 너 우리 동아리에 잘 맞을 것 같은데 어때? 기회는 오늘뿐이야.",
            "강재호: 와, 정말 좋아요! 꼭 들어가고 싶어요!",
            "최시은: (만족스러워하며) 좋아. 그럼 따라와. 다른 멤버들도 소개해줄게."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "club_room_intro"}
        ]
    ),
    
    # Chapter 2: 동아리방에서의 첫 인상들
    StoryEvent(
        id="club_room_intro",
        chapter=2,
        background="club_room",
        characters=["CHOI", "PARK", "JANG", "JASON", "KANG"],
        dialogs=[
            "유성대 3층 F&B 동아리방",
            "최시은이 동아리방 문을 열자, 아늑하면서도 현대적인 공간이 나타난다. 가운데 책상과 의자가 배치되어있다. 서랍에는 상장들이 널려있다.",
            "최시은: 여기가 우리 아지트야. 24시간 오픈이고, 프로젝트할 때는 여기서 밤새기도 해.",
            "그때 따뜻한 목소리가 들린다.",
            "박이선: (컵라면을 끓이며) 어? 시은선배, 새로운 멤버에요?",
            "최시은: 응, 이선아. 이 친구 재호야. 방금 들어왔어.",
            "박이선: (밝게 웃으며) 안녕! 나는 박이선이야. Python 전담하고 있어. 너는 어떤 언어 관심 있어?",
            "강재호: 아직 잘 모르겠어요. 다양하게 배워보고 싶어서...",
            "박이선: 그럼 Python부터 시작하는 게 어때? 문법이 영어처럼 자연스러워서 배우기 쉬워. 내가 도와줄게!",
            "그때 동아리방 안쪽에서 차분한 목소리가 들린다.",
            "장바영: (노트북에서 시선을 들며) 신입생인가요?",
            "최시은: 바영이도 인사해. 우리 새로운 멤버야.",
            "장바영: (정중하게) 안녕하세요, 장바영입니다. Java와 객체지향 프로그래밍을 주로 다루고 있어요. 체계적으로 학습하고 싶다면 언제든 말씀해주세요.",
            "강재호: 와, 다들 전문 분야가 있으시네요. 저는 아직...",
            "갑자기 동아리방 문이 벌컥 열리며 활기찬 목소리가 들린다.",
            "제이슨: (숨을 헐떡이며) 죄송해요! 제가 좀 늦었죠! 프론트엔드 스터디가 늦게 끝나서...",
            "제이슨: (강재호를 발견하고) 오? 새로운 멤버에요?",
            "최시은: 제이슨아, 너도 소개해.",
            "제이슨: (환하게 웃으며) 안녕! 나는 제이슨! JavaScript랑 웹 개발 담당이야! 너도 혹시 웹에 관심 있어?",
            "강재호: 네, 관심 많아요!",
            "제이슨: 대박! 그럼 나랑 같이 프로젝트 하자! JavaScript는 정말 재밌어!"
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "first_assignment"}
        ]
    ),
    
    # Chapter 3: 첫 번째 과제
    StoryEvent(
        id="first_assignment",
        chapter=3,
        background="club_room",
        characters=["CHOI", "PARK", "JANG", "JASON", "KANG"],
        dialogs=[
            "일주일 후",
            "최시은: (단상에 서며) 자, 다들 첫 번째 과제 결과를 발표해보자. 재호야, 너부터 해볼래?",
            "강재호: (긴장하며) 네... 저는 간단한 자기소개 프로그램을 만들어봤어요.",
            "강재호가 화면에 프로그램을 실행하자, 간단하지만 정성스럽게 만든 콘솔 프로그램이 나타난다.",
            "[CODE_IMAGE:jaeho_intro_program.png]",
            "박이선: (박수치며) 와! 정말 잘했어! 첫 프로그램치고는 너무 깔끔한데?",
            "장바영: 코드 구조도 체계적이네요. 객체지향적 사고가 조금 더 들어가면 더 좋을 것 같아요.",
            "제이슨: 이거 웹버전으로도 만들어볼래? HTML이랑 CSS 추가하면 더 멋져질 거야!",
            "최시은: (만족스러워하며) 좋아. 다음 과제는 각자 전문 언어로 간단한 유틸리티 프로그램 만들기야. 재호는 누구랑 팀 할래?",
            "강재호: 음... 사실 모든 언어를 다 배워보고 싶어요. 다들 도움을 받을 수 있을까요?",
            "최시은: 오, 의욕적이네! 좋아.",
            "박이선: 그럼 돌아가면서 각자 언어로 프로젝트 하나씩 도와주자!",
            "장바영: 체계적으로 학습하면 더 효과적일 것 같아요.",
            "제이슨: 완전 좋은 아이디어야! 우리가 다 선생님이 되는 거네!"
        ],
        choices=[
            {"text": "정말 감사해요! 모든 분께 배우고 싶어요!", "effect": {"CHOI": 10, "PARK": 10, "JANG": 10, "JASON": 10}, "next_event": "multi_project_start"}
        ]
    ),
    
    # 새로운 멀티 프로젝트 시작 이벤트
    StoryEvent(
        id="multi_project_start",
        chapter=3,
        background="club_room",
        characters=["CHOI", "PARK", "JANG", "JASON", "KANG"],
        dialogs=[
            "최시은: 그럼 이렇게 하자. 주별로 다른 언어로 미니 프로젝트를 해보는 거야.",
            "박이선: 1주차는 Python으로 데이터 분석 도구!",
            "장바영: 2주차는 Java로 간단한 관리 시스템!",
            "제이슨: 3주차는 JavaScript로 인터랙티브 웹페이지!",
            "최시은: 마지막 4주차는 C언어로 시스템 유틸리티!",
            "강재호: 와, 정말 체계적이네요! 열심히 배워보겠습니다!",
            "이렇게 강재호는 동아리 부원들과 함께 다양한 프로젝트를 진행하게 되었다."
        ],
        choices=[
            {"text": "첫 번째 프로젝트부터 시작하자!", "next_event": "individual_events"}
        ]
    ),

    
    # Chapter 5: 개별 이벤트들 - 순차적 진행
    StoryEvent(
        id="individual_events",
        chapter=5,
        background="club_room",
        characters=["CHOI", "PARK", "JANG", "JASON", "KANG"],
        dialogs=[
            "며칠 후, 강재호에게 여러 제안들이 들어온다.",
            "동아리 부원들이 개별적으로 시간을 보내자고 제안한다.",
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "choi_individual"}
        ]
    ),
    
    # Chapter 6: 갈등과 해결
    StoryEvent(
        id="conflict_event",
        chapter=6,
        background="club_room",
        characters=["CHOI", "PARK", "JANG", "JASON", "KANG"],
        dialogs=[
            "최시은: 이번 프로젝트는 효율성이 중요해. C언어로 시스템 프로그래밍하자.",
            "제이슨: 아니에요! 요즘은 웹이 대세라고요! JavaScript로 해요!",
            "장바영: 두 분 다 맞지만, 체계적인 접근이 필요해요. Java로 안정적으로...",
            "박이선: 다들 진정해요. Python으로 프로토타입부터 만들어보는 게 어때요?",
            "모든 시선이 강재호에게 집중된다.",
            "최시은: 재호야, 너는 어떻게 생각해?"
        ],
        choices=[
            {"text": "투표로 결정하는 게 공평할 것 같아요", "effect": {"CHOI": 5, "PARK": 5, "JANG": 5, "JASON": 5}, "next_event": "choi_extra_romance"},
            {"text": "각자 장점을 살려서 역할을 나누면 어떨까요?", "effect": {"CHOI": 5, "PARK": 5, "JANG": 5, "JASON": 5}, "next_event": "choi_extra_romance"},
            {"text": "모든 언어를 조금씩 써보는 건 어떨까요?", "effect": {"CHOI": 5, "PARK": 5, "JANG": 5, "JASON": 5}, "next_event": "choi_extra_romance"},
            {"text": "일단 간단한 것부터 시작해서 점차 확장해요", "effect": {"CHOI": 5, "PARK": 5, "JANG": 5, "JASON": 5}, "next_event": "choi_extra_romance"}
        ]
    ),
    
    # Chapter 8: 축제와 고백
    StoryEvent(
        id="festival_event",
        chapter=8,
        background="campus_festival",
        characters=["KANG"],
        dialogs=[
            "유성대 캠퍼스, 대동제 축제 현장",
            "강재호가 축제장을 걸어다니며 간식을 사먹고 있을 때, 핸드폰이 울린다.",
            "여러 명에게서 연이어 전화가 온다.",
            "모두 불꽃놀이를 함께 보자고 제안한다.",
            "누구와 함께할까?"
        ],
        choices=[
            {"text": "박이선에게 전화 - 도서관 옥상에서 함께", "next_event": "ending_park", "condition": "PARK >= 60"},
            {"text": "제이슨에게 전화 - PC방 테라스에서 함께", "next_event": "ending_jason", "condition": "JASON >= 60"},
            {"text": "최시은에게 전화 - 동아리방에서 함께", "next_event": "ending_choi", "condition": "CHOI >= 60"},
            {"text": "장바영에게 전화 - 세미나실에서 함께", "next_event": "ending_jang", "condition": "JANG >= 60"},
            {"text": "단체 통화방 만들기 - 모두 함께 중앙 광장에서", "next_event": "group_check"}
        ]
    ),
    
    # 엔딩들
    StoryEvent(
        id="ending_choi",
        chapter=99,
        background="club_room_evening",
        characters=["CHOI", "KANG"],
        dialogs=[
            "강재호가 최시은에게 전화를 건다.",
            "강재호: 선배, 저 갈게요. 동아리방에서 만나요.",
            "최시은: 정말? 고마워! 기다리고 있을게.",
            "동아리방의 불은 꺼져 있고, 창문을 통해 들어오는 축제 조명만이 방 안을 은은하게 비추고 있다.",
            "최시은: (돌아보며) 왔구나. 딱 맞춰서 왔네.",
            "강재호: 선배... 여기 분위기가 정말 좋네요.",
            "최시은: (자리를 가리키며) 여기 앉아. 불꽃놀이 곧 시작할 거야.",
            "둘이 나란히 앉아 창밖을 바라본다. 곧 하늘에 첫 번째 불꽃이 터진다.",
            "최시은: 예쁘다... 그런데 너 있어서 더 예쁜 것 같아.",
            "강재호: (놀라며) 선배...",
            "최시은: (강재호를 바라보며) 재호야, 솔직히 말할게. 나... 너를 좋아해.",
            "강재호: 정말요?",
            "최시은: C언어처럼 직설적으로 말하면, 너 없으면 내 프로그램이 제대로 돌아가지 않아.",
            "강재호가 최시은의 손을 잡는다.",
            "강재호: 저도... 선배를 좋아해요.",
            "최시은: (미소지으며) 그럼... 우리 커플이 된 거야?",
            "강재호: 네!",
            "불꽃놀이가 절정에 달하는 순간, 둘은 자연스럽게 서로를 바라보며 가까워진다.",
            "[최시은 엔딩 달성]"
        ],
        choices=[]
    ),
    
    StoryEvent(
        id="ending_park",
        chapter=99,
        background="library_rooftop",
        characters=["PARK", "KANG"],
        dialogs=[
            "강재호가 박이선에게 전화를 건다.",
            "강재호: 이선 선배, 갈게요! 도서관 옥상에서 만나요.",
            "박이선: 정말?! 좋아! 차 따뜻하게 준비해놓을게!",
            "도서관 옥상에는 작은 테이블과 의자가 준비되어 있고, 따뜻한 차가 김을 내고 있다.",
            "박이선: (환하게 웃으며) 와줘서 고마워! 차 식기 전에 마셔.",
            "강재호: 이선 선배가 직접 준비해주신 거예요?",
            "박이선: 응! Python처럼 간단하게 준비했어.",
            "둘이 차를 마시며 하늘을 올려다본다. 불꽃놀이가 시작된다.",
            "박이선: 정말 예쁘다... 근데 재호야.",
            "강재호: 네?",
            "박이선: 나... 너한테 전하고 싶은 말이 있어.",
            "[CODE_IMAGE:python_confession.png]",
            "박이선: (수줍게) 이게 내 진짜 마음이야.",
            "강재호: (감동하며) 이선 선배... 저도 같은 마음이에요.",
            "박이선: 정말? 그럼 우리...",
            "강재호: 네, 사귀어요!",
            "둘이 손을 잡고 불꽃놀이를 바라본다.",
            "[박이선 엔딩 달성]"
        ],
        choices=[]
    ),
    
    StoryEvent(
        id="ending_jang",
        chapter=99,
        background="library_seminar",
        characters=["JANG", "KANG"],
        dialogs=[
            "강재호가 장바영에게 전화를 건다.",
            "강재호: 바영 선배, 갈게요. 세미나실에서 만나요.",
            "장바영: 정말요? 감사합니다. 기다리고 있겠습니다.",
            "세미나실은 조용하고 차분한 분위기다. 장바영이 창가에 우아하게 앉아 있다.",
            "장바영: 와주셔서 감사합니다. 앉으세요.",
            "강재호: 바영 선배, 여기 정말 좋네요.",
            "장바영: 네, 조용해서 좋아요. 불꽃놀이도 잘 보이고요.",
            "불꽃놀이가 시작되자 둘은 함께 창밖을 바라본다.",
            "장바영: 재호님... 제가 평소에 너무 딱딱했나요?",
            "강재호: 아니에요. 안정감이 있어서 좋았어요.",
            "장바영: 그럼... 솔직히 말씀드려도 될까요?",
            "강재호: 네, 말씀하세요.",
            "장바영: 저... 재호님을 좋아합니다.",
            "[CODE_IMAGE:java_confession.png]",
            "장바영: 객체지향적으로 표현하면 이런 마음이에요.",
            "강재호: 저도... 선배를 좋아해요.",
            "장바영: (부드러운 미소로) 그럼... 우리 사귀어요.",
            "강재호: 네!",
            "둘이 조심스럽게 손을 잡는다.",
            "[장바영 엔딩 달성]"
        ],
        choices=[]
    ),
    
    StoryEvent(
        id="ending_jason",
        chapter=99,
        background="pc_cafe_rooftop",
        characters=["JASON", "KANG"],
        dialogs=[
            "강재호가 제이슨에게 전화를 건다.",
            "강재호: 제이슨, 갈게요! PC방 테라스에서 만나요.",
            "제이슨: 우와!!! 진짜?! 완전 좋아!! 기다릴게!!",
            "테라스는 활기찬 분위기로 꾸며져 있다. 제이슨이 신나게 강재호를 맞이한다.",
            "제이슨: 재호! 왔구나! 완전 최고의 뷰포인트야!",
            "강재호: 와, 여기서 보니까 정말 다르네요!",
            "제이슨: 그치? 나만 아는 비밀 장소야!",
            "불꽃놀이가 시작되자 제이슨이 갑자기 진지해진다.",
            "제이슨: 재호... 나 너한테 할 말이 있어.",
            "강재호: 뭐예요?",
            "제이슨: 사실 나... 너를 좋아해.",
            "[CODE_IMAGE:javascript_confession.png]",
            "제이슨: 이게 내 진짜 마음이야!",
            "강재호: 제이슨... 저도 같은 마음이에요.",
            "제이슨: 정말?! 야호!",
            "제이슨이 기뻐하며 강재호를 안아준다.",
            "제이슨: 우리 사귀자!",
            "강재호: 네!",
            "[제이슨 엔딩 달성]"
        ],
        choices=[]
    ),
    
    # 단체 통화방 선택 후 조건 체크
    StoryEvent(
        id="group_check",
        chapter=8,
        background="campus_festival",
        characters=["KANG"],
        dialogs=[
            "강재호가 단체 통화방을 만들어 모든 멤버들에게 전화를 건다.",
            "강재호: 여러분! 다들 중앙 광장에서 같이 불꽃놀이 볼까요? 우리 모두 함께!",
            "모든 멤버들이 기꺼이 응답한다."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "auto_branch"}
        ]
    ),
    
    StoryEvent(
        id="ending_group",
        chapter=99,
        background="campus_festival",
        characters=["CHOI", "PARK", "JANG", "JASON", "KANG"],
        dialogs=[
            "최시은: 역시 재호답네. 모두 함께 하자는 거.",
            "박이선: 좋은 생각이야! 다 같이 보는 게 더 재밌을 것 같아.",
            "장바영: 단체로 보는 것도 의미가 있을 것 같아요.",
            "제이슨: 완전 좋아! 다 같이 추억 만들자!",
            "곧 모든 멤버들이 하나둘 중앙 광장에 모여든다.",
            "불꽃놀이가 시작되고, 다섯 명이 나란히 앉아 하늘을 올려다본다.",
            "강재호: 우리 모두 함께해서 정말 좋네요.",
            "최시은: F&B 동아리 최고!",
            "모든 멤버: F&B 화이팅!",
            "[해피 엔딩 - 모두와 함께 달성]",
            "",
            "그런데 이 이야기는 여기서 끝이 아니었다...",
            "만약 모든 캐릭터와의 호감도가 충분히 높다면, 특별한 후일담이 기다리고 있을지도 모른다."
        ],
        choices=[
            {"text": "히든 엔딩 확인하기", "next_event": "harem_ending_check"}
        ]
    ),
    
    # 히든 엔딩 체크 이벤트
    StoryEvent(
        id="harem_ending_check",
        chapter=99,
        background="campus_festival",
        characters=["KANG"],
        dialogs=[
            "호감도를 확인하는 중...",
            "모든 캐릭터와의 호감도가 90 이상인지 체크합니다."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "harem_ending_result"}
        ]
    ),
    
    # 히든 엔딩: 풀스택 하렘 엔딩 (모든 호감도 90 이상)
    StoryEvent(
        id="harem_ending",
        chapter=99,
        background="restaurant",
        characters=["CHOI", "PARK", "JANG", "JASON", "KANG"],
        dialogs=[
            "4년 후, F&B 동아리 멤버 모임",
            "강재호는 대학 졸업 후 스타트업을 창업했다. 그의 회사 '풀스택 솔루션즈'는 빠르게 성장하고 있었다.",
            "오늘은 오랜만에 모든 F&B 멤버들이 모이는 날이다. 장소는 캠퍼스 근처의 아늑한 레스토랑.",
            "강재호: (혼잣말로) 오랜만에 모임이네. 다들 어떻게 지내고 있을까?",
            "모든 F&B 멤버들이 레스토랑에 모였다. 모두 성공한 개발자가 되어 있었다.",
            "최시은: 재호야! 너 완전 대박 났더라? CEO라니!",
            "박이선: 우와, 정말 대단해! 풀스택 개발자에서 풀스택 CEO가 됐네!",
            "장바영: 축하드려요. 체계적으로 사업을 확장하신 것 같네요.",
            "제이슨: 진짜 완전 쩐다! 우리도 다 잘 되고 있어!",
            "강재호: 다들 만나서 정말 반가워요. 그런데...",
            "강재호: 사실 오늘 여러분을 부른 이유가 있어요.",
            "최시은: 뭔데?",
            "강재호: 우리 회사에서 새로운 프로젝트를 시작하는데... 각자 전문 분야가 필요해요.",
            "박이선: 설마...?",
            "강재호: 시은 선배는 CTO로 시스템 아키텍처를, 이선 선배는 AI 개발팀장으로, 바영 선배는 백엔드 개발팀장으로, 제이슨은 프론트엔드 개발팀장으로...",
            "장바영: 그럼 우리가 모두...",
            "강재호: 네! 다시 한 팀이 되는 거예요!",
            "최시은: 재호야... 사실 나 아직도 너를 좋아해.",
            "박이선: 나도! 대학 때부터 지금까지 계속!",
            "장바영: 저도... 마찬가지입니다.",
            "제이슨: 나도나도! 완전 좋아해!",
            "강재호: (당황하며) 어... 다들...",
            "최시은: 우리 다 알고 있어. 서로 너를 좋아한다는 거.",
            "박이선: 그래서 우리끼리 이야기해봤어.",
            "장바영: 만약 재호님이 괜찮으시다면...",
            "제이슨: 우리 모두 함께하는 건 어때?!",
            "강재호: 모두 함께...요?",
            "최시은: 비즈니스 파트너로도, 개인적으로도 말이야.",
            "박이선: 각자 다른 매력이 있으니까, 상황에 따라 다르게!",
            "장바영: 체계적으로 스케줄 관리하면 가능할 것 같아요.",
            "제이슨: 완전 혁신적인 관계! 어때?",
            "강재호: (웃으며) 그럼... 회사도 풀스택, 관계도 풀스택이네요.",
            "최시은: (노트북을 꺼내며) 그럼 우리만의 특별한 계약서를 작성해보자.",
            "[CODE_IMAGE:fullstack_contract.png]",
            "박이선: 이거 너무 귀여운데?",
            "장바영: 체계적이고 좋네요.",
            "제이슨: 완전 혁신적이야!",
            "",
            "--- 5년 후 ---",
            "[BACKGROUND_CHANGE:office]",
            "풀스택 솔루션즈 본사 CEO실",
            "강재호의 책상에는 네 명의 사진이 놓여있다. 회사는 업계 1위로 성장했고, 다섯 명의 특별한 관계도 계속되고 있었다.",
            "강재호: (독백) 누가 개발자가 연애 못한다고 했지? 나는 풀스택으로 사랑까지 개발했는데!",
            "벽에 걸린 회사 슬로건: 'Full Stack Solutions - 기술도, 사랑도 풀스택으로!'",
            "히든 엔딩: 풀스택 하렘왕 달성!",
            "축하합니다! 당신은 연애 시뮬레이션의 궁극의 엔딩을 달성했습니다!"
        ],
        choices=[]
    )
]

# 개별 이벤트들 import
from story_events_individual import INDIVIDUAL_EVENTS

# 기존 STORY_EVENTS에 개별 이벤트들 추가
STORY_EVENTS.extend(INDIVIDUAL_EVENTS)

# 캐릭터 정보
from character import Character

CHARACTERS = {
    "CHOI": Character(
        id="CHOI",
        name="Choi Si-eun",
        korean_name="최시은",
        description="F&B 동아리 회장. C언어 전문가로 직설적이고 효율적인 성격.",
        normal_image_path="assets/images/characters/choi.png",
        blush_image_path="assets/images/characters/choi_blush.png",
        affection=30
    ),
    "PARK": Character(
        id="PARK",
        name="Park I-seon",
        korean_name="박이선",
        description="Python 전문가. 따뜻하고 자연스러운 성격으로 누구와도 쉽게 친해진다.",
        normal_image_path="assets/images/characters/park.png",
        blush_image_path="assets/images/characters/park_blush.png",
        affection=30
    ),
    "JANG": Character(
        id="JANG",
        name="Jang Ba-yeong",
        korean_name="장바영",
        description="F&B 동아리 부회장. Java 전문가로 체계적이고 우아한 성격.",
        normal_image_path="assets/images/characters/jang.png",
        blush_image_path="assets/images/characters/jang_blush.png",
        affection=30
    ),
    "JASON": Character(
        id="JASON",
        name="Jason",
        korean_name="제이슨",
        description="JavaScript 전문가. 활발하고 창의적인 성격으로 항상 새로운 아이디어가 넘친다.",
        normal_image_path="assets/images/characters/jason.png",
        blush_image_path="assets/images/characters/jason_blush.png",
        affection=30
    ),
    "KANG": Character(
        id="KANG",
        name="Kang Jae-ho",
        korean_name="강재호",
        description="주인공. 프로그래밍에 관심이 많은 신입생.",
        normal_image_path="assets/images/characters/kang.png",
        blush_image_path="assets/images/characters/kang_blush.png",
        affection=0
    )
}

# 엔딩 이벤트들
ENDING_EVENTS = []

# 특별 엔딩들
SPECIAL_ENDINGS = []

# 자동 분기 이벤트
StoryEvent(
    id="auto_branch",
    chapter=8,
    background="campus_festival",
    characters=["KANG"],
    dialogs=[
        "호감도를 확인하는 중..."
    ],
    choices=[]
)

# 히든 엔딩 결과 이벤트
StoryEvent(
    id="harem_ending_result",
    chapter=99,
    background="campus_festival",
    characters=["KANG"],
    dialogs=[
        "모든 캐릭터와의 호감도가 90 이상입니다!",
        "히든 엔딩으로 진행합니다."
    ],
    choices=[
        {"text": "(다음으로)", "next_event": "harem_ending"}
    ]
)

STORY_EVENTS.extend([
    StoryEvent(
        id="auto_branch",
        chapter=8,
        background="campus_festival",
        characters=["KANG"],
        dialogs=[
            "호감도를 확인하는 중..."
        ],
        choices=[]
    ),
    StoryEvent(
        id="harem_ending_result",
        chapter=99,
        background="campus_festival",
        characters=["KANG"],
        dialogs=[
            "모든 캐릭터와의 호감도가 90 이상입니다!",
            "히든 엔딩으로 진행합니다."
        ],
        choices=[
            {"text": "(다음으로)", "next_event": "harem_ending"}
        ]
    )
]) 