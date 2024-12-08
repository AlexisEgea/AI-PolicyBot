import json
import os
import random


class Game_421:
    def __init__(self):
        self.dices = []
        self.win_dices = []
        self.number_dice_faces = - 1

        # number of tries
        self.horizon = -1
        self.actions = []

        self.win_game = 0
        self.loose_game = 0
        self.played_party = 0
        self.score = 0

    def init_game(self):
        config_path = os.path.join(os.getcwd(), "src/configuration/config.json")
        with open(config_path, 'r') as file:
            data = json.load(file)

        win_dices = data["win_dices"]
        dices = [int(char) for char in win_dices]
        self.win_dices = self.sort_dices(dices)
        for i in range(0, len(self.win_dices)):
            self.dices.append(0)
        self.number_dice_faces = data["number_dice_faces"]

        self.horizon = data["number_tries"]

        self.init_actions()

    def reset_game(self):
        for i in range(len(self.dices)):
            self.dices[i] = 0

        config_path = os.path.join(os.getcwd(), "src/configuration/config.json")
        with open(config_path, 'r') as file:
            data = json.load(file)
        self.horizon = data["number_tries"]


    def init_actions(self):
        actions = ["keep", "roll"]
        self.actions = self.generate_combinations(actions, len(self.dices))
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

    def play_dices(self, action):
        actions = action.split(" ")
        for i in range(len(actions)):
            if actions[i] == "roll" or actions[i] == "r":
                self.dices[i] = random.randint(1, self.number_dice_faces)
        self.dices = self.sort_dices(self.dices)
        self.horizon -= 1
        self.display_state_game()

    def get_state(self):
        result = ""
        for dice in self.dices:
            result += str(dice) + " "
        result += f"h{self.horizon}"
        return result

    def sort_dices(self, dices):
        dices_sorted = sorted(dices, reverse=True)
        return dices_sorted


    def start_game(self, player, number_party):
        self.init_game()

        for i in range(0, number_party):
            print(f"Game {i} ____________________")
            action = "roll roll roll"
            self.play_dices(action)
            while not self.end():
                player.perceive(self)
                action = player.decide()
                self.play_dices(action)
                result = self.score_state()
                player.sleep(result)
            self.reset_game()
        print(f"On {self.played_party} parties, {self.win_game} parties were won and {self.loose_game} parties were lost")
        result = self.score / number_party
        print(f"score: {result}")

    def score_state(self):
        # Win score
        if self.win():
            self.score += 100
            return 100

        # Same dices
        if len(set(self.dices)) == 1:
            if self.dices[0] == 1:
                self.score += 90
                return 90
            self.score += 80
            return 80

        # n-1 1 result
        if self.dices.count(1) == len(self.dices) - 1:
            self.score += 60
            return 60

        # Suite
        sorted_faces = list(range(1, self.number_dice_faces + 1))  # Exemple : [1, 2, 3, 4, 5, 6]
        if self.dices in [sorted_faces[i:i + len(self.dices)] for i in range(len(sorted_faces) - len(self.dices) + 1)]:
            self.score += 70
            return 70

        # Other
        self.score += 1
        return 1


    def win(self):
        if self.dices == self.win_dices:
            print("Game Win !!!")
            self.win_game += 1
            self.played_party +=1
            return True
        return False

    def loose(self):
        if self.horizon == 0:
            print("Game Loose :(")
            self.loose_game += 1
            self.played_party +=1
            return True
        return False

    def end(self):
        if self.win() or self.loose():
            return True
        return False


    def display_dices(self, dices):
        result = ""
        for dice in dices:
            result += str(dice)
            result += " "
        #[:-1] to avoid the last character which is a space
        return result[:-1]

    def display_state_game(self):
        print(f"{self.display_dices(self.dices)} h{self.horizon}")


    def display_game(self):
        print(f"Score to win the game: {self.display_dices(self.win_dices)}")
        print(f"Your dices: {self.display_dices(self.dices)}, try: {self.horizon}")
