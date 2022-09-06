import pygame
#from gameDir import Game_Code

SCREEN_SIZE = (896, 896)
FPS = 60

MAP_SIZE = 64

f = open("mapfile.txt", "r")
MAP_DATA = f.read().replace("\n", "").split(",")
MAP_GRID = []
# print(f.read())


screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("A Maze Game")
clock = pygame.time.Clock()


class Game_Object:
    def __init__(self, name, x, y):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load(name+".png").convert_alpha()
        self.x = x
        self.y = y
        self.old_x = x
        self.old_y = y
        self.gx = x
        self.gy = y

    def move(self, spx, spy):
        self.old_x = self.x
        self.old_y = self.y
        self.x += spx
        self.y += spy

    def update(self):
        if self.gx < self.x:
            self.gx += 1
        if self.gy < self.y:
            self.gy += 1
        if self.gx > self.x:
            self.gx -= 1
        if self.gy > self.y:
            self.gy -= 1

    def draw(self, map):
        map.blit(self.image, (self.gx, self.gy))


class Game_Code:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("backgorund.png").convert_alpha()
        self.background = pygame.transform.scale(self.image, SCREEN_SIZE)
        self.player = Game_Object("player", 64, 64)
        self.last_input = "none"
        self.map_items = []
        self.offset_x, self.offset_y = (0, 0)
        for itm_y in range(14):
            for itm_x in range(14):
                index = itm_x + itm_y*14

                if MAP_DATA[index] == "1":
                    self.map_items.append(Game_Object(
                        "wall", itm_x*MAP_SIZE, itm_y*MAP_SIZE))
                    MAP_GRID.append(1)
                else:
                    MAP_GRID.append(0)

    def move(self, input):

        if input == "up":
            self.player.move(0, -8)
        if input == "down":
            self.player.move(0, 8)
        if input == "left":
            self.player.move(-8, 0)
        if input == "right":
            self.player.move(8, 0)

        self.last_input = input
        if self.hitwall(self.player):
            self.player.x = self.player.old_x
            self.player.y = self.player.old_y

    def hitwall(self, input):
        xa = int((self.player.x)/64)
        ya = int((self.player.y)/64)*14
        xb = int((self.player.x+60)/64)
        yb = int((self.player.y)/64)*14
        xc = int((self.player.x)/64)
        yc = int((self.player.y+60)/64)*14
        xd = int((self.player.x+60)/64)
        yd = int((self.player.y+60)/64)*14
        #print(((self.player.y/64) % 20)*20)
        if MAP_GRID[xa+ya] + MAP_GRID[xb+yb] + MAP_GRID[xc+yc] + MAP_GRID[xd+yd]:
            return True
        return False

    def update(self):
        self.player.update()

    def draw(self):

        self.display_surface.blit(self.background, (0, 0))
        self.player.draw(self.display_surface)
        for obj in self.map_items:
            obj.draw(self.display_surface)


TheGame = Game_Code()
run = True
while (run):
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            TheGame.move("up")
        if keys[pygame.K_s]:
            TheGame.move("down")
        if keys[pygame.K_a]:
            TheGame.move("left")
        if keys[pygame.K_d]:
            TheGame.move("right")

    TheGame.update()
    screen.fill('black')
    TheGame.draw()
    pygame.display.update()
