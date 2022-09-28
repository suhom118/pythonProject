from operator import truediv
import pygame

pygame.init()

screen_width = 480
screen_height =640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("pygame")

background = pygame.image.load("./background.png")
#screen.fill((255,0,0))
    
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    screen.blit(background, (0,0))
    
            
pygame.quit()