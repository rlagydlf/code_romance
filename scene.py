import pygame
import os

class Scene:
    def __init__(self, name, background_path):
        self.name = name
        self.background = None
        
        # 파일 존재 여부 확인 후 로드
        if os.path.exists(background_path):
            try:
                self.background = pygame.image.load(background_path)
                self.background = pygame.transform.scale(self.background, (1280, 720))
            except pygame.error:
                self._create_default_background()
            
    def draw(self, screen):
        screen.blit(self.background, (0, 0)) 