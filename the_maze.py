import random
from guardian import Guardian
from player import Macgyver


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
        with open("maze.txt", "r") as maze:
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
        if direction == "up":
            coo_destination = (self.mac_gyver.x - 1, self.mac_gyver.y)
            if self.tiles[coo_destination]:
                if self.tiles[coo_destination] != "X":
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                    self.mac_gyver.x = coo_destination[0]
                    self.mac_gyver.y = coo_destination[1]
                    if self.tiles[coo_destination] in "TSE":
                        self.numb_objects += 1
                    if self.tiles[coo_destination] == "B":
                        if self.numb_objects == 3:
                            print("you win")
                        else:
                            print("you lose")
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"
                    return True

        if direction == "down":
            coo_destination = (self.mac_gyver.x + 1, self.mac_gyver.y)
            if self.tiles[coo_destination]:
                if self.tiles[coo_destination] != "X":
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                    self.mac_gyver.x = coo_destination[0]
                    self.mac_gyver.y = coo_destination[1]
                    if self.tiles[coo_destination] in "TSE":
                        self.numb_objects += 1
                    if self.tiles[coo_destination] == "B":
                        if self.numb_objects == 3:
                            print("you win")
                        else:
                            print("you lose")
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"
                    return True

        if direction == "right":
            coo_destination = (self.mac_gyver.x, self.mac_gyver.y + 1)
            if self.tiles[coo_destination]:
                if self.tiles[coo_destination] != "X":
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                    self.mac_gyver.x = coo_destination[0]
                    self.mac_gyver.y = coo_destination[1]
                    if self.tiles[coo_destination] in "TSE":
                        self.numb_objects += 1
                    if self.tiles[coo_destination] == "B":
                        if self.numb_objects == 3:
                            print("you win")
                        else:
                            print("you lose")
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"
                    return True

        if direction == "left":
            coo_destination = (self.mac_gyver.x, self.mac_gyver.y - 1)
            if self.tiles[coo_destination]:
                if self.tiles[coo_destination] != "X":
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                    self.mac_gyver.x = coo_destination[0]
                    self.mac_gyver.y = coo_destination[1]
                    if self.tiles[coo_destination] in "TSE":
                        self.numb_objects += 1
                    if self.tiles[coo_destination] == "B":
                        if self.numb_objects == 3:
                            print("you win")
                        else:
                            print("you lose")
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"
                    return True
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
            coo_nouvel_obj = self.paths[i]
            self.tiles[coo_nouvel_obj] = objects[i]
