import pygame

from pygame.locals import *

from items import Maze, Guardian, Macgyver


""" Different constants of the game """

# String to identify each character in level structure
PLAYER_STRIPE = "P"
BAD_GUY_STRIPE = "B"
ETHER_STRIPE = "E"
TUBE_STRIPE = "T"
SERINGE_STRIPE = "S"
WALL_STRIPE = "X"
FLOOR_STRIPE = " "

pygame.init()
clock = pygame.time.Clock()

WIDTH = 300
HEIGHT = 300
size_sprite = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fond = pygame.image.load("./images/floor-tiles-20x20.png").convert()
pygame.display.set_caption('The Maze')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

FLOOR_IMG = pygame.image.load("./images/floor-tiles-20x20.png").convert()
WALL_IMG = pygame.image.load("./images/structures.png").convert()
ETHER_IMAGE = pygame.image.load("./images/ether.png").convert_alpha()
TUBE_IMAGE = pygame.image.load("./images/tube_plastique.png").convert_alpha()
SERINGE_IMAGE = pygame.image.load("./images/seringue.png").convert_alpha()
BAD_GUY_IMAGE = pygame.image.load("./images/Gardien.png").convert_alpha()

PLAYER_IMG = pygame.image.load("./images/MacGyver.png").convert_alpha()
player_img = pygame.Rect(0, 20, 20, 20)

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


level = Level()
is_running = True
screen.blit(fond, (0, 0))
level.afficher()
# Dans pygame
while is_running:
    clock.tick(5)
    x = 0
    y = 20
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT:
                screen.blit(FLOOR_IMG, (x, y))
                x += 1 * size_sprite
                screen.blit(PLAYER_IMG, (x, y))
            elif event.key == pygame.K_LEFT:
                screen.blit(FLOOR_IMG, (x, y))
                x -= 1 * size_sprite
                screen.blit(PLAYER_IMG, (x, y))
            elif event.key == pygame.K_UP:
                screen.blit(FLOOR_IMG, (x, y))
                y -= 1 * size_sprite
                screen.blit(PLAYER_IMG, (x, y))
            elif event.key == pygame.K_DOWN:
                screen.blit(FLOOR_IMG, (x, y))
                y += 1 * size_sprite
                screen.blit(PLAYER_IMG, (x, y))
        if event.type == pygame.QUIT:
            is_running = False
    pygame.display.update()

pygame.quit()
