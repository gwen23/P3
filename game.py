import pygame

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

# Path for the different sources of the game
PLAYER_IMAGE = "images/MacGyver.png"
BAD_GUY_IMAGE = "images/Gardien.png"
WALL_IMAGES = "images/structures.png"
FLOOR_IMAGES = "images/floor-tiles-20x20.png"
ETHER_IMAGE = "images/ether.png"
TUBE_IMAGE = "images/tube_plastique.png"
SERINGE_IMAGE = "images/seringue.png"


pygame.init()

WIDTH = 300
HEIGHT = 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
fond = pygame.image.load("images/floor-tiles-20x20.png").convert_alpha()
SCREEN.blit(fond, (0, 0))
pygame.display.set_caption('The Maze')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

SCREEN.fill(BLUE)

MAZE_IMG = pygame.image.load("images/floor-tiles-20x20.png").convert_alpha()
WALL_IMG = pygame.image.load('images/structures.png').convert_alpha()
PLAYER_IMG = pygame.image.load("images/MacGyver.png").convert_alpha()


class CreateGame(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300

        x, y = 0, 0
        with open("maze.txt", "r") as maze:
            for line in maze:
                x += 1
                for cell in line:
                    if cell != "\n":
                        y += 1
                        self.tiles[(x, y)] = cell
                    if cell == " ":
                        self.tiles[(x, y)] = MAZE_IMG
                        tiles.blit(MAZE_IMG, (20 * x, 20 * y))
                    if cell == "P":
                        self.tiles[(x, y)] = PLAYER_IMAGE
                        tiles.blit(PLAYER_IMG, (20 * x, 20 * y))
                    if cell == "B":
                        self.tiles[(x, y)] = BAD_GUY_IMAGE
                        tiles.blit(BAD_GUY_IMG, (20 * x, 20 * y))
                    if cell == "X":
                        self.tiles[(x, y)] = WALL_IMG
                        tiles.blit(WALL_IMG, (20 * x, 20 * y))
                    if cell == "E":
                        self.tiles[(x, y)] = ETHER_IMAGE
                        tiles.blit(ETHER_IMAGE, (20 * x, 20 * y))
                    if cell == "T":
                        self.tiles[(x, y)] = TUBE_IMAGE
                        tiles.blit(TUBE_IMAGE, (20 * x, 20 * y))
                    if cell == "S":
                        self.tiles[(x, y)] = SERINGE_IMAGE
                        tiles.blit(SERINGE_IMAGE, (20 * x, 20 * y))
                y = 0


pygame.display.flip()


is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

pygame.quit()
