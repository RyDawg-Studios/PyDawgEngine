import pygame
from data.engine.player.player_controller import PlayerController

class DebugController(PlayerController):
    def __init__(self, owner, **kwargs) -> None:
        super().__init__(owner, **kwargs)
        self.resetPos = True

    def on_input(self, input):
        if input == pygame.K_l:
            self.owner.pde.game == self.owner.pde.Leukosite(pde=self.pde)

        if input == pygame.K_f:
            self.owner.sendself()



        return super().on_input(input)

    def manage_input(self):
        if pygame.K_RIGHT in self.owner.pde.input_manager.key_inputs or pygame.K_d in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[0] = 2
        elif pygame.K_LEFT in self.owner.pde.input_manager.key_inputs or pygame.K_a in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[0] = -2
        else:
            self.owner.movement[0] = 0
        
        if pygame.K_UP in self.owner.pde.input_manager.key_inputs or pygame.K_w in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[1] = -2
        elif pygame.K_DOWN in self.owner.pde.input_manager.key_inputs or pygame.K_s in self.owner.pde.input_manager.key_inputs:
            self.owner.movement[1] = 2
        else:
            self.owner.movement[1] = 0


        return super().manage_input()