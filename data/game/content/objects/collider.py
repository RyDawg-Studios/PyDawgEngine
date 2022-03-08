from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class Collider(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[36, 36]):
        self.checkForCollision = True
        self.checkForOverlap = True
        self.position = position
        self.scale = scale
        super().__init__(man, pde)