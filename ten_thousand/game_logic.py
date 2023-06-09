# import random
#
#
# def game_round(round_num, banked_score):
#     kept_dice = []
#     dice_to_roll = 6
#     unbanked_previous = 0
#     hot_hand_carry_over = 0
#
#     print(f"""Starting round {round_num}
# Rolling 6 dice...""")
#
#     while dice_to_roll > 0:
#         new_dice = tuple(GameLogic.roll_dice(dice_to_roll))
#         roll = list(new_dice) + kept_dice
#         print_roll(new_dice, kept_dice)
#         unbanked = GameLogic.calculate_score(roll) + hot_hand_carry_over
#
#         if unbanked == unbanked_previous:
#             print("Fiddlesticks!!!")
#             return banked_score, True
#         unbanked_previous = unbanked
#
#         while True:
#             print("Enter dice to keep, or (q)uit:")
#             prompt = input("> ")
#             if prompt == "q":
#                 return banked_score, False
#
#             parsed_input = parse_user_input(prompt)
#             # print(parsed_input, new_dice, valid_user_input(parsed_input, new_dice))
#             if valid_user_input(parsed_input, new_dice):
#                 break
#             print_roll(new_dice, kept_dice)
#         dice_to_roll -= len(parsed_input)
#         kept_dice += parsed_input
#
#         while True:
#             print(f"""You have {unbanked} unbanked points and {dice_to_roll} dice remaining
# (r)oll again, (b)ank your points or (q)uit:""")
#             prompt = input("> ")
#             if prompt == "r":
#                 if hot_hand_check(roll):
#                     dice_to_roll = 6
#                     kept_dice = []
#                     hot_hand_carry_over = unbanked
#                     print("Hot Hand!")
#                 break
#             elif prompt == "b":
#                 banked_score += unbanked
#                 print(f"""You banked {unbanked} points in round {round_num}""")
#                 return banked_score, True
#             elif prompt == "q":
#                 return banked_score, False
#             else:
#                 print("Invalid response, please type (r)oll to again, (b)ank to your points or (q)uit")
#     print("Fiddle Sticks!")
#     return banked_score, True
#
#
# def valid_user_input(user_input, new_dice):
#     """
#     Checks to see if user_input is valid
#     Example: "1 2 3 4 5 6"
#     :param user_input: Parsed user input []
#     :param new_dice: random.randint []
#     :return: True is user_input is valid, False is user_info is not valid
#     """
#     if not user_input:
#         return False
#     dice_lst = list(new_dice)
#     for i in user_input:
#         if len(dice_lst) < 1:
#             return False
#         if not (i in dice_lst):
#             print(f"{user_input} is not in your roll! Please retype...")
#             return False
#         dice_lst.remove(i)
#     return True
#
#
# def parse_user_input(user_input):
#     """
#     Checks to see if user_input is an int value, and will
#     parse, return NULL is input is not an int in str data type
#     :param user_input: users input str""
#     :return: list of ints [] / return NULL is input is not an int in str data type
#     """
#     user_input = user_input.replace(" ", "")
#     lst = user_input
#     lst_2 = [int(i) for i in lst]
#     return lst_2
#
#
# class GameLogic:
#
#     @staticmethod
#     def roll_dice(n):
#         """
#         roll 6 standard 6 sided dice, and return 6 values in between 1 - 6.
#         :param n: dice rolled
#         :return: a tuple of n numbers/ints each in between 1 - 6, like a standard 6 sided dice
#         """
#         return tuple(random.randint(1, 6) for _ in range(n))
#
#     @staticmethod
#     # def calculate_score(roll):
#     #     lst = [0] * 6
#     #     roll_sum = 0
#     #     straight_counter = 0
#     #     doubles_counter = 0
#     #     triples_counter = 0
#     #
#     #     for die in roll:
#     #         lst[die - 1] += 1
#     #     for freq in range(6):
#     #         if lst[freq] > 2:
#     #             if (freq + 1) == 1:
#     #                 roll_sum += (lst[freq] - 2) * 1000
#     #             else:
#     #                 roll_sum += ((lst[freq] - 2) * (freq + 1) * 100)
#     #         elif (freq + 1) == 1:
#     #             roll_sum += (lst[freq] * 100)
#     #         elif (freq + 1) == 5:
#     #             roll_sum += (lst[freq] * 50)
#     #         if lst[freq] == 1:
#     #             straight_counter += 1
#     #         elif lst[freq] == 2:
#     #             doubles_counter += 1
#     #         elif lst[freq] == 3:
#     #             triples_counter += 1
#     #     if straight_counter == 6:
#     #         return 1500
#     #     elif doubles_counter == 3:
#     #         return 1500
#     #     elif triples_counter == 2:
#     #         return 1200
#     #
#     #     return roll_sum
#     def calculate_score(roll):
#         """
#         function to calculate and sum roll_dice score
#         :param roll: start of score = 0, based on role int will be increased
#         :return: Dice score based on
#         """
#         roll_sum = 0  # Base number of points
#         lst = [roll.count(i) for i in range(1, 7)]
#         # Using comprehension to loop through roll list, and creat lst of all rolled dice values
#
#         straight_counter = lst.count(1) == 6  # Loops through lst looking for straight, set to true/false
#
#         for freq, count in enumerate(lst):
#             if count >= 3:
#                 if freq == 0:
#                     roll_sum += (count - 2) * 1000
#                 else:
#                     roll_sum += (freq + 1) * 100 * (count - 2)
#                 # Using enumerates built-in function, this section checks if there are multiples of 3
#                 # or above in the roll, and assigning the proper scoring for each multiple
#                 # Enumerate() is a built-in function that allows you to keep track of how many loops are in a loop
#
#             elif freq == 0:
#                 roll_sum += count * 100
#             elif freq == 4:
#                 roll_sum += count * 50
#                 # These values represent 1 and 5, as they have different scoring cases
#
#         if straight_counter or lst.count(2) == 3 or lst.count(3) == 2:
#             return 1500 \
#                 if straight_counter \
#                 else 1200 \
#                 if lst.count(3) == 2 \
#                 else 1500
#         return roll_sum
#         # Last part of function, searching for special dice scoring cases
#         # Lastly returning roll_sum with updated score
#
#     # @staticmethod
#     # def get_scorers(dice):
#     #     # version_3
#     #
#     #     all_dice_score = GameLogic.calculate_score(dice)
#     #
#     #     if all_dice_score == 0:
#     #         return tuple()
#     #
#     #     scorers = []
#     #
#     #     # for i in range(len(dice)):
#     #
#     #     for i, val in enumerate(dice):
#     #         sub_roll = dice[:i] + dice[i + 1:]
#     #         sub_score = GameLogic.calculate_score(sub_roll)
#     #
#     #         if sub_score != all_dice_score:
#     #             scorers.append(val)
#     #
#     #     return tuple(scorers)
#
#     # Brendens get-scorers() method
#
#     # @staticmethod
#     # def get_scorers(roll):
#     #     roll_score = GameLogic.calculate_score(roll)
#     #
#     #     scorers = [r for r in roll if GameLogic.calculate_score([x for x in roll if x != r]) != roll_score]
#     #     if roll_score:
#     #         return tuple(scorers)
#     #     else:
#     #         return tuple()
#
#
# # GameLogic - method - get_scorers()
# # List or tuple, needs to contain values of the dice that contribute
# # to the score in the current given role
# # returns the dice that contribute to the score
#
#
# def hot_hand_check(roll):
#     full_hand = GameLogic.calculate_score(roll)
#     # TODO: Check if removing any element reduces roll score
#     for i in range(len(roll)):
#         hot_roll = list(roll)
#         hot_roll.pop(i)
#         if not GameLogic.calculate_score(hot_roll) < full_hand:
#             return False
#     return True
#
#
# def print_roll(new_dice, kept_dice):
#     print("New dice: " + str(new_dice)[1:-1] + "   Kept dice: " + str(kept_dice)[1:-1])
#
#
# def round_start():
#     print("""
# Welcome to Ten Thousand
#
# (y)es to play or (q)uit to decline
#     """)
#     while True:
#         prompt = input("> ")
#         if prompt == "y":
#             play_game()
#             return
#         elif prompt == "q":
#             print("OK. Maybe another time")
#             return
#         else:
#             print(f"Sorry, {prompt} is not a valid answer, please type y or q.")
#
#
# def play_game():
#     banked_score = 0
#     round_num = 1
#     continue_game = True
#     while continue_game and round_num <= 20:
#         banked_score, continue_game = game_round(round_num, banked_score)
#         print(f"Total score is {banked_score} points")
#         round_num += 1
#
#     print(f"Thanks for playing. You earned {banked_score} points")
#
#
# if __name__ == "__main__":
#     round_start()

from collections import Counter
import random


class GameLogic:
    def __init__(self, mock_rolls=None):
        """
        Initialize an instance of the GameLogic class for testing. Accepts optional argument of a list of mock rolls.
        :param mock_rolls: List of tuples, each tuple is a list of integers representing a mocked roll.
        """
        self.mock_rolls = mock_rolls

    def mock_roller(self, _):
        return self.mock_rolls.pop(0)

    @staticmethod
    def roll_dice(n):
        """
        Rolls n 6-sided dice.
        :param n: Number of dice.
        :return: Tuple of dice rolls.
        """
        rolls = tuple(random.randint(1, 6) for _ in range(n))
        return rolls

    @staticmethod
    def is_cheating(roll, keepers): # (1, 2, 1, 3, 3, 4)  (1, 1, 1)
        """
        Returns True if user is cheating!
        :param roll: Tuple of integers, representing the dice roll
        :param keepers: Tuple of integers, representing dice the user is keeping
        :return: Boolean! True if the user is trying to cheat. False if not cheating.
        """
        return bool(Counter(keepers) - Counter(roll))
        pass

    @staticmethod
    def calculate_score(roll):
        """
        Scores a give roll according to the rules of Ten Thousand.
        :param roll: A tuple of integers representing dice values.
        :return: An integer representing the score.
        """
        roll = Counter(roll)
        score = 0

        # Check for straight
        if len(roll) == 6:
            return 1500

        # Check for 3 pair
        if len(roll) == 3 and roll.most_common()[2][1] == 2:
            return 1500

        # 3 or more of any number
        for i in range(1, 7):
            quantity = roll[i]
            if quantity >= 3:
                if i == 1:
                    score += (quantity - 2) * 1000
                else:
                    score += (quantity - 2) * i * 100

        # 1s and 5s
        score += 100 if roll[1] == 1 else 0
        score += 200 if roll[1] == 2 else 0
        score += 50 if roll[5] == 1 else 0
        score += 100 if roll[5] == 2 else 0

        return score

    @staticmethod
    def get_scorers(dice):
        # version_3

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        # for i in range(len(dice)):

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(val)

        return tuple(scorers)
