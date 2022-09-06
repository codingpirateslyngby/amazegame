import pygame


MAP_SIZE = 64

class Game_Code:
    def __init__(self, SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("backgorund.png").convert_alpha()
        self.background = pygame.transform.scale(self.image, SCREEN_SIZE)
        
        self.dir = "none"
        self.loaded = False
        self.read_start = self.load_map("mapfile")
        self.create_map()

        self.player = Game_Object("player", MAP_SIZE, MAP_SIZE,0,0)

    def load_map(self,name):
        f = open(name+".txt", "r")
        DATA = f.read().replace("\n", "").split("map:")
        self.MAP_GRID = DATA[0].split(",")
        self.MAP_DATA = DATA[1].split(",")
        f.close()
        self.map_len = int(self.MAP_DATA[0])
        self.map_cods = {}
        self.map_cods["0"] = {"name":"wall","codes":[]}
        for index,data in enumerate(self.MAP_DATA):
            if index == 0:
                continue
            code_name = data.split("<")
            val = code_name[0].split(":")
            self.map_cods[val[0]] = {"name":val[1],"codes":code_name[1].split(">")}

    def create_map(self):
        self.map_draws = []
        self.map_items = {}
        for index,value in enumerate(self.MAP_GRID):
            if value == "0" or index == len(self.MAP_GRID)-1:
                continue
            blue_print = self.map_cods[value]
            print(blue_print["name"])
            obj = Game_Object(blue_print["name"], int(index % self.map_len) * MAP_SIZE, int(index / self.map_len) * MAP_SIZE)
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
                
        self.loaded = True
    def update(self):
        if not self.loaded:
            return
        self.player.move(self.dir,self.MAP_GRID)
        self.dir = "none"
        if self.player.Trigger != -1:

            for i,obj_data in enumerate(self.map_items[self.player.Trigger].data):
                val = obj_data.split(":")
                self.MAP_GRID[int(val[0])] = val[1]
                print(obj_data)
            self.MAP_GRID[self.player.Trigger] = "0"
            self.create_map()
            self.player.Trigger = -1

    def move(self, input):
        self.dir = input

    def draw(self):
        if not self.loaded:
            return
        self.display_surface.blit(self.background, (0, 0))
        self.player.draw(self.display_surface)
        for obj in self.map_draws:
            obj.draw(self.display_surface)


class Game_Object:
    def __init__(self, name, x, y,off_x = 0,off_y = 0):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load(name + ".png").convert_alpha()
        self.x = x
        self.y = y
        self.points = [(0.1,0.1),(0.9,0.1),(0.9,0.9),(0.1,0.9)]
        #(0.5,0.1),(0.5,0.9),(0.1,0.5),(0.9,0.5)
        self.grid_x = 1
        self.grid_y = 1
        self.off_x = off_x
        self.off_y = off_y
        self.index = 15
        #self.current_index = 15
        self.speed = 4
        self.dirx = 0
        self.diry = 0
        self.Trigger = -1
        self.life = 100
        self.visible = True
        self.data = []


    def move(self, dir, MAP_GRID):
        self.index = self.grid_x + self.grid_y * 14
        #if self.index>=0 and self.index<len(MAP_GRID) and MAP_GRID[self.index] == 0:
        #    self.current_index = self.index

        self.dirx = 0
        self.diry = 0
        if dir == "up":
            self.diry = -self.speed
        if dir == "down":
            self.diry = self.speed
        if dir == "left":
            self.dirx = -self.speed
        if dir == "right":
            self.dirx = self.speed

        self.x += self.dirx
        self.y += self.diry
        self.can_stand(MAP_GRID)

    def can_stand(self,MAP_GRID):
        for pp in self.points:
            x = int((64*pp[0]+self.x) / 64)
            y = int((64*pp[1]+self.y) / 64)
            i = x+y*14
            if MAP_GRID[i] == "1":
                self.x -= self.dirx*1.1
                self.y -= self.diry*1.1
            if MAP_GRID[i] == "2":
                self.Trigger = i

    def draw(self, map):
        if self.visible:
            map.blit(self.image, (self.x+self.off_x, self.y+self.off_y))
