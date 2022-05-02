from data.engine.game.game import Game
from data.topdownshooter.content.levels.ShooterLevel import ShooterLevel

class ShooterGame(Game):
    def __init__(self, pde):
        self.player = None
        super().__init__(pde)


    def activate(self):
        self.pde.level_manager.addlevel(level=ShooterLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
        return super().activate()