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
                    return True

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
                    return True
        return False

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
