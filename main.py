import pygame
import os

from maze import Maze
from mac_gyver import MacGyver
import constants


class Main:

    ITEMS = ["J", "K", "L"]

    def __init__(self):
        self.maze = Maze("MazeMap/Maze.txt", self.ITEMS)
        self.mac_gyver = MacGyver(*self.maze.find_player())

        launched = True
        while launched:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    launched = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.game_loop("UP")

    def game_loop(self, direction):
        new_y, new_x = self.mac_gyver.get_move_coords(direction)

        if self.maze.check_move(new_y, new_x):
            if self.maze.check_guardian(new_y, new_x):
                self.check_victory()
            self.collect_item(new_y, new_x)
            self.maze.update_player(self.mac_gyver.y, self.mac_gyver.x, new_y, new_x)
            self.mac_gyver.x = new_x
            self.mac_gyver.y = new_y

    def collect_item(self, y, x):
        item = self.maze.get_item(self.ITEMS, y, x)
        if item is not None:
            self.mac_gyver.inventory.append(item)

    def check_victory(self):
        if len(self.mac_gyver.inventory) == len(self.ITEMS):
            print("You Win")
        else:
            print("You Loose")
        exit()


if __name__ == "__main__":
    Main()
