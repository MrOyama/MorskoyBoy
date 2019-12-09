import pygame

pygame.init()

screen = pygame.display.set_mode([1000, 700])
pygame.display.set_caption("MorskoyBoy")
clock = pygame.time.Clock()
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill([255, 255, 255])
    for y_offset in range(0, 200, 20):
        pygame.draw.line(screen, [80, 80, 80], [140, 200 + y_offset], [340, 200 + y_offset], 2)
        pygame.draw.line(screen, [80, 80, 80], [140 + y_offset, 200], [140 + y_offset, 400], 2)
    pygame.draw.line(screen, [80, 80, 80], [140, 400], [340, 400], 2)
    pygame.draw.line(screen, [80, 80, 80], [340, 200], [340, 400], 2)
    for y_offset in range(0, 200, 20):
        pygame.draw.line(screen, [80, 80, 80], [660, 200 + y_offset], [860, 200 + y_offset], 2)
        pygame.draw.line(screen, [80, 80, 80], [660 + y_offset, 200], [660 + y_offset, 400], 2)
    pygame.draw.line(screen, [80, 80, 80], [660, 400], [860, 400], 2)
    pygame.draw.line(screen, [80, 80, 80], [860, 200], [860, 400], 2)

    pygame.display.update()
    clock.tick(60)


pygame.quit()

