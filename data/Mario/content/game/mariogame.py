from data.engine.game.game import Game
from data.game.debug.debuglevel import MarioDebugLevel


class MarioGame(Game):
    def __init__(self, pde):
        super().__init__(pde)

    def activate(self):
        self.pde.level_manager.changelevel(level=MarioDebugLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
        return super().activate()

    