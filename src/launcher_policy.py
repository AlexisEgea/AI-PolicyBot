import os
import random
from src.player.humane import Humane
from src.game.game_421 import Game_421
from src.player.random_bot import RandomBot
from src.player.policy_bot import PolicyBot

if __name__ == '__main__':
    game = Game_421()

    humane = Humane()

    data_path = os.path.join(os.getcwd(), "src/data/421.csv")
    if not os.path.exists(data_path):
        random_bot = RandomBot(game)
        game.start_game(random_bot, 10000)
        score_random = game.score

    game = Game_421()
    policy_bot = PolicyBot(game)
    game.start_game(policy_bot, 10000)





