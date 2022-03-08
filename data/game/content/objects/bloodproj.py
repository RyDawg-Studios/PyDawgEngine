from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
import math

class Blood(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[16,16], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=False, lifetime=150):
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.useCenterForPosition = True
        self.checkForOverlap=checkForOverlap
        self.lifetime=lifetime
        self.rotation=rotation
        self.speed = speed

        super().__init__(man, pde)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\sci_bloodcell.png', layer=1)
        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)

    def move(self):
        pass

    def update(self):
        if self.position[0] < -20 or self.position[1] < -80:
            self.deconstruct()
        elif self.position[0] > 640 or self.position[1] > 480:
            self.deconstruct()
        return super().update()
