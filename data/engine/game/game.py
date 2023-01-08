from data.engine.level.level import Level

class Game:
    def __init__(self, pde):
        self.pde = pde

    def activate(self):
        self.pde.level_manager.addlevel(level=Level(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

    def clearObjectManager(self):
        if self.pde.level_manager.level is not None:
            self.pde.level_manager.clearlevel()

    def update(self):
        pass

