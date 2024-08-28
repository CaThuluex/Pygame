import pygame
from pygame.locals import*
from constants import*


pygame.init()


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Control de inicio
running = True
while running:

   #Para salir click en la X de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Background
    screen.fill((0, 0, 0))

    # Player
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 25) #(Color), (Posicion), (Radio del circulo)

    
    pygame.display.flip()


pygame.quit()