import random


class RandomBot:
    def __init__(self, game):
        self.game = game
        self.state = None
        self.action = {}


    def perceive(self, game):
        pass

    def decide(self):
        self.state = self.game.get_state()
        i = random.randint(0, len(self.game.actions)-1)
        action = self.game.actions[i]
        self.action = action

        return self.action

    def sleep(self, result):
        # open a State.Action.Value file in append mode:
        logFile= open( "src/data/421.csv", "a" )
        logFile.write( f"{self.state},{self.action},{result}\n" )
        logFile.close()