import os
from game.game_421 import Game_421
from game.launcher import Launcher
from player.random_bot import RandomBot
from player.policy_bot import PolicyBot

if __name__ == '__main__':
    game = Game_421()

    # To use the policy bot, we need a dataset to create a policy. If this dataset does not exist,
    # we need to execute the random bot on 10,000 games to generate it.
    data_path = os.path.join(os.getcwd(), "data/421.csv")
    if not os.path.exists(data_path):
        random_bot = RandomBot(game)
        launcher = Launcher(game, random_bot)
        launcher.start_game(10000)
        game = Game_421()

    policy_bot = PolicyBot(game)
    launcher = Launcher(game, policy_bot)
    launcher.start_game(10000)





