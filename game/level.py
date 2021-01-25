import pygame as pg

from game.settings import *

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))


class Level:
    def __init__(self):
        self.direction = 0

    def display(self, tiles):
        for key, value in enumerate(tiles):
            x = int(value[1]) * SIZE_SPRITE
            y = int(value[0]) * SIZE_SPRITE
            sprite = tiles[value]
            if sprite == " ":
                SCREEN.blit(pg.image.load(FL).convert(), (x, y))
            elif sprite == "X":
                SCREEN.blit(pg.image.load(WA).convert(), (x, y))
            elif sprite == "P":
                SCREEN.blit(pg.image.load(PL).convert(), (x, y))
            elif sprite == "B":
                SCREEN.blit(pg.image.load(BG).convert(), (x, y))
            elif sprite == "E":
                SCREEN.blit(pg.image.load(E).convert(), (x, y))
            elif sprite == "T":
                SCREEN.blit(pg.image.load(T).convert(), (x, y))
            elif sprite == "S":
                SCREEN.blit(pg.image.load(S).convert(), (x, y))

    def movement(self, x, y):
        for key, value in enumerate(self.tiles):
            x = int(value[1]) * SIZE_SPRITE
            y = int(value[0]) * SIZE_SPRITE
        for event.type in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    y += (1 * SIZE_SPRITE)
                    SCREEN.blit(pg.image.load(PL).convert_alpha(), (x, y + 20))
                elif event.key == pg.K_LEFT:
                    y -= (1 * SIZE_SPRITE)
                    SCREEN.blit(pg.image.load(PL).convert_alpha(), (x, y - 20))
                elif event.key == pg.K_DOWN:
                    x -= (1 * SIZE_SPRITE)
                    SCREEN.blit(pg.image.load(PL).convert_alpha(), (x - 20, y))
                elif event.key == pg.K_UP:
                    x += (1 * SIZE_SPRITE)
                    SCREEN.blit(pg.image.load(PL).convert_alpha(), (x + 20, y))
