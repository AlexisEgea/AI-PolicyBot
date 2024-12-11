from game.game_421 import Game_421
from player.human import Human

if __name__ == '__main__':
    game = Game_421()

    human = Human()
    print("-----------------------------------------------------------------------------")
    print("|                        ©  Dice Roll Game                                  |")
    print("| Author : Alexis EGEA                                                      |")
    print("-----------------------------------------------------------------------------\n")
    print(f"Goal of this game: "
        f"\n    Roll {len(game.get_win_dice())} dice and get {game.get_win_dice()} to win. You have {game.get_horizon()} "
        f"attempts to achieve this goal."
        f"\n    You can also choose to roll only the dice you want. To play, type 'keep' to save a die or 'roll' "
        f"to reroll it. Enter your actions in the desired order to perform keeps and re rolls."
        f"\n    Note that the dice are sorted before being displayed.\n")

    game.start_game(human, 1)
