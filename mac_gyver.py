import pygame

class MacGyver:
    """
    Getting all the information for the player.
    Safety if no player is placed in the maze
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

        if x is None or y is None:
            print("Map invalide, personnage non trouvé")
            exit(1)  # 1 = error happened

        self.inventory = []

    def get_move_coords(self, direction):
        """
        :arg The direction to move to
        Input converted for Pygame library
        """
        x = self.x
        y = self.y

        if direction == "RIGHT":
            x = x - 1
        elif direction == "LEFT":
            x = x + 1
        elif direction == "UP":
            y = y - 1
        elif direction == "DOWN":
            y = y + 1
        else:
            print("Veuillez saisir un caractère valide")

        return y, x


