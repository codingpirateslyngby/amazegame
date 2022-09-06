import pygame
from second_b import Game_Code  # <-- add file

SCREEN_SIZE = (896, 896) 

pygame.display.set_caption("Cazy Mazy")

# remove TheGame
#class Game_Code:
#    def __init__(self, SCREEN_SIZE):
#        self.display_surface = pygame.display.get_surface()
#        self.image = pygame.image.load("backgorund.png").convert_alpha() # <-- set background to image
#        self.background = pygame.transform.scale(self.image, SCREEN_SIZE) # <-- add transform on image

#    def draw(self):
#        self.display_surface.blit(self.background, (0, 0))


class Game: 
    def __init__(self): 
        pygame.init() 
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.TheGame = Game_Code(SCREEN_SIZE) 

    def run(self): # <-- add run
        run = True
        while run:
            self.clock.tick(60) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            # key press
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.screen.fill("blue") 
                self.TheGame.draw() 
                pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()