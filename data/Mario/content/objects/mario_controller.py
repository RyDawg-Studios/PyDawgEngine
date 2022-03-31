import pygame
from data.engine.player.player_controller import PlayerController

class MarioController(PlayerController):
    def __init__(self, owner, **kwargs) -> None:
        super().__init__(owner, **kwargs)
        self.resetPos = True

    def on_input(self, input):
        if input == pygame.K_w:
            print(self.owner.speed)
            self.owner.movement[1] = -10
        return super().on_input(input)

    def manage_input(self):
        if pygame.K_RIGHT in self.owner.pde.input_manager.key_inputs or pygame.K_d in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[0] += 0.4
        elif pygame.K_LEFT in self.owner.pde.input_manager.key_inputs or pygame.K_a in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[0] += -0.4
        else:
            self.owner.movement[0] = 0


            
    
        return super().manage_input()