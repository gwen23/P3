import pygame

from pygame.locals import *
from settings import *
from level import *
from the_maze import *
from guardian import Guardian
from player import Macgyver

level = Level()
maze = Maze()


class Game:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.fond = pygame.image.load("./images/floor-tiles-20x20.png").convert()
        pygame.display.set_caption('The Maze')
        self.level = Level()
        self.run()

    def run(self):
        self.screen.blit(self.fond, (0, 0))
        self.level.afficher()
        self.main_loop()

    def main_loop(self):
        x = 0
        y = 20
        is_running = True
        while is_running:
            clock.tick(5)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if level.move_macgyver("right"):
                            screen.blit(FLOOR_IMG, (x, y))
                            x += 1 * size_sprite
                            screen.blit(PLAYER_IMG, (x, y))
                    elif event.key == pygame.K_LEFT:
                        if level.move_macgyver("left"):
                            screen.blit(FLOOR_IMG, (x, y))
                            x -= 1 * size_sprite
                            screen.blit(PLAYER_IMG, (x, y))
                    elif event.key == pygame.K_UP:
                        if level.move_macgyver("up"):
                            screen.blit(FLOOR_IMG, (x, y))
                            y -= 1 * size_sprite
                            screen.blit(PLAYER_IMG, (x, y))
                    elif event.key == pygame.K_DOWN:
                        if level.move_macgyver("down"):
                            screen.blit(FLOOR_IMG, (x, y))
                            y += 1 * size_sprite
                            screen.blit(PLAYER_IMG, (x, y))
                if event.type == pygame.QUIT:
                    is_running = False
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    while True:
        game.maze()
        game.main_loop()
