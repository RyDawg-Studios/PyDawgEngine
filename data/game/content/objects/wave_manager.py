from random import random

import pygame
from data.engine.object.object import Object
from data.engine.sprite.sprite_component import SpriteComponent
import random


class WaveManager(Object):
    def __init__(self, man, pde, wave):
        super().__init__(man, pde)
        self.currentWave = wave(owner=self)

    def update(self):
        self.currentWave.update()

        return super().update()