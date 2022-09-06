import pygame
from gameDir import Game_Code

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 896, 896
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Caze Mazeaa")
        self.clock = pygame.time.Clock()
        self.TheGame = Game_Code(SCREEN_SIZE)
        self.debug_init()

    def debug_init(self):
        self.debugStop = False
        self.Freze = False
        self.TakeStep = False

    def debugFreze(self,keys):
        if keys[pygame.K_m]:
            if self.debugStop:
                self.debugStop = False
                self.Freze = self.Freaaaaaaze == False
        else:
            self.debugStop = True

        if self.Freze and not self.TakeStep:
            if keys[pygame.K_n]:
                if self.WhatUdoingstepButten:
                    self.TakeStep = True
                    self.WhatUdoingstepButten = False
            else:
                self.WhatUdoingstepButten = True
            return True
        else:
            self.TakeStep = False
            return False

    def run(self):
        run = True
        while run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.TheGame.move("up")
            if keys[pygame.K_s]:
                self.TheGame.move("down")
            if keys[pygame.K_a]:
                self.TheGame.move("left")
            if keys[pygame.K_d]:
                self.TheGame.move("right")

            if not self.debugFreze(keys):
                self.TheGame.update()

            self.screen.fill("black")
            self.TheGame.draw()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
