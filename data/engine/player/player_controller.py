from data.engine.component.component import Component
from data.engine.action.queues.queue import Queue

class PlayerController(Component):
    def __init__(self, owner, **kwargs) -> None:
        super().__init__(owner, **kwargs)
        self.inpman = self.owner.pde.input_manager

        if len(self.inpman.joysticks) > 0:
            self.resetPos = False
        else:
            self.resetPos = True

    def update(self):
        if self not in self.owner.pde.player_manager.player_controllers:
            self.owner.pde.player_manager.player_controllers.append(self)
        self.manage_input()
        return super().update()

    def manage_input(self):
        pass

    def on_joystick(self, event):
        pass

    def update_debug(self):
        pass

    def on_input(self, input):
        pass

    def on_mouse(self, button):
        pass

    def deconstruct(self):
        self.owner.pde.player_manager.player_controllers.remove(self)
        return super().deconstruct()