from maze import Maze


class MacGyver:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory = []

    def get_move_coords(self, direction):
        x = self.x
        y = self.y

        if direction == "q":
            x = x - 1
        elif direction == "d":
            x = x + 1
        elif direction == "z":
            y = y - 1
        elif direction == "s":
            y = y + 1
        else:
            print("Veuillez saisir un caractère valide")

        return y, x

    def check_inventory(self):
        if self.inventory == 3:
            pass
