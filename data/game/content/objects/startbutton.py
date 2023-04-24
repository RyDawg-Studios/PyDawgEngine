from random import random

import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.text import TextComponent
from data.game.content.objects.widgets.loadgame import LoadGameButton


class StartButtonActor(Actor):
    def __init__(self, man, pde, position):
        super().__init__(man, pde)
        self.position = position
        self.defaultScale = [90, 27]
        self.scale = self.defaultScale
        self.checkForOverlap = False
        self.checkForCollision = False
        self.useCenterForPosition = True
        self.textvar = 3

    def construct(self):
        super().construct()

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\start.png', layer=3)
        self.components["Button"] = LoadGameButton(owner=self)
