import pygame
from filemanger import File_Loader
from game_menu import GameMenu 

class Game_Code:
    def __init__(self, SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/backgorund.png").convert_alpha()
        self.background = pygame.transform.scale(self.image, SCREEN_SIZE)
        self.player = Game_Object("player",64,64)
        self.gamestate = "menu"
        self.key = "none"
        self.menu = GameMenu(SCREEN_SIZE)

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

            for i,codes in enumerate(blue_print["codes"]):
                if i == 0:
                    for obj_data in codes.split(":"):
                        if obj_data == "d":
                            self.map_draws.append(obj)
                        if obj_data == "i":
                            self.map_items[index] = obj
                        if obj_data == "h":
                            obj.visible = False
                        
                else:
                    obj.data.append(codes)
    def draw(self):
        if self.gamestate == "menu":
            self.menu.draw()
            return
        self.display_surface.blit(self.background, (0, 0))
        for obj in self.map_draws:
            obj.draw(self.display_surface)
        self.player.draw(self.display_surface) # <--- swap this to front

        
    def move(self,way):
        self.key = way
        if way == "up":
            self.player.speed_y = -3
        if way == "down":
            self.player.speed_y = 3
        if way == "left":
            self.player.speed_x = -3
        if way == "right":
            self.player.speed_x = 3


    def update(self):
        if self.gamestate == "menu":
            self.menu.update(self.key)
            self.key = "none"
        if self.gamestate == "begin":
            self.map_loader = File_Loader("mapfile")
            self.create_map()
            self.player.x = 64
            self.player.y = 64
            self.player.visible = True
            self.gamestate = "main"
        if self.gamestate == "main":
            self.player.move(self.MAP_GRID)
            if self.player.Trigger != -1:
                if self.player.Trigger < 0:
                    self.player.x = -100
                    self.player.y = -100
                    self.player.visible = False
                    self.player.Trigger -= 1
                    if self.player.Trigger < -20:
                        self.menu.level = 1
                        self.gamestate = "menu"
                        self.player.Trigger = -1
                    return
                for i,obj_data in enumerate(self.map_items[self.player.Trigger].data):
                    val = obj_data.split(":")
                    self.MAP_GRID[int(val[0])] = val[1]
                self.MAP_GRID[self.player.Trigger] = "0"
                self.create_map()
                self.player.Trigger = -1

class Game_Object:
    def __init__(self, name, x, y):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/"+name + ".png").convert_alpha()
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.visible = True
        self.points = [(0.2,0.2),(1.8,0.2),(1.8,1.8),(0.2,1.8)]
        self.data = []
        self.Trigger = -1

    def move(self,MAP_GRID):
        self.x += self.speed_x
        self.y += self.speed_y
        self.can_stand(MAP_GRID)
        self.speed_x *= 0.2
        self.speed_y *= 0.2

    def can_stand(self,MAP_GRID):
        for point in self.points:
            gx = int((point[0]*32+self.x) / 64)
            gy = int((point[1]*32+self.y) / 64)
            i = gx+gy*14
            if MAP_GRID[i] == "1":
                self.x -= self.speed_x
                self.y -= self.speed_y
                self.speed_x = 0
                self.speed_y = 0
            if MAP_GRID[i] == "2": 
                self.Trigger = i 
            if MAP_GRID[i] == "v":
                self.Trigger = -2


    def draw(self, display):
        if not self.visible:
            return
        display.blit(self.image, (self.x, self.y))
