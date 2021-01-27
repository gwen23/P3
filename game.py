import pygame as pg
import pygame.key as kd


from game.settings import E, T, S, FL, WA, BG, PL, WIDTH, HEIGHT, SIZE_SPRITE
from game.level import Level
from game.the_maze import Maze

clock = pg.time.Clock()
pg.display.set_caption('The Maze')
level = Level()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))


class Game:

    def __init__(self):
        pg.init()
        self.maze = Maze()
        pg.display.set_mode((WIDTH, HEIGHT))
        pg.image.load(FL).convert()
        pg.image.load(WA).convert()
        pg.image.load(E).convert_alpha()
        pg.image.load(T).convert_alpha()
        pg.image.load(S).convert_alpha()
        pg.image.load(BG).convert_alpha()
        pg.image.load(PL).convert_alpha()
        pg.display.set_caption('The Maze')
        self.clock = pg.time.Clock()
        self.is_running = True
        self.SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
        self.fond = pg.image.load("./images/floor-tiles-20x20.png").convert()
        self.level = Level()
        self.run()

    def run(self):
        self.SCREEN.blit(self.fond, (0, 0))
        self.level.display(self.maze.tiles)
        self.main_loop()

    def main_loop(self):
        x = 0
        y = 20
        is_running = True
        while is_running:
            clock.tick(5)
            for event in pg.event.get():
                if event.type == kd and event.key == pg.K_RIGHT:
                    if self.maze.move_macgyver("right"):
                        SCREEN.blit(pg.image.load(FL).convert(), (x, y))
                        x += 1 * SIZE_SPRITE
                        SCREEN.blit(pg.image.load(PL).convert_alpha(), (x, y))
                elif event.type == kd and event.key == pg.K_LEFT:
                    if self.maze.move_macgyver("left"):
                        SCREEN.blit(pg.image.load(FL).convert(), (x, y))
                        x -= 1 * SIZE_SPRITE
                        SCREEN.blit(pg.image.load(PL).convert_alpha(), (x, y))
                elif event.type == kd and event.key == pg.K_UP:
                    if self.maze.move_macgyver("up"):
                        SCREEN.blit(pg.image.load(FL).convert(), (x, y))
                        y -= 1 * SIZE_SPRITE
                        SCREEN.blit(pg.image.load(PL).convert_alpha(), (x, y))
                elif event.type == kd and event.key == pg.K_DOWN:
                    if self.maze.move_macgyver("down"):
                        SCREEN.blit(pg.image.load(FL).convert(), (x, y))
                        y += 1 * SIZE_SPRITE
                        SCREEN.blit(pg.image.load(PL).convert_alpha(), (x, y))
                if event.type == pg.QUIT:
                    is_running = False
            pg.display.update()
        pg.quit()


if __name__ == "__main__":
    game = Game()
    while True:
        game.run()
        game.main_loop()
