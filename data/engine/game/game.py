class Game:
    def __init__(self, pde):
        self.pde = pde

    def activate(self):
        return

    def clearObjectManager(self):
        if self.pde.level_manager.level is not None:
            self.pde.level_manager.clearlevel()

    def update(self):
        pass

    def add_player(self, data):
        return

