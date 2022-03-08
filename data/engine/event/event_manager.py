import pygame
from data.engine.input.input_manager import InputManager
import sys

class EventManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde

        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                self.pde.input_manager.manage_inputs(event)

    def activate(self):
        pass