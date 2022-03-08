from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
import math

class Bullet(Actor):
    def __init__(self, man, pde, owner, position=[0,0], scale=[16,16], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=False, lifetime=150, piercing = False):
        self.useCenterForPosition = True
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.useCenterForPosition = True
        self.lifetime=lifetime
        self.rotation=rotation
        self.speed = speed
        self.piercing = piercing
        self.owner=owner
        self.spriteScale = self.scale

        super().__init__(man, pde)

        if not self.piercing:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\bullet.png', layer=5)
        else:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\bluebullet.png', layer=5)

        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)

    def move(self):
        pass

    def update(self):
        if self.position[0] < -40 or self.position[1] < -80:
            self.deconstruct()
        elif self.position[0] > 640 or self.position[1] > 480:
            self.deconstruct()
        return super().update()
