import random
from src.player.humane import Humane
from src.game.game_421 import Game_421
from src.player.random_bot import RandomBot
from src.player.policy_bot import PolicyBot

if __name__ == '__main__':
    game = Game_421()

    humane = Humane()
    random_bot = RandomBot(game)
    policy_bot = PolicyBot(game)
    game.start_game(policy_bot, 10000)





