import pygame

pygame.display.set_caption("Cazy Mazy")
screen = pygame.display.set_mode((896, 896))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        # add key press -->
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            screen.fill("blue")
            pygame.display.update()
        # <--