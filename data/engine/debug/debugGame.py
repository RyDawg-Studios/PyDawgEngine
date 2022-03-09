from data.engine.debug.debugLevel import DebugLevel
from data.engine.game.game import Game



class DebugGame(Game):
    def __init__(self, pde):
        super().__init__(pde)

    def activate(self):
        self.pde.level_manager.addlevel(level=DebugLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
        return super().activate()