import random


class GameLogic:

    @staticmethod
    def roll_dice(n):
        """
        roll 6 standard 6 sided dice, and return 6 values in between 1 - 6.
        :param n: dice rolled
        :return: a tuple of n numbers/ints each in between 1 - 6, like a standard 6 sided dice
        """
        return tuple(random.randint(1, 6) for _ in range(n))

    @staticmethod
    def calculate_score(roll):
        pass


if __name__ == "__main__":
    print(GameLogic.roll_dice(6))
