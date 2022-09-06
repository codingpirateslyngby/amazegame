import pygame

class GameMenu:
    def __init__(self,SCREEN_SIZE):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load("./img/menu_bg.png").convert_alpha()
        #self.background = pygame.transform.scale(self.image, SCREEN_SIZE)
        self.size = SCREEN_SIZE
        #self.txt_rect = pygame.Rect(self.size[0]*0.1,self.size[1]*0.33,self.size[0]*0.75,self.size[1]*0.3)
        #self.bt_rect = pygame.Rect(self.size[0]*0.1,self.size[1]*0.33,self.size[0]*0.75,self.size[1]*0.2)
        self.bt_color = '#71ddee'
        self.bt_shadow = '#31adae'
        self.font = pygame.font.Font('./font/joystix.ttf',28)
        self.buttons = [{"text":"Exit Game","x":0.1,"y":0.1},{"text":"Start Game","x":0.1,"y":0.15},{"text":"Resume Game","x":0.1,"y":0.15}]
        self.sellected = 1
        self.sell = 10
        self.level = 1

    def start(self):
        pass
    def draw_button(self,x,y,text,hasborder):
        if hasborder:
            bt_rect_shad = pygame.Rect(self.size[0]*x+10,self.size[1]*y+10,self.size[0]*0.75,self.size[1]*0.07)
            pygame.draw.rect(self.display_surface,self.bt_shadow,bt_rect_shad)
        bt_rect = pygame.Rect(self.size[0]*x,self.size[1]*y,self.size[0]*0.75,self.size[1]*0.07)
        #txt_rect = pygame.Rect(self.size[0]*x,self.size[1]*y,self.size[0]*0.75,self.size[1]*0.08)
        pygame.draw.rect(self.display_surface,self.bt_color,bt_rect)
        text_surf = self.font.render(text,False,'#111111')
        self.display_surface.blit(text_surf,bt_rect)
        


    def draw(self):
        self.display_surface.blit(self.image, (0, 0))
        yy = 0
        for i,bt in enumerate(self.buttons):
            if i > self.level:
                return
            self.draw_button(bt["x"],yy+bt["y"],bt["text"],i == self.sellected)
            yy += bt["y"]
        

    def update(self,dir):
        if dir == "space":
            return
        if dir == "up":
            self.sell += 1
            if self.sell > self.level*10+9:
                self.sell = 0
        if dir == "down":
            self.sell -= 1
            if self.sell < 0:
                self.sell = self.level*10+9
        self.sellected = int(self.sell / 10)
        #for i in range(3):
        #    self.size
        #    pygame.draw.rect