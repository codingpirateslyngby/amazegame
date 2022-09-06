import pygame

class Game_Code:
    def __init__(self, SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/backgorund.png").convert_alpha()
        self.background = pygame.transform.scale(self.image, SCREEN_SIZE)
        self.player = Game_Object("player",64,64) # <-- add player

    def draw(self):
        self.display_surface.blit(self.background, (0, 0))
        self.player.draw(self.display_surface)

# add Game_Object --> 
class Game_Object: # make game obejct
    def __init__(self, name, x, y):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/"+ name + ".png").convert_alpha()
        self.x = x
        self.y = y
    def draw(self, display):
        display.blit(self.image, (self.x, self.y))
# <---