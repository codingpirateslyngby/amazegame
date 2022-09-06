import pygame
from second_c import File_Loader 

class Game_Code:
    def __init__(self, SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/backgorund.png").convert_alpha()
        self.background = pygame.transform.scale(self.image, SCREEN_SIZE)
        self.player = Game_Object("player",64,64) 
        self.map_loader = File_Loader("mapfile")
        self.create_map()

    def create_map(self):
        self.map_draws = []
        self.map_items = {}
        map_len = self.map_loader.map_len
        self.MAP_GRID = self.map_loader.MAP_GRID
        for index,value in enumerate(self.MAP_GRID):
            if value == "0" or index == len(self.MAP_GRID)-1:
                continue
            blue_print = self.map_loader.map_cods[value]
            obj = Game_Object(blue_print["name"], int(index % map_len) * 64, int(index / map_len) * 64)
            # move: self.map_draws.append(obj)
            # add ---->
            for i,codes in enumerate(blue_print["codes"]):
                if i == 0:
                    for obj_data in codes.split(":"):
                        if obj_data == "d":
                            self.map_draws.append(obj) #<--- to here
                        if obj_data == "i":
                            self.map_items[index] = obj
                        if obj_data == "h":
                            obj.visible = False
                else:
                    obj.data.append(codes)
            # <----
    def draw(self):
        self.display_surface.blit(self.background, (0, 0))
        self.player.draw(self.display_surface)
        for obj in self.map_draws:
            obj.draw(self.display_surface)
        

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
        self.player.move(self.MAP_GRID)


class Game_Object:
    def __init__(self, name, x, y):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/"+name + ".png").convert_alpha()
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.visible = False
        self.points = [(0.2,0.2),(1.8,0.2),(1.8,1.8),(0.2,1.8)] # <-- add  points
        self.data = [] # <-- add data for later

    def move(self,MAP_GRID):
        self.x += self.speed_x
        self.y += self.speed_y
        self.can_stand(MAP_GRID)
        self.speed_x *= 0.2
        self.speed_y *= 0.2

    def can_stand(self,MAP_GRID):
        for point in self.points: # <-- add  points
            gx = int((point[0]*32+self.x) / 64) # <-- add  point[0]
            gy = int((point[1]*32+self.y) / 64) # <-- add  point[1]
            if MAP_GRID[gx+gy*14] == "1":
                self.x -= self.speed_x
                self.y -= self.speed_y
                self.speed_x = 0
                self.speed_y = 0

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))
