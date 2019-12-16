import pygame

#Окно и рабочая область
Game_Window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sea battel')
screen = pygame.Surface((800, 600))


#Неабходимые цвета
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Необходимые переменные
square_BLACK = pygame.Surface((16, 16))
square_BLACK.fill(BLACK)

square_RED = pygame.Surface((16, 16))
square_RED.fill(RED)


Close_Game_Window = True
while Close_Game_Window:
    for exit in pygame.event.get():
        if exit.type == pygame.QUIT:
            Close_Game_Window = False

    screen.fill(GREY)

    Viev_x_1 = 10
    Viev_y_1 = 10

    for x in range(10):
        Viev_y_1 = 10
        for y in range(10):
            screen.blit(square_BLACK, (Viev_x_1, Viev_y_1))
            Viev_y_1 += 17
        Viev_x_1 += 17

    Viev_x_2 = 620
    Viev_y_2 = 10

    for x in range(10):
        Viev_y_2 = 10
        for y in range(10):
            screen.blit(square_RED, (Viev_x_2, Viev_y_2))
            Viev_y_2 += 17
        Viev_x_2 += 17

    Game_Window.blit(screen, (0, 0))
    pygame.display.flip()
