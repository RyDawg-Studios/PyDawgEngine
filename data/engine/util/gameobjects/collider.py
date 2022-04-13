import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.text import TextComponent


class Collider(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[36, 36]):
        self.checkForCollision = True
        self.checkForOverlap = True
        self.position = position
        self.scale = scale
        self.text = "WALL"
        super().__init__(man, pde)

        self.components["Text"] = TextComponent(owner=self, text='text', layer=9, font=pygame.font.SysFont('impact.ttf', 72), color=(255, 255, 255))

