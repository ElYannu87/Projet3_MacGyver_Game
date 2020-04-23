import pygame

class MacGyver:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        if x is None or y is None:
            print("Map invalide, personnage non trouvé")
            exit(1)  # 1 = error happened

        self.inventory = []

    def get_move_coords(self, direction):
        x = self.x
        y = self.y

        if direction == "q":
            x = x - 1
        elif direction == "d":
            x = x + 1
        elif direction == "UP":
            y = y - 1
        elif direction == "s":
            y = y + 1
        else:
            print("Veuillez saisir un caractère valide")

        return y, x


