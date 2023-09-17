import pygame
import sys

class PlayerManager():
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.player_controllers = []
        self.net_controllers = {}
        
    def update(self):
        return
        
    def activate(self):
        return

    def clear(self):
        for pc in self.player_controllers:
            pc.deconstruct()
            pc = None
        return