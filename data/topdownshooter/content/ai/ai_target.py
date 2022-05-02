from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.actor.actor import Actor

class AITarget(Actor):
    def __init__(self, man, pde, position):
        self.position = position
        self.checkForCollision = False
        super().__init__(man, pde)


    