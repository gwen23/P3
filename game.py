import pygame


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
fond = pygame.image.load("images/floor-tiles-20x20.png").convert()
SCREEN.blit(fond, (0, 0))
pygame.display.set_caption('The Maze')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

SCREEN.fill(BLUE)


class Maze:
    maze = pygame.image.load("images/floor-tiles-20x20.png").convert()
    wall = pygame.image.load('images/structures.png').convert()


class Macgyver:
    player = pygame.image.load("images/MacGyver.png").convert_alpha()


pygame.display.flip()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

pygame.quit()
