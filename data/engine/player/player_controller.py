import pygame
from data.engine.component.component import Component

class PlayerController(Component):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.inpman = self.owner.pde.input_manager
        self.key_inputs = []
        self.mouse_pos = [0,0]

    def update(self):
        super().update()
        self.key_inputs = self.inpman.key_inputs.copy()

        if self.owner is not None:
            if self not in self.owner.pde.player_manager.player_controllers:
                self.owner.pde.player_manager.player_controllers.append(self)
            self.manage_input()

    def manage_input(self):
        pass

    def on_joystick(self, event):
        pass

    def update_debug(self):
        pass

    def on_input(self, input):
        if input == pygame.K_F1:
            self.owner.pde.level_manager.level.objectManager.printobjects()
            
    def on_mouse(self, button):
        pass

    def deconstruct(self):
        super().deconstruct()
        if self.owner is not None:
            if self in self.owner.pde.player_manager.player_controllers:
                self.owner.pde.player_manager.player_controllers.remove(self)