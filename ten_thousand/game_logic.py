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
        lst = [0] * 6
        roll_sum = 0
        straight_counter = 0
        doubles_counter = 0
        triples_counter = 0

        for die in roll:
            lst[die - 1] += 1
        for freq in range(6):
            if lst[freq] > 2:
                if (freq + 1) == 1:
                    roll_sum += (lst[freq] - 2) * 1000
                else:
                    roll_sum += ((lst[freq] - 2) * (freq + 1) * 100)
            elif (freq + 1) == 1:
                roll_sum += (lst[freq] * 100)
            elif (freq + 1) == 5:
                roll_sum += (lst[freq] * 50)
            if lst[freq] == 1:
                straight_counter += 1
            elif lst[freq] == 2:
                doubles_counter += 1
            elif lst[freq] == 3:
                triples_counter += 1
        if straight_counter == 6:
            return 1500
        elif doubles_counter == 3:
            return 1500
        elif triples_counter == 2:
            return 1200

        return roll_sum


if __name__ == "__main__":
    print(GameLogic.roll_dice(6))
