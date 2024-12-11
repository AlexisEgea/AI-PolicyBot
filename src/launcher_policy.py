import os
from game.game_421 import Game_421
from player.random_bot import RandomBot
from player.policy_bot import PolicyBot

if __name__ == '__main__':
    game = Game_421()

    # To use the policy bot, we need a dataset to create a policy. If this dataset does not exist,
    # we need to execute the random bot on 10,000 games to generate it.
    data_path = os.path.join(os.getcwd(), "data/421.csv")
    if not os.path.exists(data_path):
        random_bot = RandomBot(game)
        game.start_game(random_bot, 10000)
        game = Game_421()

    policy_bot = PolicyBot(game)
    game.start_game(policy_bot, 10000)





