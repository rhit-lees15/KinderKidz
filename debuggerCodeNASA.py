# Welcome to KiNderKidz
# i am raspberry pi
import pygame
 
# initialize pygame
pygame.init()
screen_size = (700, 500)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Kinder Kidz")
 
# clock is used to set a max fps
clock = pygame.time.Clock()
 
# create a demo surface, and draw a red line diagonally across it
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill((255, 255, 255))

    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render('CAT', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (screen_size[0]//2, screen_size[1]//2)
    
    screen.blit(text, textRect)
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()