import random
from game.guardian import Guardian
from game.player import Macgyver


class Maze:

    def __init__(self):
        self.tiles = {}
        self.paths = []
        self.mac_gyver = ()
        self.guardian = ()
        self.test()
        self.create_objects()
        self.numb_objects = 0

    def test(self):
        x, y = -1, -1
        with open("game/maze.txt", "r") as maze:
            for line in maze:
                x += 1
                for cell in line:
                    if cell != "\n":
                        y += 1
                        self.tiles[(x, y)] = cell
                    if cell == " ":
                        self.paths.append((x, y))
                    if cell == "P":
                        self.mac_gyver = Macgyver(x, y)
                    if cell == "B":
                        self.guardian = Guardian(x, y)
                y = -1

    def move_macgyver(self, direction):
        coo_destination = (self.mac_gyver.x, self.mac_gyver.y)
        if direction == "up":
            coo_destination = (self.mac_gyver.x - 1, self.mac_gyver.y)
        if direction == "down":
            coo_destination = (self.mac_gyver.x + 1, self.mac_gyver.y)
        if direction == "right":
            coo_destination = (self.mac_gyver.x, self.mac_gyver.y + 1)
        if direction == "left":
            coo_destination = (self.mac_gyver.x, self.mac_gyver.y - 1)
        self.conditions(coo_destination)
        if self.tiles[coo_destination] != "X":
            return True
        else:
            return False

    def conditions(self, coo_destination):
        if self.tiles[coo_destination]:
            if self.tiles[coo_destination] != "X":
                self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                self.mac_gyver.x = coo_destination[0]
                self.mac_gyver.y = coo_destination[1]
                if self.tiles[coo_destination] in "TSE":
                    self.numb_objects += 1
                    print("object + 1")
                if self.tiles[coo_destination] == "B":
                    if self.numb_objects == 3:
                        print("you win")
                    else:
                        print("you lose")
                self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"
                return True

    def create_objects(self):
        objects = ["E", "T", "S"]
        random.shuffle(self.paths)
        for i in range(0, 3):
            coo_new_obj = self.paths[i]
            self.tiles[coo_new_obj] = objects[i]
