import pygame

SCREEN_SIZE = (896, 896) # <--- add variable

pygame.display.set_caption("Cazy Mazy")
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


# add class -->
class Game_Code:
    def __init__(self, SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.background = pygame.image.load("./img/backgorund.png").convert_alpha()

    def draw(self):
        self.display_surface.blit(self.background, (0, 0))

TheGame = Game_Code(SCREEN_SIZE)
# <---

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        # key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            screen.fill("blue")
            TheGame.draw()  # <-- add draw()
            pygame.display.update()
            