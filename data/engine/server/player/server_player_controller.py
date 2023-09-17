import pygame

from data.engine.player.player_controller import PlayerController

class ServerPlayerController(PlayerController):
    def __init__(self, owner, client=(0,0)):
        super().__init__(owner)
        self.client = client
        self.resetPos = True
        self.axis = [0, 0, 0, 0, 0, 0]

        self.owner.pde.player_manager.net_controllers[self.client] = self

    def on_input(self, input):
        return

    def manage_input(self):
        return
    
    def on_joystick(self, event):
        return

    def update(self):
        self.manage_input()
    
    def deconstruct(self):
        super().deconstruct()
        self.owner.pde.player_manager.net_controllers.pop(self)
        return
