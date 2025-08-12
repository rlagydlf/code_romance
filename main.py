import pygame
import sys
from game import Game

# Pygame 초기화
pygame.init()
pygame.mixer.init()

# 스크린 크기 완전 고정
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("코드로맨스: 디버그된 사랑")

def main():
    # 게임 인스턴스 생성
    game = Game(screen)
    if game is None:
        return
    
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            # 게임 이벤트 처리
            game.handle_event(event)
        
        # 게임 업데이트
        game.update()
        
        # 화면 그리기
        screen.fill((0, 0, 0))  # 검은색으로 화면 지우기
        game.draw()
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()