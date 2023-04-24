import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.text import TextComponent


class Collider(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[36, 36]):
        super().__init__(man, pde)
        self.checkForCollision = True
        self.checkForOverlap = True
        self.useCenterForPosition = False
        self.position = position
        self.scale = scale


