""" Different constants of the game """
import pygame
from pygame.locals import *

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