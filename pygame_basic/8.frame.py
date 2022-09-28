from operator import truediv
import pygame

pygame.init()

screen_width = 480
screen_height =640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("pygame")

#fps
clock = pygame.time.Clock()

############################################################

#1.사용자게임초기화(배경화면 게임이미지 좌표 속도 폰트등)




running = True #게임이진행중인가?
while running:
    dt = clock.tick(60) # 초당프레임 
    #2.이벤트처리(키보드 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    #3. 게임케릭터 위치정의(+경계값처리)
    
    
    #4.충돌처리
    #5. 화면에서 보여지는 모습
    

    
    
            
pygame.quit()