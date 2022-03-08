import pygame


class LevelManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.levels={}

    def addlevel(self, level, name, active):
        level.active = active
        self.levels[name] = level

    def removelevel(self, level):
        for obj in list(self.levels[level].objectManager.objects.values()):
            obj.deconstruct()
        self.levels.pop(level)

    def update(self):
        for level in list(self.levels):
            if self.levels[level].active:
                self.levels[level].update()

    def activate(self):
        pass