from random import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent



class Reticle(Actor):
    def __init__(self, man, pde, player):
        self.player = player
        self.position = [player.position[0], player.position[1]]
        self.defaultScale = [30, 30]
        self.scale = self.defaultScale
        self.checkForOverlap = False
        self.checkForCollision = False
        self.useCenterForPosition = True
        self.state = 'Mouse'

        super().__init__(man, pde)


        if len(self.pde.input_manager.joysticks) > 0:
            self.state = [self.player.position[0], self.player.position[1]]
        else:
            self.state = self.man.pde.input_manager.mouse_position

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\reticle.png', layer=3)

    def update(self):

        if len(self.pde.input_manager.joysticks) > 0:
            self.state = [self.player.position[0], self.player.position[1]]
        else:
            self.state = self.man.pde.input_manager.mouse_position

        self.rect.center = self.state
        if "Sprite" in self.components:
            self.components["Sprite"].sprite.image = pygame.transform.scale(self.components["Sprite"].sprite.image, (self.scale[0],self.scale[1]))

        return super().update()