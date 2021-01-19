import pygame

from settings import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class Level():

    def __init__(self):
        self.direction = 0

    def afficher(self, tiles):
        for key, value in enumerate(tiles):
            x = int(value[1]) * SIZE_SPRITE
            y = int(value[0]) * SIZE_SPRITE
            sprite = tiles[value]
            if sprite == " ":
                SCREEN.blit(pygame.image.load(FLOOR_IMG).convert(), (x, y))
            elif sprite == "X":
                SCREEN.blit(pygame.image.load(WALL_IMG).convert(), (x, y))
            elif sprite == "P":
                SCREEN.blit(pygame.image.load(PLAYER_IMG).convert(), (x, y))
            elif sprite == "B":
                SCREEN.blit(pygame.image.load(BAD_GUY_IMAGE).convert(), (x, y))
            elif sprite == "E":
                SCREEN.blit(pygame.image.load(ETHER_IMAGE).convert(), (x, y))
            elif sprite == "T":
                SCREEN.blit(pygame.image.load(TUBE_IMAGE).convert(), (x, y))
            elif sprite == "S":
                SCREEN.blit(pygame.image.load(SERINGE_IMAGE).convert(), (x, y))

    def mouvement(self, x, y):
        for key, value in enumerate(self.tiles):
            x = int(value[1]) * SIZE_SPRITE
            y = int(value[0]) * SIZE_SPRITE
        for event.type in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    y += (1 * SIZE_SPRITE)
                    SCREEN.blit(pygame.image.load(PLAYER_IMG).convert_alpha(), (x, y + 20))
                elif event.key == pygame.K_LEFT:
                    y -= (1 * SIZE_SPRITE)
                    SCREEN.blit(pygame.image.load(PLAYER_IMG).convert_alpha(), (x, y - 20))
                elif event.key == pygame.K_DOWN:
                    x -= (1 * SIZE_SPRITE)
                    SCREEN.blit(pygame.image.load(PLAYER_IMG).convert_alpha(), (x - 20, y))
                elif event.key == pygame.K_UP:
                    x += (1 * SIZE_SPRITE)
                    SCREEN.blit(pygame.image.load(PLAYER_IMG).convert_alpha(), (x + 20, y))
