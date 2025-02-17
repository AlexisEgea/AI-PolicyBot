import json
import os
import random

class Game_421:
    def __init__(self):
        self.dice = []
        self.win_dice = []
        self.number_dice_faces = - 1

        # number of tries
        self.horizon = -1
        self.actions = []

        self.win_game = 0
        self.loose_game = 0
        self.played_party = 0
        self.score = 0
        self.sum_score = 0

        self.init_game()

    # Init variables from specific configuration
    def init_game(self):
        config_path = os.path.join(os.getcwd(), "configuration/config.json")
        with open(config_path, 'r') as file:
            data = json.load(file)

        win_dice = data["win_dice"]
        dice = [int(char) for char in win_dice]
        self.win_dice = self.sort_dice(dice)
        for i in range(0, len(self.win_dice)):
            self.dice.append(0)
        self.number_dice_faces = data["number_dice_faces"]

        self.horizon = data["number_tries"]

        self.init_actions()

    def get_dice(self):
        return self.dice

    def get_win_dice(self):
        return self.win_dice

    def get_actions(self):
        return self.actions

    def get_horizon(self):
        return self.horizon

    def get_number_dice_faces(self):
        return self.number_dice_faces

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score = score
        self.sum_score += score

    def get_sum_score(self):
        return self.sum_score

    def get_win_game(self):
        return self.win_game

    def get_loose_game(self):
        return self.loose_game

    def get_played_party(self):
        return self.played_party

    def reset_game(self):
        for i in range(len(self.dice)):
            self.dice[i] = 0

        config_path = os.path.join(os.getcwd(), "configuration/config.json")
        with open(config_path, 'r') as file:
            data = json.load(file)
        self.horizon = data["number_tries"]
        self.score = 0

    # Init all possible actions
    def init_actions(self):
        actions = ["keep", "roll"]
        self.actions = self.generate_combinations(actions, len(self.dice))
        # print(self.actions)

    def generate_combinations(self, actions, num_dice, current_combination=None):
        if current_combination is None:
            current_combination = []

        if len(current_combination) == num_dice:
            return [" ".join(current_combination)]

        all_combinations = []
        for action in actions:
            all_combinations += self.generate_combinations(actions, num_dice, current_combination + [action])

        return all_combinations

    def play_dice(self, action):
        action_per_die = action.split(" ")
        for i in range(len(action_per_die)):
            if action_per_die[i] == "roll" or action_per_die[i] == "r":
                self.dice[i] = random.randint(1, self.number_dice_faces)
        self.dice = self.sort_dice(self.dice)
        self.horizon -= 1
        self.display_state_game()

    def get_state(self):
        result = ""
        for dice in self.dice:
            result += str(dice) + " "
        result += f"h{self.horizon}"
        return result

    def sort_dice(self, dice):
        dice_sorted = sorted(dice, reverse=True)
        return dice_sorted

    def win(self):
        if self.dice == self.win_dice:
            print("Game Win !!!")
            self.win_game += 1
            return True
        return False

    def loose(self):
        if self.horizon == 0:
            print("Game Loose :(")
            self.loose_game += 1
            return True
        return False

    def end(self):
        if self.win() or self.loose():
            self.played_party +=1
            return True
        return False


    def display_dice(self, dice):
        result = ""
        for dice in dice:
            result += str(dice)
            result += " "
        #[:-1] to avoid the last character which is a space
        return result[:-1]

    def display_state_game(self):
        print(f"{self.display_dice(self.dice)} h{self.horizon}")
