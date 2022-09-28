from operator import truediv
import pygame

pygame.init()

screen_width = 480
screen_height =640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("pygame")
# 배경이미지 불러오기
background = pygame.image.load("background.png")
#screen.fill((255,0,0))
#캐릭터 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size #이미지의크기
character_width = character_size[0] #케릭터의 가로크기
character_height = character_size[1] #케릭터의 세로크기
character_x_pos = screen_width / 2
character_y_pos = screen_height - character_height

    
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    
    screen.blit(background, (0, 0))
    
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update()
    
            
pygame.quit()