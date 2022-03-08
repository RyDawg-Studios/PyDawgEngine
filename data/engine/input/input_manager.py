import pygame
import sys


class InputManager():
    def __init__(self, pde):
        self.active = False
        self.pde = pde
        self.key_inputs = []
        self.mouse_inputs = []
        self.mouse_position = []
        self.controller_axis_values = {0: 0, 1:0, 2:0, 3:0, 4:-1, 5:-1}
        self.controller_inputs = []
        self.joystick_inputs = None
        self.hat_inputs = (0, 0)
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for j in self.joysticks:
            print(j)
            j.init()
 
    def update(self):
        self.mouse_inputs = pygame.mouse.get_pressed(5)
        self.mouse_position = pygame.mouse.get_pos()

    def manage_inputs(self, event):

        if event.type == pygame.KEYDOWN:
            self.key_inputs.append(event.key)
            for pc in self.pde.game.player_controllers:
                pc.on_input(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for pc in self.pde.game.player_controllers:
                pc.on_mouse(event)

        if event.type == pygame.KEYUP:
            self.key_inputs.remove(event.key)

        if event.type == pygame.JOYAXISMOTION:
            self.controller_axis_values[event.axis] = round(event.value)
            for pc in self.pde.game.player_controllers:
                pc.on_joystick(event)

        if event.type == pygame.JOYBUTTONDOWN:
            self.controller_inputs.append(event.button)
            for pc in self.pde.game.player_controllers:
                pc.on_input(event.button)

        if event.type == pygame.JOYBUTTONUP:
            self.controller_inputs.remove(event.button)

        if event.type == pygame.JOYHATMOTION:
            self.hat_inputs = event.value
            for pc in self.pde.game.player_controllers:
                pc.on_input(event.value)
        else:
            self.hat_inputs = (0, 0)




        if pygame.K_ESCAPE in self.key_inputs:
            pygame.quit()
            sys.exit()


    def activate(self):
        pass
