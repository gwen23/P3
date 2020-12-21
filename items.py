import random


class Macgyver:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Guardian:

    def __init__(self, x, y):
        self.x = x
        self.y = y


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
        x, y = 0, 0
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
                y = 0

    def move_macgyver(self, direction):
        if direction == "up":
            # on connait les coordonnées de macgyver
            # on veut trouver les coordonnées de destination
            coo_destination = (self.mac_gyver.x - 1, self.mac_gyver.y)
            # on vérifie que les coo de destination existent
            if self.tiles[coo_destination]:
                # ici je sais que la case existe
                if self.tiles[coo_destination] != "X":
                    # ici je sais que la case n'est pas un mur
                    # je peux bouger Macgyver

                    # changer le contenu de la case où se trouvait macgyver par un chemin
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                    # changer les coordonnées de macgyver
                    self.mac_gyver.x = coo_destination[0]
                    self.mac_gyver.y = coo_destination[1]

                    # il faut vérifier qu'il n'y ait pas d'objet sur la case.
                    # si il y a un objet, on le ramasse
                    if self.tiles[coo_destination] in "TSE":
                        # on ramasse l'objet
                        self.numb_objects += 1

                    # Il faut vérifier qu'il n'y ait pas le gardien sur la
                    # case de destination
                    if self.tiles[coo_destination] == "B":
                        # il y a le gardien :
                        if self.numb_objects == 3:
                            print("you win")
                            # on gagne
                        else:
                            print("you lose")
                            # on perd

                    # changer les coordonnées de macgyver DANS self.tiles
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"
        if direction == "down":
            # on connait les coordonnées de macgyver
            # on veut trouver les coordonnées de destination
            coo_destination = (self.mac_gyver.x + 1, self.mac_gyver.y)
            # on vérifie que les coo de destination existent
            if self.tiles[coo_destination]:
                # ici je sais que la case existe
                if self.tiles[coo_destination] != "X":
                    # ici je sais que la case n'est pas un mur
                    # je peux bouger Macgyver

                    # changer le contenu de la case où se trouvait macgyver par un chemin
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                    # changer les coordonnées de macgyver
                    self.mac_gyver.x = coo_destination[0]
                    self.mac_gyver.y = coo_destination[1]

                    # il faut vérifier qu'il n'y ait pas d'objet sur la case.
                    # si il y a un objet, on le ramasse
                    if self.tiles[coo_destination] in "TSE":
                        # on ramasse l'objet
                        self.numb_objects += 1

                    # Il faut vérifier qu'il n'y ait pas le gardien sur la
                    # case de destination
                    if self.tiles[coo_destination] == "B":
                        # il y a le gardien :
                        if self.numb_objects == 3:
                            print("you win")
                            # on gagne
                        else:
                            print("you lose")
                            # on perd

                    # changer les coordonnées de macgyver DANS self.tiles
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"

        # OK
        if direction == "right":
            # on connait les coordonnées de macgyver
            # on veut trouver les coordonnées de destination
            coo_destination = (self.mac_gyver.x, self.mac_gyver.y + 1)
            # on vérifie que les coo de destination existent
            if self.tiles[coo_destination]:
                # ici je sais que la case existe
                if self.tiles[coo_destination] != "X":
                    # ici je sais que la case n'est pas un mur
                    # je peux bouger Macgyver

                    # changer le contenu de la case où se trouvait macgyver par un chemin
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                    # changer les coordonnées de macgyver
                    self.mac_gyver.x = coo_destination[0]
                    self.mac_gyver.y = coo_destination[1]

                    # il faut vérifier qu'il n'y ait pas d'objet sur la case.
                    # si il y a un objet, on le ramasse
                    if self.tiles[coo_destination] in "TSE":
                        # on ramasse l'objet
                        self.numb_objects += 1

                    # Il faut vérifier qu'il n'y ait pas le gardien sur la
                    # case de destination
                    if self.tiles[coo_destination] == "B":
                        # il y a le gardien :
                        if self.numb_objects == 3:
                            print("you win")
                            # on gagne
                        else:
                            print("you lose")
                            # on perd

                    # changer les coordonnées de macgyver DANS self.tiles
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"

        if direction == "left":
            # on connait les coordonnées de macgyver
            # on veut trouver les coordonnées de destination
            coo_destination = (self.mac_gyver.x, self.mac_gyver.y - 1)
            # on vérifie que les coo de destination existent
            if self.tiles[coo_destination]:
                # ici je sais que la case existe
                if self.tiles[coo_destination] != "X":
                    # ici je sais que la case n'est pas un mur
                    # je peux bouger Macgyver

                    # changer le contenu de la case où se trouvait macgyver par un chemin
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = " "
                    # changer les coordonnées de macgyver
                    self.mac_gyver.x = coo_destination[0]
                    self.mac_gyver.y = coo_destination[1]

                    # il faut vérifier qu'il n'y ait pas d'objet sur la case.
                    # si il y a un objet, on le ramasse
                    if self.tiles[coo_destination] in "TSE":
                        # on ramasse l'objet
                        self.numb_objects += 1

                    # Il faut vérifier qu'il n'y ait pas le gardien sur la
                    # case de destination
                    if self.tiles[coo_destination] == "B":
                        # il y a le gardien :
                        if self.numb_objects == 3:
                            print("you win")
                            # on gagne
                        else:
                            print("you lose")
                            # on perd

                    # changer les coordonnées de macgyver DANS self.tiles
                    self.tiles[(self.mac_gyver.x, self.mac_gyver.y)] = "P"

    def create_objects(self):
        # créer 3 objets
        # Pour les créer :
        # définir les 3 objets
        # Leur attribuer une position dans le labyrinthe (sur les chemins uniquement)
        # Il faut donc se servir de la liste des chemins.
        # Pour l'aléatoire, on utilise random.shuffle()
        # on attribue les 3 premières valeurs aux 3 objets
        objects = ["E", "T", "S"]
        random.shuffle(self.paths)
        for i in range(0, 3):
            # objects[i] # 0 => E
            # objects[i] # 1 => T
            # objects[i] # 2 => S
            # self.paths[i] # i = 0 => coordonnées
            # self.paths[i] # i = 1 => coordonnées
            # self.paths[i] # i = 2 => coordonnées
            coo_nouvel_obj = self.paths[i]  # coordonnées de placement des objets
            self.tiles[coo_nouvel_obj] = objects[i]  # définition de l'objet dans les tiles, aux coordonnées aléatoires


if __name__ == "__main__":
    maze = Maze()
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 2, 1
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 2, 2
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 2, 3
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 2, 4
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 2, 5
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 3, 5
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 4, 5
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 5, 5
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 6, 5
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 7, 5
    maze.move_macgyver("left")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 7, 4
    maze.move_macgyver("left")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 7, 3
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 8, 3
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 9, 3
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 10, 3
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 11, 3
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 11, 4
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 11, 5
    maze.move_macgyver("up")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 10, 5
    maze.move_macgyver("up")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 9, 5
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 9, 6
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 9, 7
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 9, 8
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 10, 8
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 11, 8
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 11, 9
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 12, 9
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 13, 9
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 14, 9
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 14, 10
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 14, 11
    maze.move_macgyver("up")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 13, 11
    maze.move_macgyver("up")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 12, 11
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 12, 12
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 12, 13
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 13, 13
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 13 ,14
    maze.move_macgyver("down")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 14, 14
    maze.move_macgyver("right")
    print(maze.mac_gyver.x, maze.mac_gyver.y)
    # 14, 15



