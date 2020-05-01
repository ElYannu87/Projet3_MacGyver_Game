import pygame

from mac_gyver import MacGyver
from maze import Maze


class Main:
    """
     Contains constant Item list
    """

    ITEMS = ["J", "K", "L"]

    def __init__(self):
        """
        Initialses the maze and player position and
        launches pygame game loop
        """
        self.maze = Maze("MazeMap/Maze.txt", self.ITEMS)
        self.mac_gyver = MacGyver(*self.maze.find_player())
        self.maze.display_maze()

        launched = True
        while launched:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    launched = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.game_loop("UP")
                    elif event.key == pygame.K_DOWN:
                        self.game_loop("DOWN")
                    elif event.key == pygame.K_LEFT:
                        self.game_loop("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.game_loop("RIGHT")

                    self.maze.display_maze()

    def game_loop(self, direction):
        """
        Main game loop with checks for movement, victory, items and
        player position.

        :param : Directions
        """
        new_y, new_x = self.mac_gyver.get_move_coords(direction)

        if self.maze.check_move(new_y, new_x):
            if self.maze.check_guardian(new_y, new_x):
                self.check_victory()
            self.collect_item(new_y, new_x)
            self.maze.update_player(self.mac_gyver.y, self.mac_gyver.x, new_y, new_x)
            self.mac_gyver.x = new_x
            self.mac_gyver.y = new_y

    def collect_item(self, y, x):
        """
        Stores items in player inventory
        :param : y and x of items
        """
        item = self.maze.get_item(self.ITEMS, y, x)
        if item is not None:
            self.mac_gyver.inventory.append(item)

    def check_victory(self):
        """
        Check for victory if player on Guardian position.
        """
        if len(self.mac_gyver.inventory) == len(self.ITEMS):
            print("You Win")
        else:
            print("You Loose")
        exit()


if __name__ == "__main__":
    Main()
