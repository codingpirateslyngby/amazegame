import pygame
from first_c import File_Loader 

class Game_Code:
    def __init__(self, SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/backgorund.png").convert_alpha()
        self.background = pygame.transform.scale(self.image, SCREEN_SIZE)
        self.player = Game_Object("player",64,64) 
        self.map_loader = File_Loader("mapfile") # <-- add map_loader
        self.create_map() # <-- add map_loader

    # <-- add map_loader
    def create_map(self):
        self.map_draws = []
        self.map_items = {}
        map_len = self.map_loader.map_len
        self.MAP_GRID = self.map_loader.MAP_GRID
        for index,value in enumerate(self.MAP_GRID):
            if value != "1" or index == len(self.MAP_GRID)-1:
                continue
            blue_print = self.map_loader.map_cods[value]
            obj = Game_Object(blue_print["name"], int(index % map_len) * 64, int(index / map_len) * 64)
            self.map_draws.append(obj)
    # -->

    def draw(self):
        self.display_surface.blit(self.background, (0, 0))
        self.player.draw(self.display_surface)
        for obj in self.map_draws:  # <-- add wall draw
            obj.draw(self.display_surface) # <-- add wall draw


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
        self.player.move(self.MAP_GRID) # <-- add self.map_grid

class Game_Object:
    def __init__(self, name, x, y):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/"+name + ".png").convert_alpha()
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.visible = False

    def move(self,MAP_GRID): # <--- add MAP_GRID
        self.x += self.speed_x
        self.y += self.speed_y
        self.can_stand(MAP_GRID) # <--- add can stand
        self.speed_x *= 0.97
        self.speed_y *= 0.97

    # add can_stand --->
    def can_stand(self,MAP_GRID):
        gx = int((32+self.x) / 64)
        gy = int((32+self.y) / 64)
        if MAP_GRID[gx+gy*14] == "1":
            self.x -= self.speed_x
            self.y -= self.speed_y
            self.speed_x = 0
            self.speed_y = 0
    # <---

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))
