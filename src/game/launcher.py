from game.game_421 import Game_421
from utils.evaluation import Evaluation


class Launcher:
    def __init__(self, game: Game_421, player):
        self.game = game
        self.player = player

    def start_game(self, number_party):
        for i in range(0, number_party):
            print(f"Game {i+1} ____________________")
            action = " ".join(["roll"] * len(self.game.get_dice()))
            self.game.play_dice(action)
            score = Evaluation.score(self.game)
            self.game.add_score(score)
            while not self.game.end():
                self.player.perceive(self)
                action = self.player.decide()
                self.game.play_dice(action)
                score = Evaluation.score(self.game)
                self.game.add_score(score)
                self.player.sleep(score)
            self.game.reset_game()
        print(f"On {self.game.get_played_party()} games, {self.game.get_win_game()} were won and {self.game.get_loose_game()} were lost")
        result = self.game.get_sum_score() / self.game.get_played_party()
        print(f"score: {result}/100")