import pygame
import sys

from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.input.input_manager import InputManager


class InputManagerServer(InputManager):
    def __init__(self, pde):
        super().__init__(pde)

    def manage_inputs(self, event):
        if event.type == pygame.KEYDOWN:
            self.on_input_event.call(event.key)

        if event.type == pygame.KEYUP:
            self.on_output_event.call(event.key)

        if pygame.K_ESCAPE in self.key_inputs:
            pygame.quit()
            sys.exit()

    def handle_net_input(self, data, client):
        if data[1] == True: #If Keydown
            self.pde.player_manager.net_controllers[client].key_inputs.append(data[0])
            self.pde.player_manager.net_controllers[client].on_input(data[0])
        else:
            self.pde.player_manager.net_controllers[client].key_inputs.remove(data[0])

    def handle_net_mouse(self, data, client):
        self.pde.player_manager.net_controllers[client].mouse_pos = data[0]