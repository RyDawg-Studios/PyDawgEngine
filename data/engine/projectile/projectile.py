from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
import math

class Projectile(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[16,16], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=True, lifetime=150):
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.lifetime=lifetime
        self.rotation=rotation
        self.speed = speed

        super().__init__(man, pde)

    def move(self, movement):
        pass

    def update(self):
        if self.position[0] < -80 or self.position[1] < -80:
            self.deconstruct()
        elif self.position[0] > 720 or self.position[1] > 560:
            self.deconstruct()
        return super().update()
