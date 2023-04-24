from random import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent



class Reticle(Actor):
    def __init__(self, man, pde, player):
        super().__init__(man, pde)
        self.player = player
        self.position = [player.position[0], player.position[1]]
        self.defaultScale = [30, 30]
        self.scale = self.defaultScale
        self.checkForOverlap = False
        self.checkForCollision = False
        self.useCenterForPosition = True
        self.state = [0, 0]



        if len(self.pde.input_manager.joysticks) > 0:
            self.state = [self.player.position[0], self.player.position[1]]
        else:
            self.state = self.man.pde.input_manager.mouse_position

    def construct(self):
        super().construct()

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\reticle.png', layer=5)

    def update(self):
        super().update()

        if len(self.pde.input_manager.joysticks) > 0:
            self.state = [self.player.position[0], self.player.position[1]]
        else:
            self.state = self.man.pde.input_manager.mouse_position

        self.rect.center = self.state

