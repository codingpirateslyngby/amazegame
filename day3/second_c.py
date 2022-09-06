import pygame

class File_Loader:
    def __init__(self, name):
        self.map_cods = {}
        # remove self.map_cods["1"] = {"name":"wall","codes":[]}
        self.add_code(("0","wall"),[]) # <-- add
        self.load_map("mapfile")

    # add codes --->
    def add_code(self,index_name,code):
        self.map_cods[index_name[0]] = {"name":index_name[1],"codes":code}
    # <---

    def load_map(self,name):
        f = open(name+".txt", "r")
        DATA = f.read().replace("\n", "").split("map:")
        self.MAP_GRID = DATA[0].split(",")
        self.MAP_DATA = DATA[1].split(",")
        f.close()
        self.map_len = int(self.MAP_DATA[0])
        # add codes --->
        for index,data in enumerate(self.MAP_DATA):
            if index == 0:
                continue
            code_name = data.split("<")
            val = code_name[0].split(":")
            self.add_code(val,code_name[1].split(">"))
        # <----