from maze import Maze
from mac_gyver import MacGyver


class Main:
    ITEMS = ["J", "K", "L"]

    def __init__(self):
        self.maze = Maze("MazeMap/Maze.txt")
        x, y = self.maze.find_player()

        if x is None or y is None:
            print("Map invalide, personnage non trouvé")
            exit(1)  # 1 = error happened

        self.maze.randomize_items(self.ITEMS)
        self.mac_gyver = MacGyver(x, y)

        while True:
            self.game_loop()

    def game_loop(self):
        self.maze.print_maze()
        direction = input()
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
