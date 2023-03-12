import pygame


class LevelManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.level = None

    def clearlevel(self):
        if self.level is not None:
            self.level.objectManager.clear()
            self.level.deconstruct()
            self.level = None

    def addlevel(self, level, name, active):
        if self.level is not None:
            self.clearlevel()
        self.level = None
        self.level = level
        level.active = active
        return self.level

    def update(self):
        self.level.update()
        return

    def activate(self):
        return