import random
import pygame
import constants


class Maze:
    def __init__(self, file_path, items_list):
        self.maze = self.load_maze(file_path)
        self.randomize_items(items_list)

        pygame.init()
        self.screen = pygame.display.set_mode((constants.SEIZE_SCREEN, constants.SEIZE_SCREEN))
        self.floor = pygame.image.load("Images/floortile1.png").convert_alpha()
        self.wall = pygame.image.load("Images/wall.png").convert_alpha()
        self.guardian = pygame.image.load("Images/Gardien.png").convert_alpha()
        self.macgyver = pygame.image.load("Images/MacGyver.png").convert_alpha()
        self.needle = pygame.image.load("Images/Bonus/aiguille.png").convert_alpha()
        self.ether = pygame.image.load("Images/Bonus/ether.png").convert_alpha()
        self.seringue = pygame.image.load("Images/Bonus/seringue.png").convert_alpha()

    def load_maze(self, file_path):
        """
        Load labyrinth from file_path into maze
        :param file_path: path of the maze
        :return: list of list containing the map
        """

        maze = []
        with open(file_path, "r") as file:
            for line in file:
                lab_line = []
                for character in line:
                    if character != "\n":
                        lab_line.append(character)
                maze.append(lab_line)

        return maze

    def display_maze(self):
        """
        Displays the maze on screen with pygame canvas
        """
        for y, line in enumerate(self.maze):
            for x, case in enumerate(line):
                if case == "#":
                    self.screen.blit(source=self.wall, dest=(x * 40, y * 40))
                elif case == "m":
                    self.screen.blit(source=self.wall, dest=(x * 40, y * 40))
                elif case == " ":
                    self.screen.blit(source=self.floor, dest=(x * 40, y * 40))
                elif case == "L":
                    self.screen.blit(source=self.floor, dest=(x * 40, y * 40))
                    self.screen.blit(source=self.needle, dest=(x * 40, y * 40))
                elif case == "J":
                    self.screen.blit(source=self.floor, dest=(x * 40, y * 40))
                    self.screen.blit(source=self.ether, dest=(x * 40, y * 40))
                elif case == "K":
                    self.screen.blit(source=self.floor, dest=(x * 40, y * 40))
                    self.screen.blit(source=self.seringue, dest=(x * 40, y * 40))
                elif case == "G":
                    self.screen.blit(source=self.guardian, dest=(x * 40, y * 40))

        pygame.display.flip()

    def find_player(self):
        """
        Finds the player starting position
        """
        for y, line in enumerate(self.maze):
            for x, character in enumerate(line):
                if character == "m":
                    return y, x
        return None

    def check_move(self, y, x):
        """
        Verifys the if the movement is legal and does not
        exit the maze or goes into walls
        :param y and x of player
        """
        return 0 <= y < len(self.maze) \
               and 0 <= x < len(self.maze[y]) \
               and self.maze[y][x] != "#"

    def update_player(self, old_y, old_x, new_y, new_x):
        """
        Replaces the old player position with the new one
        :param old_y, old_y: old player position
        :param new_y, new_x: new player position
        """
        self.maze[old_y][old_x] = " "
        self.maze[new_y][new_x] = "m"

    def randomize_items(self, items_name):
        """
        Randomizes the item displayed in the maze
        :param : item_name from global Items in Main
        """
        maze_item_space = []
        for y, line in enumerate(self.maze):
            for x, char in enumerate(line):
                if char == " ":
                    maze_item_space.append([y, x])

        items = random.sample(maze_item_space, len(items_name))

        for index, item in enumerate(items_name):
            self.maze[items[index][0]][items[index][1]] = item

    def get_item(self, items, y, x):
        """
        Verifing if the space where the player stands contains an Item.
        If so, Item is added to inventory
        :param y and x of the items
        :return : Item
        """
        if self.maze[y][x] != " " and self.maze[y][x] in items:
            return self.maze[y][x]
        else:
            return None

    def check_guardian(self, y, x):
        """
        :param y and x coordianates of guardian
        :return : Guardian coordinates
        """
        return self.maze[y][x] == "G"
