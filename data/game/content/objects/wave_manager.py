from random import random

from data.engine.object.object import Object

class WaveManager(Object):
    def __init__(self, man, pde, wave):
        super().__init__(man, pde)
        self.currentWave = wave(owner=self)

    def update(self):
        self.currentWave.update()

        return super().update()