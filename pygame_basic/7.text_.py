from operator import truediv
import pygame

pygame.init()

screen_width = 480
screen_height =640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("pygame")

#fps
clock = pygame.time.Clock()
# 배경이미지 불러오기
background = pygame.image.load("background.png")
#screen.fill((255,0,0))
#캐릭터 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size #이미지의크기
character_width = character_size[0] #케릭터의 가로크기
character_height = character_size[1] #케릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width /2 )
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0
#이동속도
character_speed = 0.6

#적 enemy케릭터
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size #이미지의크기
enemy_width = enemy_size[0] #케릭터의 가로크기
enemy_height = enemy_size[1] #케릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width /2 )
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)
#폰트정의
game_font=pygame.font.Font(None, 40)

#총시간
total_time=10
#시작시간
start_ticks=pygame.time.get_ticks()

#이벤트루프
running = True #게임이진행중인가?
while running:
    dt = clock.tick(60) # 초당프레임 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x  =0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y  =0
    character_x_pos += to_x *dt
    character_y_pos += to_y *dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width -character_width
        
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height -character_height
    
    #충돌처리
    character_rect = character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos
    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running=false
    
    
    

    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    #타이머집어넣기
    #경과시간계산
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000
    timer=game_font.render(str(int(total_time-elapsed_time)), True, (255,255,255))
    #시간이 0이하면 게임종료
    if total_time -elapsed_time <=0:
        print("타임아웃")
        running=False
    screen.blit(timer,(10,10))
    
    pygame.display.update() #게임화면을 다시그리기
#잠시대기
pygame.time.delay(2000) #2초정도대기
        
    

    
    
            
pygame.quit()