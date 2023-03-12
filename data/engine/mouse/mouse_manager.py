import pygame
from pygame import display


class MouseManager():
    def __init__(self, pde):
        self.active = False
        self.pde = pde
        self.pos = [0, 0]

    def update(self):
        self.pos = pygame.mouse.get_pos()


    def activate(self):
        return