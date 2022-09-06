import pygame
from first_b import Game_Code 

SCREEN_SIZE = (896, 896) 

pygame.display.set_caption("Cazy Mazy")

class Game: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.TheGame = Game_Code(SCREEN_SIZE) 

    def run(self):
        run = True
        while run:
            self.clock.tick(60) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            # key press
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.TheGame.move("up")
            if keys[pygame.K_d]:
                self.TheGame.move("right")
            if keys[pygame.K_s]:
                self.TheGame.move("down")
            if keys[pygame.K_a]:
                self.TheGame.move("left")

            self.TheGame.update()
            self.screen.fill("blue") 
            self.TheGame.draw() 
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()