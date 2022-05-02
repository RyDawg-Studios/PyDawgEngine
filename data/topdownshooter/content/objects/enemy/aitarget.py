import random
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class AIMovementTarget(Actor):
    def __init__(self, man, pde, position=[1, 1]):
        self.position = self.randomizeposition()
        self.scale = [20, 20]
        self.checkForCollision = False
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\undef.png', layer=4)

    def update(self):
        self.randomizeposition()
        return super().update()

    def randomizeposition(self):
        self.position = [random.randint(0, 640), random.randint(0, 480)]
        return self.position