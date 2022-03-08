from random import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class Logo(Actor):
    def __init__(self, man, pde, position):
        self.position = position
        self.defaultScale = [43*6, 7*6]
        self.scale = self.defaultScale
        self.checkForOverlap = False
        self.checkForCollision = False
        self.useCenterForPosition = True
        super().__init__(man, pde)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\sci_logo.png', layer=3)

    def update(self):
        return super().update()