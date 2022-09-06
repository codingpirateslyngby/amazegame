import pygame

class Game_Code:
    def __init__(self, SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/backgorund.png").convert_alpha()
        self.background = pygame.transform.scale(self.image, SCREEN_SIZE)
        self.player = Game_Object("player",64,64)

    def draw(self):
        self.display_surface.blit(self.background, (0, 0))
        self.player.draw(self.display_surface)

    # add move and update -->
    def move(self,way):
        if way == "up":
            self.player.speed_y = -3
        if way == "down":
            self.player.speed_y = 3
        if way == "left":
            self.player.speed_x = -3
        if way == "right":
            self.player.speed_x = 3

    def update(self):
        self.player.move()
    # <---

class Game_Object:
    def __init__(self, name, x, y):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/"+name + ".png").convert_alpha()
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.visible = False # <-- add for later

    # add move and update -->
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_x *= 0.97
        self.speed_y *= 0.97
    # <---

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))
