import pygame

from pygame.locals import *
from settings import *
from level import *
from the_maze import *

clock = pygame.time.Clock()
pygame.display.set_caption('The Maze')
level = Level()


class Game:

    def __init__(self):
        pygame.init()
        self.maze = Maze()
        pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.image.load(FLOOR_IMG).convert()
        pygame.image.load(WALL_IMG).convert()
        pygame.image.load(ETHER_IMAGE).convert_alpha()
        pygame.image.load(TUBE_IMAGE).convert_alpha()
        pygame.image.load(SERINGE_IMAGE).convert_alpha()
        pygame.image.load(BAD_GUY_IMAGE).convert_alpha()
        pygame.image.load(PLAYER_IMG).convert_alpha()
        pygame.display.set_caption('The Maze')
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.fond = pygame.image.load("./images/floor-tiles-20x20.png").convert()
        self.level = Level()
        self.run()

    def run(self):
        self.SCREEN.blit(self.fond, (0, 0))
        self.level.afficher(self.maze.tiles)
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
                        if self.maze.move_macgyver("right"):
                            SCREEN.blit(pygame.image.load(FLOOR_IMG).convert(), (x, y))
                            x += 1 * SIZE_SPRITE
                            SCREEN.blit(pygame.image.load(PLAYER_IMG).convert_alpha(), (x, y))
                    elif event.key == pygame.K_LEFT:
                        if self.maze.move_macgyver("left"):
                            SCREEN.blit(pygame.image.load(FLOOR_IMG).convert(), (x, y))
                            x -= 1 * SIZE_SPRITE
                            SCREEN.blit(pygame.image.load(PLAYER_IMG).convert_alpha(), (x, y))
                    elif event.key == pygame.K_UP:
                        if self.maze.move_macgyver("up"):
                            SCREEN.blit(pygame.image.load(FLOOR_IMG).convert(), (x, y))
                            y -= 1 * SIZE_SPRITE
                            SCREEN.blit(pygame.image.load(PLAYER_IMG).convert_alpha(), (x, y))
                    elif event.key == pygame.K_DOWN:
                        if self.maze.move_macgyver("down"):
                            SCREEN.blit(pygame.image.load(FLOOR_IMG).convert(), (x, y))
                            y += 1 * SIZE_SPRITE
                            SCREEN.blit(pygame.image.load(PLAYER_IMG).convert_alpha(), (x, y))
                if event.type == pygame.QUIT:
                    is_running = False
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    while True:
        game.run()
        game.main_loop()
