from game.game_421 import Game_421
from player.random_bot import RandomBot

if __name__ == '__main__':
    game = Game_421()
    random_bot = RandomBot(game)
    game.start_game(random_bot, 10000)





