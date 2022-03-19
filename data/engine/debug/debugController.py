import pygame
from data.engine.player.player_controller import PlayerController


class DebugController(PlayerController):
    def __init__(self, owner, **kwargs) -> None:
        super().__init__(owner, **kwargs)
        self.resetPos = True

    def on_input(self, input):
        return super().on_input(input)

    def manage_input(self):
        maxSpeed = self.owner.maxSpeed
        if pygame.K_RIGHT in self.owner.pde.input_manager.key_inputs or pygame.K_d in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[0] = maxSpeed[0]
            self.owner.direction = 1
        elif pygame.K_LEFT in self.owner.pde.input_manager.key_inputs or pygame.K_a in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[0] = -maxSpeed[0]
            self.owner.direction = -1
        else:
            self.owner.speed[0] = 0

        if pygame.K_UP in self.owner.pde.input_manager.key_inputs or pygame.K_w in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[1] = -maxSpeed[1]
        elif pygame.K_DOWN in self.owner.pde.input_manager.key_inputs or pygame.K_s in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[1] = maxSpeed[1]
        else:
            if self.resetPos:
                self.owner.speed[1] = 0
        return super().manage_input()