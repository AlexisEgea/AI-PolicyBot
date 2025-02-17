from game.game_421 import Game_421
from game.launcher import Launcher
from player.random_bot import RandomBot

if __name__ == '__main__':
    game = Game_421()
    random_bot = RandomBot(game)
    launcher = Launcher(game, random_bot)
    launcher.start_game(10000)