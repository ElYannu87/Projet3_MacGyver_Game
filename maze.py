import random


class Maze:
    def __init__(self, file_path):
        self.maze = self.load_maze(file_path)

    def load_maze(self, file_path):
        maze = []
        with open(file_path, "r") as file:
            for line in file:
                lab_line = []
                for character in line:
                    if character != "\n":
                        lab_line.append(character)
                maze.append(lab_line)

        return maze

    def print_maze(self):
        for line in self.maze:
            print("".join(line))

    def find_player(self):
        for y, line in enumerate(self.maze):
            for x, character in enumerate(line):
                if character == "m":
                    return y, x
        return None

    def check_move(self, y, x):
        return 0 <= y < len(self.maze) \
               and 0 <= x < len(self.maze[y]) \
               and self.maze[y][x] != "#"

    def update_player(self, old_y, old_x, new_y, new_x):
        self.maze[old_y][old_x] = " "
        self.maze[new_y][new_x] = "m"

    def randomize_items(self, items_name):
        maze_item_space = []
        for y, line in enumerate(self.maze):
            for x, char in enumerate(line):
                if char == " ":
                    maze_item_space.append([y, x])

        items = random.sample(maze_item_space, len(items_name))

        for index, item in enumerate(items_name):
            self.maze[items[index][0]][items[index][1]] = item

    def get_item(self, items, y, x):
        if self.maze[y][x] != " " and self.maze[y][x] in items:
            return self.maze[y][x]
        else:
            return None