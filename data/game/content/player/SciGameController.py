import pygame
from data.engine.player.player_controller import PlayerController


class SciGameController(PlayerController):
    def __init__(self, owner, **kwargs):
        super().__init__(owner, **kwargs)
        self.max_player_speed = 2
        self.saved_pos = [0,0]
        self.resetPos = True
        if len(self.inpman.joysticks) > 0:
            self.resetPos = False
        self.ticks = 0

    def manage_input(self):
        super().manage_input()
        self.ticks += 1
        if pygame.K_RIGHT in self.key_inputs or pygame.K_d in self.key_inputs:
            self.owner.movement[0] = 1
        elif pygame.K_LEFT in self.key_inputs or pygame.K_a in self.key_inputs:
            self.owner.movement[0] = -1
        else:
            self.owner.movement[0] = 0
        if pygame.K_UP in self.key_inputs or pygame.K_w in self.key_inputs:
            self.owner.movement[1] = -1
        elif pygame.K_DOWN in self.key_inputs or pygame.K_s in self.key_inputs:
            self.owner.movement[1] = 1
        else:
            self.owner.movement[1] = 0


        if self.owner.pde.input_manager.mouse_inputs[0] or pygame.K_SPACE in self.owner.pde.input_manager.key_inputs or self.owner.pde.input_manager.controller_axis_values[5] > 0:
            if self.ticks >= self.owner.shotInfo['fireRate']:
                self.owner.shoot()
                self.ticks = 0

    def on_joystick(self, event):
        super().on_joystick(event)
        if event.axis < 2:
            self.owner.speed[event.axis] = round(event.value) * self.owner.maxSpeed[0]

        elif event.axis == 2 or event.axis == 3:
            self.owner.reticle.speed[event.axis-2] = event.value * 50

    def on_input(self, input):
        super().on_input(input)
        if input == pygame.K_f:
            self.saved_pos = [self.owner.rect.x, self.owner.rect.y]
            print("Position Logged @ " + str(self.saved_pos))
        if input == pygame.K_g:
            self.owner.rect.x, self.owner.rect.y = self.saved_pos
            print("Position Loaded @ " + str(self.saved_pos))
        if input == pygame.K_p:
            self.owner.printDebugInfo()
        if input == 6:
            self.owner.pde.game.loadtitlelevel()
        if input == pygame.K_j:
            self.owner.health += 99999
            self.owner.shotType = 'triple'
        if input == pygame.K_UP:
            self.owner.pde.game.bossesKilled += 1
        if input == pygame.K_DOWN:
            self.owner.pde.game.bossesKilled -= 1

