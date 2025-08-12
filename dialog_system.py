import pygame

class DialogSystem:
    def __init__(self):
        # Windows 기본 한글 폰트 경로
        font_paths = [
            "C:/Windows/Fonts/malgun.ttf",
            "C:/Windows/Fonts/gulim.ttc",
            "C:/Windows/Fonts/batang.ttc",
            "C:/Windows/Fonts/msyh.ttc",
            "C:/Windows/Fonts/msyhbd.ttc"
        ]
        
        # 폰트 파일 찾기
        font_loaded = False
        for font_path in font_paths:
            try:
                self.font = pygame.font.Font(font_path, 32)
                font_loaded = True
                break
            except (FileNotFoundError, OSError):
                continue
        
        # 폰트를 찾지 못한 경우
        if not font_loaded:
            self.font = pygame.font.SysFont(None, 32)
            
    def draw(self, screen, speaker, text):
        # 대화창 배경
        dialog_rect = pygame.Rect(140, 500, 1000, 200)
        pygame.draw.rect(screen, (0, 0, 0), dialog_rect)
        pygame.draw.rect(screen, (150, 150, 150), dialog_rect, 2)
        
        # 화자 이름
        if speaker:
            name_text = self.font.render(speaker, True, (255, 255, 255))
            screen.blit(name_text, (160, 520))
        
        # 대사
        dialog_text = self.font.render(text, True, (255, 255, 255))
        screen.blit(dialog_text, (160, 580))
    
    def draw_choices(self, screen, choices):
        for i, choice in enumerate(choices):
            choice_rect = self.choice_box.get_rect(
                centerx=640,
                top=300 + i * 80
            )
            self.choice_box.fill((0, 0, 0))
            screen.blit(self.choice_box, choice_rect)
            
            text_surface = self.font.render(choice["text"], True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=choice_rect.center)
            screen.blit(text_surface, text_rect) 