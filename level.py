from the_maze import Maze
from settings import *


class Level(Maze):

    def __init__(self):
        Maze.__init__(self)
        self.direction = 0
        # self.tiles => est disponible

    def afficher(self):
        for key, value in enumerate(self.tiles):
            x = int(value[1]) * size_sprite
            y = int(value[0]) * size_sprite
            sprite = self.tiles[value]
            if sprite == " ":
                screen.blit(FLOOR_IMG, (x, y))
            elif sprite == "X":
                screen.blit(WALL_IMG, (x, y))
            elif sprite == "P":
                screen.blit(PLAYER_IMG, (x, y))
            elif sprite == "B":
                screen.blit(BAD_GUY_IMAGE, (x, y))
            elif sprite == "E":
                screen.blit(ETHER_IMAGE, (x, y))
            elif sprite == "T":
                screen.blit(TUBE_IMAGE, (x, y))
            elif sprite == "S":
                screen.blit(SERINGE_IMAGE, (x, y))

    def mouvement(self, x, y):
        for key, value in enumerate(self.tiles):
            x = int(value[1]) * size_sprite
            y = int(value[0]) * size_sprite
        for event.type in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    y += (1 * size_sprite)
                    screen.blit(PLAYER_IMG, (x, y + 20))
                elif event.key == pygame.K_LEFT:
                    y -= (1 * size_sprite)
                    screen.blit(PLAYER_IMG, (x, y - 20))
                elif event.key == pygame.K_DOWN:
                    x -= (1 * size_sprite)
                    screen.blit(PLAYER_IMG, (x - 20, y))
                elif event.key == pygame.K_UP:
                    x += (1 * size_sprite)
                    screen.blit(PLAYER_IMG, (x + 20, y))


