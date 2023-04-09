import random


def welcome():
    print("""
    Welcome to Ten Thousand
    
    (y)es to play or (q)uit to decline
    """)
    while True:
        prompt = input("> ")
        if prompt == "y":
            game_round()
            break
        elif prompt == "q":
            print("OK. Maybe another time")
            break
        else:
            print(f"Sorry, {prompt} is not a valid answer, please type y or q.")


def game_round():
    round_num = 0
    print(f"""Starting round {round_num}
Rolling 6 dice...""")
    print(GameLogic.roll_dice(6))
    while True:
        round_num += 1
        print("Enter dice to keep, or (q)uit:")
        prompt = input("> ")
        if prompt == "123456":
            calc_score()
        elif prompt == "q":
            print("Thanks for playing. You earned 0 points")
            break


def calc_score(roll):
    pass
    print()
# this function will calculate a users score if they
# choose to bank any dice.


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
    # def calculate_score(roll):
    #     lst = [0] * 6
    #     roll_sum = 0
    #     straight_counter = 0
    #     doubles_counter = 0
    #     triples_counter = 0
    #
    #     for die in roll:
    #         lst[die - 1] += 1
    #     for freq in range(6):
    #         if lst[freq] > 2:
    #             if (freq + 1) == 1:
    #                 roll_sum += (lst[freq] - 2) * 1000
    #             else:
    #                 roll_sum += ((lst[freq] - 2) * (freq + 1) * 100)
    #         elif (freq + 1) == 1:
    #             roll_sum += (lst[freq] * 100)
    #         elif (freq + 1) == 5:
    #             roll_sum += (lst[freq] * 50)
    #         if lst[freq] == 1:
    #             straight_counter += 1
    #         elif lst[freq] == 2:
    #             doubles_counter += 1
    #         elif lst[freq] == 3:
    #             triples_counter += 1
    #     if straight_counter == 6:
    #         return 1500
    #     elif doubles_counter == 3:
    #         return 1500
    #     elif triples_counter == 2:
    #         return 1200
    #
    #     return roll_sum
    def calculate_score(roll):
        """
        function to calculate and sum roll_dice score
        :param roll: start of score = 0, based on role int will be increased
        :return: Dice score based on
        """
        roll_sum = 0  # Base number of points
        lst = [roll.count(i) for i in range(1, 7)]
        # Using comprehension to loop through roll list, and creat lst of all rolled dice values

        straight_counter = lst.count(1) == 6  # Loops through lst looking for straight, set to true/false

        for freq, count in enumerate(lst):
            if count >= 3:
                if freq == 0:
                    roll_sum += (count - 2) * 1000
                else:
                    roll_sum += (freq + 1) * 100 * (count - 2)
                # Using enumerates built-in function, this section checks if there are multiples of 3
                # or above in the roll, and assigning the proper scoring for each multiple
                # Enumerate() is a built-in function that allows you to keep track of how many loops are in a loop

            elif freq == 0:
                roll_sum += count * 100
            elif freq == 4:
                roll_sum += count * 50
                # These values represent 1 and 5, as they have different scoring cases

        if straight_counter or lst.count(2) == 3 or lst.count(3) == 2:
            return 1500 \
                if straight_counter \
                else 1200 \
                if lst.count(3) == 2 \
                else 1500
        return roll_sum
        # Last part of function, searching for special dice scoring cases
        # Lastly returning roll_sum with updated score


if __name__ == "__main__":
    welcome()
