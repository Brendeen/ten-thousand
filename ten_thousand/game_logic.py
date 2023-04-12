import random


def game_round():
    round_num = 1
    banked_score = 0
    kept_dice = []
    dice_to_roll = 6
    while dice_to_roll > 0:
        new_dice = tuple(GameLogic.roll_dice(dice_to_roll))
        roll = list(new_dice) + kept_dice
        print(roll)
        while True:
            print("Enter dice to keep, or (q)uit:")
            prompt = input("> ")
            if prompt == "q":
                print(f"Thanks for playing. You earned {banked_score} points")
                return
            parsed_input = parse_user_input(prompt)
            # print(parsed_input, new_dice, valid_user_input(parsed_input, new_dice))
            if valid_user_input(parsed_input, new_dice):
                break
        dice_to_roll -= len(parsed_input)
        kept_dice += parsed_input
        unbanked = GameLogic.calculate_score(kept_dice)
        while True:
            print(f"""You have {unbanked} unbanked points and {dice_to_roll} dice remaining
(r)oll again, (b)ank your points or (q)uit:""")
            prompt = input("> ")
            if prompt == "r":
                break
            elif prompt == "b":
                banked_score += unbanked
                print(f"""You banked {banked_score} points in round {round_num}
Total score is {banked_score} points""")
                round_num += 1
                print(f"""Starting round {round_num}
Rolling 6 dice...""")
                kept_dice = []
                dice_to_roll = 6
                break
            elif prompt == "q":
                print(f"Thanks for playing. You earned {banked_score} points")
                return


def valid_user_input(user_input, new_dice):
    """
    Checks to see if user_input is valid
    Example: "1 2 3 4 5 6"
    :param user_input: Parsed user input []
    :param new_dice: random.randint []
    :return: True is user_input is valid, False is user_info is not valid
    """
    if not user_input:
        return False
    dice_lst = list(new_dice)
    for i in user_input:
        if len(dice_lst) < 1:
            return False
        if not (i in dice_lst):
            print(f"{user_input} is not in your roll! Please retype...")
            return False
        dice_lst.remove(i)
    return True


def parse_user_input(user_input):
    """
    Checks to see if user_input is an int value, and will
    parse, return NULL is input is not an int in str data type
    :param user_input: users input str""
    :return: list of ints [] / return NULL is input is not an int in str data type
    """
    lst = user_input
    lst_2 = [int(i) for i in lst]
    return lst_2


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


def round_start():
    print("""
Welcome to Ten Thousand

(y)es to play or (q)uit to decline
    """)
    while True:
        prompt = input("> ")
        if prompt == "y":
            print("Starting round 1")
            game_round()
            return
        elif prompt == "q":
            print("OK. Maybe another time")
            break
        else:
            print(f"Sorry, {prompt} is not a valid answer, please type y or q.")


if __name__ == "__main__":
    round_start()
