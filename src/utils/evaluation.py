class Evaluation:
    @classmethod
    # def score(cls, dice, win_dice, number_dice_faces, previous_score):
    def score(cls, game):

        # Win dice
        if game.win():
            score = 100
        # All the dice show the same value.
        elif len(set(game.get_dice())) == 1:
            if game.get_dice()[0] == 1:
                score = 30
            else:
                score = 25
        # All the dice are showing 1, except for one
        elif game.get_dice().count(1) == len(game.get_dice()) - 1:
            score = 10
        # A sequence of consecutive numbers
        elif game.get_dice() in [list(range(i, i + len(game.get_dice()))) for i in
                      range(1, game.get_number_dice_faces() - len(game.get_dice()) + 2)]:
            score = 20
        # Other cases
        else:
            score = 1

        reward = score - game.get_score()
        return reward
