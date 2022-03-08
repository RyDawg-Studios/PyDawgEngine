from data.engine.widgets.button import Button


class LoadGameButton(Button):
    def __init__(self, owner):
        super().__init__(owner)


    def onpressed(self, mbid):
        self.owner.pde.game.loadbattlelevel()

    def update(self):
        if 7 in self.owner.pde.input_manager.controller_inputs:
            self.onpressed(0)
        return super().update()

