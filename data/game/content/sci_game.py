from data.engine.game.game import Game


class Eukaryosite(Game):
    def __init__(self, pde):
        super().__init__(pde)
        self.difficulty = 10
        self.score = "No Score"