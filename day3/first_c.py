import pygame

class File_Loader:
    def __init__(self, name):
        self.map_cods = {}
        self.map_cods["1"] = {"name":"wall","codes":[]}
        self.load_map("mapfile")

    def load_map(self,name):
        f = open(name+".txt", "r")
        DATA = f.read().replace("\n", "").split("map:")
        self.MAP_GRID = DATA[0].split(",")
        self.MAP_DATA = DATA[1].split(",")
        f.close()
        self.map_len = int(self.MAP_DATA[0])
