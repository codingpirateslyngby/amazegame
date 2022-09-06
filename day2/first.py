import pygame

SCREEN_SIZE = (896, 896) 

pygame.display.set_caption("Cazy Mazy")

# TheGame
class Game_Code:
    def __init__(self, SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/backgorund.png").convert_alpha() # <-- set background to image
        self.background = pygame.transform.scale(self.image, SCREEN_SIZE) # <-- add transform on image

    def draw(self):
        self.display_surface.blit(self.background, (0, 0))


class Game: # <-- add class Game
    def __init__(self): # <-- add init
        pygame.init()  # <-- add init
        self.screen = pygame.display.set_mode(SCREEN_SIZE) # <-- add self.
        self.clock = pygame.time.Clock() # <-- add self.
        self.TheGame = Game_Code(SCREEN_SIZE) # <-- add self.

    def run(self): # <-- add run
        run = True
        while run:
            self.clock.tick(60) # <-- add self.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                # key press
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.screen.fill("blue") # <-- add self.
                    self.TheGame.draw() # <-- add self.
                    pygame.display.update()

# add __main__ --->
if __name__ == "__main__":
    game = Game()
    game.run()
# <-- 