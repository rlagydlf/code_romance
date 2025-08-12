import pygame
from story_data import STORY_EVENTS, ENDING_EVENTS, SPECIAL_ENDINGS, CHARACTERS
from dialog_system import DialogSystem
from scene import Scene



# Screen dimensions
W, H = 1280, 720

class Game:
    # 상수 정의
    MAIN_CHARACTERS = ["CHOI", "PARK", "JANG", "JASON"]
    HAREM_ENDING_THRESHOLD = 90
    FESTIVAL_ENDING_THRESHOLD = 100
    BLUSHING_DURATION = 300  # 5초 (60FPS 기준)
    AFFECTION_DISPLAY_DURATION = 180  # 3초
    
    def __init__(self, screen):
        self.screen = screen
        self.dialog = DialogSystem()
        self.event = None
        self.idx = 0
        self.choices_on = False
        self.choices = []
        self.name = "강재호"
        self.chapter = 1
        self.affection_on = False
        self.affection_timer = 0
        self.affection_changes = []
        self.blush = {}
        self.selected = 0
        self.font = pygame.font.Font("assets/fonts/NanumGothic.ttf", 32)
        self.state = "TITLE"
        self.love = {k: 30 for k in CHARACTERS.keys() if k != "KANG"}
        self.last_chap = 1
        self.event_map = {event.id: event for event in STORY_EVENTS}
        self.name_map = {}
        for cid, char in CHARACTERS.items():
            self.name_map[char.korean_name] = cid
            self.name_map[char.name] = cid
        self.bg_map = {
            "campus": "assets/images/backgrounds/campus.png",
            "club_room": "assets/images/backgrounds/club_room.png",
            "club_room_evening": "assets/images/backgrounds/club_room_evening.png",
            "club_room_late_night": "assets/images/backgrounds/club_room_late_night.png",
            "cafe": "assets/images/backgrounds/cafe.png",
            "library_seminar": "assets/images/backgrounds/library_seminar.png",
            "library_rooftop": "assets/images/backgrounds/library_rooftop.png",
            "park": "assets/images/backgrounds/park.png",
            "park_home": "assets/images/backgrounds/park_home.png",
            "pc_cafe": "assets/images/backgrounds/pc_cafe.png",
            "pc_cafe_rooftop": "assets/images/backgrounds/pc_cafe_rooftop.png",
            "campus_festival": "assets/images/backgrounds/campus_festival.png",
            "office": "assets/images/backgrounds/office.png",
            "restaurant": "assets/images/backgrounds/restaurant.png",
            "observatory": "assets/images/backgrounds/observatory.png",
            "amusement_park": "assets/images/backgrounds/amusement_park.png",
            "pension": "assets/images/backgrounds/pension.png"
        }
        
    # 이벤트 ID로 이벤트를 찾는다
    def find_event_by_id(self, event_id):
        return self.event_map.get(event_id)
    
    # 지정된 이벤트로 전환한다
    def switch_to_event(self, event_id):
        event = self.find_event_by_id(event_id)
        if event:
            self.event = event
            self.idx = 0
            self.selected = 0
            self.update_scene()
            return True
        return False

    # 새 게임을 시작한다
    def start_new_game(self):
        # affection 초기화
        for k in self.love:
            self.love[k] = 30
        for char in CHARACTERS.values():
            if hasattr(char, 'affection'):
                char.affection = 30
        if STORY_EVENTS:
            self.event = STORY_EVENTS[0]
            self.idx = 0
            self.choices_on = False
            self.update_scene()


    
    # 입력 이벤트를 처리한다
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.state == "TITLE":
                if event.key == pygame.K_SPACE:
                    self.state = "PLAYING"
                    self.start_new_game()
            elif self.state == "PLAYING":
                # 선택지가 있는 경우
                if self.event and self.event.choices and self.idx >= len(self.event.dialogs) - 1:
                    # 사용 가능한 선택지 수 확인
                    available_choices = getattr(self.event, 'available_choices', self.event.choices)
                    
                    if event.key == pygame.K_UP:
                        self.selected = max(0, self.selected - 1)
                    elif event.key == pygame.K_DOWN:
                        self.selected = min(len(available_choices) - 1, self.selected + 1)
                    elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.handle_choice(self.selected)
                    elif event.key >= pygame.K_1 and event.key <= pygame.K_9:
                        choice_num = event.key - pygame.K_1
                        if choice_num < len(available_choices):
                            self.handle_choice(choice_num)
                else:
                    # 일반 대화 진행
                    if event.key == pygame.K_SPACE:
                        self.progress_dialog()
            elif self.state == "GAME_OVER":
                if event.key == pygame.K_SPACE:
                    self.state = "TITLE"
            

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.state == "TITLE":
                # 타이틀 화면에서 클릭 시 게임 시작
                self.state = "PLAYING"
                self.start_new_game()
            elif self.state == "PLAYING":
                # 선택지가 있는 경우 마우스 클릭으로 선택
                if self.event and self.event.choices and self.idx >= len(self.event.dialogs) - 1:
                    mouse_x, mouse_y = event.pos
                    
                    # 사용 가능한 선택지 확인
                    available_choices = getattr(self.event, 'available_choices', self.event.choices)
                    
                    choice_count = len(available_choices)
                    choice_height = 50
                    choice_spacing = 15
                    total_height = choice_count * choice_height + (choice_count - 1) * choice_spacing
                    
                    # 화면 중앙에 위치 계산
                    screen_center_y = 360  # 화면 높이의 중앙
                    start_y = screen_center_y - total_height // 2
                    
                    choice_width = 900  # 선택지 너비
                    choice_x = (1280 - choice_width) // 2  # 화면 가로 중앙
                    
                    for i, choice in enumerate(available_choices):
                        choice_y = start_y + i * (choice_height + choice_spacing)
                        choice_rect = pygame.Rect(choice_x, choice_y, choice_width, choice_height)
                        if choice_rect.collidepoint(mouse_x, mouse_y):
                            self.handle_choice(i)
                            break
                else:
                    # 일반 대화 진행
                    self.progress_dialog()
    
    # 대화 한 줄을 진행한다
    def progress_dialog(self):
        if not self.event:
            return
        
        # dialogs는 문자열 리스트이므로 마지막 인덱스까지 진행
        if self.idx >= len(self.event.dialogs) - 1:
            if hasattr(self.event, 'choices') and self.event.choices:
                self.choices_on = True
                self.choices = self.event.choices
            else:
                # 엔딩 이벤트인 경우 게임 종료 (단, harem_ending으로 시작하는 id는 예외)
                if self.event.id.startswith("ending_") or (self.event.id == "harem_ending"):
                    self.state = "GAME_OVER"
                elif self.event.id.startswith("harem_ending"):
                    # 하렘 엔딩 시리즈는 계속 진행
                    self.move_to_next_event()
                else:
                    self.move_to_next_event()
        else:
            self.idx += 1
            
            # 현재 대화 라인 확인
            if self.idx < len(self.event.dialogs):
                current_dialog = self.event.dialogs[self.idx]
                
                # 배경 변경 태그 처리
                if current_dialog.startswith("[BACKGROUND_CHANGE:") and current_dialog.endswith("]"):
                    bg_name = current_dialog[19:-1]  # [BACKGROUND_CHANGE: 와 ] 제거
                    # 배경 변경
                    bg_path = self.bg_map.get(bg_name, "assets/images/backgrounds/classroom.png")
                    self.current_scene = Scene(bg_name, bg_path)
                    # 배경 변경 태그는 건너뛰고 다음 대화로 진행
                    self.progress_dialog()
                    return
                
                # 얼굴 빨개지기 효과 체크
                if "(얼굴 빨개지며)" in current_dialog or "(얼굴이 빨갛게 물들며)" in current_dialog:
                    # 현재 화자 찾기
                    if ":" in current_dialog:
                        speaker, _ = current_dialog.split(":", 1)
                        speaker = speaker.strip()
                        
                        char_id = self.find_character_by_name(speaker)
                        if char_id:
                            self.blush[char_id] = self.BLUSHING_DURATION
                
        # 붉어진 얼굴 상태 확인 및 설정
        dialog_line = self.event.dialogs[self.idx]
        if ":" in dialog_line:
            speaker_name, dialog_text = dialog_line.split(":", 1)
            speaker_name = speaker_name.strip()
            dialog_text = dialog_text.strip()

            # CHARACTERS 딕셔너리에서 speaker_name과 일치하는 캐릭터 찾기
            current_speaker_id = None
            for char_id, character_obj in CHARACTERS.items():
                if character_obj.korean_name == speaker_name or character_obj.name == speaker_name:
                    current_speaker_id = char_id
                    break

            if current_speaker_id:
                if "빨개지며" in dialog_text or "수줍게 웃으며" in dialog_text:
                    self.blush[current_speaker_id] = 180 # 3초 (60 FPS 기준)
                else:
                    # 대화가 바뀌면 붉어진 얼굴 상태 해제 (단, 현재 화자가 아닌 다른 캐릭터는 유지)
                    if current_speaker_id in self.blush:
                        del self.blush[current_speaker_id] # 현재 화자만 해제
    
    # 다음 이벤트로 이동한다
    def move_to_next_event(self):
        # 다음 이벤트는 next_event id로 찾음
        if hasattr(self.event, 'choices') and self.event.choices:
            # 선택지 분기에서만 next_event 사용
            return
        
        current_index = STORY_EVENTS.index(self.event)
        if current_index < len(STORY_EVENTS) - 1:
            next_event = STORY_EVENTS[current_index + 1]
            # 챕터가 바뀌면 챕터 전환 연출
            if hasattr(next_event, 'chapter') and next_event.chapter != self.last_chap:
                self.last_chap = next_event.chapter
            self.event = next_event
            self.idx = 0
            self.choices_on = False
            self.update_scene()

    
    # 호감도 변화를 화면에 표시한다
    def show_affection_change(self, character_id, change_amount, old_value, new_value):
        self.affection_on = True
        self.affection_timer = self.AFFECTION_DISPLAY_DURATION
        
        # 새로운 변화 추가
        change_info = {
            'character_id': character_id,
            'change': change_amount,
            'old_value': old_value,
            'new_value': new_value,
            'timer': self.AFFECTION_DISPLAY_DURATION
        }
        self.affection_changes.append(change_info)
    

    
    # 호감도 변화 알림을 그린다
    def draw_affection_change(self):
        """호감도 변화 알림을 화면에 그립니다."""
        if not self.affection_on or not self.affection_changes:
            return
        if not self.event or self.event.chapter < 3:
            return
        
        start_y = 200
        for i, change_info in enumerate(self.affection_changes):
            if change_info['timer'] <= 0:
                continue
            character_id = change_info['character_id']
            change = change_info['change']
            new_value = change_info['new_value']
            alpha = min(255, change_info['timer'] * 2)
            
            if character_id in CHARACTERS:
                display_name = CHARACTERS[character_id].korean_name
                if change > 0:
                        color = (144, 238, 144)
                        sign = "+"
                else:
                        color = (255, 182, 193)
                        sign = ""
                text = f"{display_name} {sign}{change} (총 {new_value})"
                text_surface = self.font.render(text, True, color)
                text_rect = text_surface.get_rect()
                box_width = max(text_rect.width + 20, 200)
                box_height = text_rect.height + 10
                box_x = (1280 - box_width) // 2
                box_y = start_y + (i * 50)
                box_surface = pygame.Surface((box_width, box_height))
                box_surface.set_alpha(min(200, alpha))
                box_surface.fill((0, 0, 0))
                self.screen.blit(box_surface, (box_x, box_y))
                pygame.draw.rect(self.screen, color, (box_x, box_y, box_width, box_height), 2)
                text_x = box_x + 10
                text_y = box_y + 5
                self.screen.blit(text_surface, (text_x, text_y))
    
    # 선택지(선택 이벤트)를 처리한다
    def handle_choice(self, choice_index):
        if not self.event or not self.event.choices:
            return
        available_choices = getattr(self.event, 'available_choices', self.event.choices)
        if choice_index >= len(available_choices):
            return
        choice = available_choices[choice_index]
        # 호감도 변경
        if "effect" in choice:
            for char_id, affection_change in choice["effect"].items():
                if char_id in CHARACTERS:
                    old_affection = CHARACTERS[char_id].affection
                    CHARACTERS[char_id].affection += affection_change
                    new_affection = CHARACTERS[char_id].affection
                    self.show_affection_change(char_id, affection_change, old_affection, new_affection)
        # 이벤트별 특별 처리
        if self.event.id == "group_check" or self.event.id == "harem_ending_check":
            if self.check_all_high_affection(self.HAREM_ENDING_THRESHOLD):
                self.switch_to_event("harem_ending")
            else:
                self.switch_to_event("ending_group")
            return
        elif self.event.id == "ending_group":
            # ending_group에서 선택지를 누르면 무조건 게임 종료
            self.state = "GAME_OVER"
            return
        elif self.event.id == "festival_event":
            if (self.check_all_high_affection(self.FESTIVAL_ENDING_THRESHOLD) and 
                choice["text"] == "단체 통화방 만들기 - 모두 함께 중앙 광장에서"):
                self.switch_to_event("harem_ending")
                return
        if "next_event" in choice:
            next_event_id = choice["next_event"]
            if self.switch_to_event(next_event_id):
                return
        self.state = "GAME_OVER"

    

    
    # 게임 상태를 업데이트한다
    def update(self):
        """게임 상태 업데이트"""
        
        # 호감도 변화 알림 타이머 업데이트
        if self.affection_on:
            self.affection_timer -= 1
            
            # 각 호감도 변화의 타이머 업데이트
            for change_info in self.affection_changes[:]:  # 복사본으로 순회
                change_info['timer'] -= 1
                if change_info['timer'] <= 0:
                    self.affection_changes.remove(change_info)
            
            # 모든 알림이 끝나면 표시 종료
            if not self.affection_changes:
                self.affection_on = False

        # 붉어진 얼굴 상태 타이머 업데이트
        for char_id in list(self.blush.keys()): # 딕셔너리 변경 중 에러 방지 위해 list로 복사
            self.blush[char_id] -= 1
            if self.blush[char_id] <= 0:
                del self.blush[char_id]
    
    # 화면을 그린다
    def draw(self):
        if self.state == "TITLE":
            self.draw_title_screen()
        elif self.state == "PLAYING":
            self.draw_game_screen()
            if self.affection_on:
                self.draw_affection_change()
        elif self.state == "GAME_OVER":
            self.draw_game_over_screen()
        
        pygame.display.flip()
    
    # 타이틀 화면을 그린다
    def draw_title_screen(self):
        self.screen.fill((0, 0, 0))
        title_text = self.font.render("코드로맨스 : 디버깅된 사랑", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(640, 200))
        self.screen.blit(title_text, title_rect)
        start_text = self.font.render("스페이스바를 눌러 시작", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(640, 400))
        self.screen.blit(start_text, start_rect)

    # 호감도 패널을 그린다
    def draw_affection_status(self):
        if not self.event or self.event.chapter < 3:
            return
        panel_width = 320
        panel_height = 200
        panel_x = 1280 - panel_width - 10
        panel_y = 10
        panel_surface = pygame.Surface((panel_width, panel_height))
        panel_surface.set_alpha(200)
        panel_surface.fill((0, 0, 0))
        self.screen.blit(panel_surface, (panel_x, panel_y))
        pygame.draw.rect(self.screen, (255, 255, 255), (panel_x, panel_y, panel_width, panel_height), 2)
        title_font = pygame.font.Font("assets/fonts/NanumGothic.ttf", 26)
        title_text = title_font.render("호감도", True, (255, 255, 255))
        self.screen.blit(title_text, (panel_x + 10, panel_y + 8))
        char_font = pygame.font.Font("assets/fonts/NanumGothic.ttf", 18)
        for i, char_id in enumerate(self.MAIN_CHARACTERS):
            if char_id in CHARACTERS:
                character = CHARACTERS[char_id]
                affection = character.affection
                color = (255, 255, 255)
                name_text = f"{character.korean_name}: {affection}"
                text_surface = char_font.render(name_text, True, color)
                if text_surface.get_width() > panel_width - 20:
                    short_name = character.korean_name[:2]
                    name_text = f"{short_name}: {affection}"
                    text_surface = char_font.render(name_text, True, color)
                text_y = panel_y + 45 + (i * 35)
                self.screen.blit(text_surface, (panel_x + 10, text_y))
                bar_x = panel_x + 10
                bar_y = text_y + 20
                bar_width = panel_width - 20
                bar_height = 6
                pygame.draw.rect(self.screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
                fill_width = int((affection / 100) * bar_width)
                fill_width = min(fill_width, bar_width)
                if fill_width > 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (bar_x, bar_y, fill_width, bar_height))

    # 게임 오버 화면을 그린다
    def draw_game_over_screen(self):
        # 배경을 어둡게
        overlay = pygame.Surface((1280, 720))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # 게임 오버 텍스트
        game_over_text = self.font.render("게임 종료", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(640, 300))
        self.screen.blit(game_over_text, game_over_rect)
        
        # 재시작 안내
        restart_text = self.font.render("스페이스바를 눌러 다시 시작", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(640, 400))
        self.screen.blit(restart_text, restart_rect)
    
    # 텍스트를 줄바꿈한다
    def wrap_text(self, text, font, max_width):
        # 코드 이미지 태그 처리
        if text.startswith("[CODE_IMAGE:") and text.endswith("]"):
            return [text]  # 코드 이미지는 그대로 반환
        
        # 한글 텍스트의 경우 공백과 문장부호를 기준으로 분할
        if any('\u3131' <= char <= '\u3163' or '\uac00' <= char <= '\ud7a3' for char in text):
            # 한글이 포함된 경우
            words = []
            current_word = ""
            
            for char in text:
                if char in [' ', ',', '.', '!', '?', ':', ';', ')', '}', ']']:
                    if current_word:
                        words.append(current_word + char if char != ' ' else current_word)
                        current_word = ""
                    if char == ' ':
                        continue
                elif char in ['(', '{', '[']:
                    if current_word:
                        words.append(current_word)
                        current_word = ""
                    current_word = char
                else:
                    current_word += char
            
            if current_word:
                words.append(current_word)
        else:
            # 영어의 경우 기존 방식
            words = text.split(' ')
        
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + word + " " if current_line else word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line.strip())
                    current_line = word + " "
                else:
                    # 단어가 너무 길면 강제로 줄바꿈
                    lines.append(word)
                    current_line = ""
        
        if current_line:
            lines.append(current_line.strip())
        
        return lines

    # 코드 이미지를 그린다
    def draw_code_image(self, image_name, x, y):
        image_path = f"assets/images/code/{image_name}"
        code_image = pygame.image.load(image_path)
        code_image = pygame.transform.scale(code_image, (800, 400))
        self.screen.blit(code_image, (x, y))
        return 400  # 이미지 높이 반환

    # 게임 플레이 화면을 그린다
    def draw_game_screen(self):
        self.current_scene.draw(self.screen)
        self.draw_affection_status()
        current_speaker_id = None
        if self.event and self.idx < len(self.event.dialogs):
            dialog_line = self.event.dialogs[self.idx]
            if ":" in dialog_line:
                speaker, _ = dialog_line.split(":", 1)
                speaker = speaker.strip()
                current_speaker_id = self.find_character_by_name(speaker)
                if current_speaker_id and current_speaker_id in CHARACTERS:
                    character = CHARACTERS[current_speaker_id]
                    image_path_to_load = character.normal_image_path
                    if current_speaker_id in self.blush and character.blush_image_path:
                        image_path_to_load = character.blush_image_path
                    if image_path_to_load:
                        character_image = pygame.image.load(image_path_to_load)
                        character_image = pygame.transform.scale(character_image, (400, 600))
                        image_x = 50
                        image_y = (720 - 600) // 2
                        self.screen.blit(character_image, (image_x, image_y))
        
        # 현재 대화 표시
        if self.event and self.idx < len(self.event.dialogs):
            dialog_line = self.event.dialogs[self.idx]
            
            # 대화창 배경 - 크기 증가
            dialog_rect = pygame.Rect(50, 500, 1180, 170)
            pygame.draw.rect(self.screen, (0, 0, 0), dialog_rect)  # 완전 불투명한 검은색
            pygame.draw.rect(self.screen, (255, 255, 255), dialog_rect, 2)
            
            # 코드 이미지 처리
            if dialog_line.startswith("[CODE_IMAGE:") and dialog_line.endswith("]"):
                image_name = dialog_line[12:-1]  # [CODE_IMAGE: 와 ] 제거
                code_y = 250  # 코드 이미지 위치
                self.draw_code_image(image_name, 340, code_y)
            elif ":" in dialog_line:
                speaker, text = dialog_line.split(":", 1)
                speaker = speaker.strip()
                text = text.strip()
                
                # 화자 이름 표시 (위쪽 마진 5px 추가)
                speaker_surface = self.font.render(speaker, True, (255, 255, 0))
                self.screen.blit(speaker_surface, (70, 515))  # 510 + 5
                
                # 대화 텍스트를 줄바꿈하여 표시 (위쪽 마진 5px 추가)
                max_width = 1100  # 대화창 너비에서 여백 제외
                wrapped_lines = self.wrap_text(text, self.font, max_width)
                
                y_offset = 545  # 540 + 5 (화자 이름 아래로 충분한 간격 + 마진)
                line_height = 26  # 줄 간격 조정
                for line in wrapped_lines:
                    if y_offset > 645:  # 650 - 5 (대화창을 넘어가면 중단, 아래쪽 마진 고려)
                        break
                    text_surface = self.font.render(line, True, (255, 255, 255))
                    self.screen.blit(text_surface, (70, y_offset))
                    y_offset += line_height
            else:
                # 화자가 없는 경우 (나레이션 등) - 위쪽 마진 5px 추가
                wrapped_lines = self.wrap_text(dialog_line, self.font, 1100)
                y_offset = 515  # 510 + 5
                line_height = 26
                for line in wrapped_lines:
                    if y_offset > 645:  # 650 - 5 (아래쪽 마진 고려)
                        break
                    text_surface = self.font.render(line, True, (255, 255, 255))
                    self.screen.blit(text_surface, (70, y_offset))
                    y_offset += line_height
        
        # 선택지 표시 - 화면 정중앙에 표시, 겹침 방지
        if self.event and self.event.choices and self.idx >= len(self.event.dialogs) - 1:
            # 선택지 필터링
            available_choices = self.get_available_choices()
            
            if not available_choices:
                return
            
            choice_count = len(available_choices)
            choice_height = 50  # 선택지 높이 증가
            choice_spacing = 15  # 선택지 간격 증가
            total_height = choice_count * choice_height + (choice_count - 1) * choice_spacing
            
            # 화면 중앙에 위치 계산
            screen_center_y = 360  # 화면 높이의 중앙
            start_y = screen_center_y - total_height // 2
            
            choice_width = 900  # 선택지 너비 증가
            choice_x = (1280 - choice_width) // 2  # 화면 가로 중앙
            
            for i, choice in enumerate(available_choices):
                choice_y = start_y + i * (choice_height + choice_spacing)
                choice_rect = pygame.Rect(choice_x, choice_y, choice_width, choice_height)
                
                # 선택지 배경
                if i == self.selected:
                    pygame.draw.rect(self.screen, (100, 100, 200), choice_rect)  # 선택된 선택지
                else:
                    pygame.draw.rect(self.screen, (50, 50, 50), choice_rect)  # 일반 선택지
                
                pygame.draw.rect(self.screen, (255, 255, 255), choice_rect, 2)
                
                # 선택지 텍스트 - 줄바꿈 처리
                choice_text_lines = self.wrap_text(choice["text"], self.font, choice_width - 20)
                
                # 텍스트가 여러 줄인 경우 중앙 정렬
                total_text_height = len(choice_text_lines) * 24
                start_text_y = choice_rect.centery - total_text_height // 2
                
                for j, line in enumerate(choice_text_lines):
                    if j >= 2:  # 최대 2줄까지만 표시
                        break
                    line_surface = self.font.render(line, True, (255, 255, 255))
                    line_rect = line_surface.get_rect()
                    line_rect.centerx = choice_rect.centerx
                    line_rect.y = start_text_y + j * 24
                    self.screen.blit(line_surface, line_rect)
            
            # 현재 이벤트의 선택지를 사용 가능한 선택지로 임시 교체
            self.event.available_choices = available_choices
    
    # 현재 이벤트에서 사용 가능한 선택지를 반환한다
    def get_available_choices(self):
        """현재 이벤트에서 사용 가능한 선택지를 반환합니다."""
        if not self.event or not self.event.choices:
            return []
        
        available_choices = []
        
        # 축제 이벤트에서 호감도 조건 체크
        if self.event.id == "festival_event":
            for choice in self.event.choices:
                if "condition" in choice:
                    condition = choice["condition"]
                    # 호감도 조건 파싱 (예: "CHOI >= 60")
                    if ">=" in condition:
                        char_id, threshold = condition.split(" >= ")
                        if char_id in CHARACTERS and CHARACTERS[char_id].affection >= int(threshold):
                            available_choices.append(choice)
                    elif condition == "HIDDEN_ENDING":
                        # 히든 엔딩 조건 (현재는 사용하지 않음)
                        pass
                else:
                    available_choices.append(choice)
        else:
            # 다른 이벤트는 모든 선택지 사용 가능
            available_choices = self.event.choices[:]
        
        return available_choices

    # 배경 씬을 갱신한다
    def update_scene(self):
        # background 이름을 이미지 경로로 변환
        bg_name = getattr(self.event, 'background', None)
        bg_path = self.bg_map.get(bg_name, "assets/images/backgrounds/classroom.png")
        self.current_scene = Scene(bg_name, bg_path)
        
    # 화자 이름으로 캐릭터 ID를 찾는다
    def find_character_by_name(self, speaker_name):
        return self.name_map.get(speaker_name)
    
    # 모든 주요 캐릭터의 호감도가 임계값 이상인지 확인한다
    def check_all_high_affection(self, threshold):
        return all(CHARACTERS[char_id].affection >= threshold 
                  for char_id in self.MAIN_CHARACTERS) 