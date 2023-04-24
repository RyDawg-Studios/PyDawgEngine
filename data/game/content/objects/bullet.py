from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
import math

class Bullet(Actor):
    def __init__(self, man, pde, owner, position=[0,0], scale=[16,16], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=True, lifetime=150, piercing = False):
        super().__init__(man, pde)
        self.useCenterForPosition = True
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=True
        self.lifetime=lifetime
        self.rotation=rotation
        self.speed = speed
        self.piercing = piercing
        self.owner=owner
        self.spriteScale = self.scale


    def construct(self):
        super().construct()
        if not self.piercing:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\bullet.png', layer=1)
        else:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\bluebullet.png', layer=1)


    def update(self):
        super().update()

        self.movement[0] = math.cos(math.radians(self.rotation)) * self.speed[0]
        self.movement[1] = math.sin(math.radians(self.rotation)) * self.speed[1] *-1

        if self.position[0] < -40 or self.position[1] < -80:
            self.deconstruct()
        elif self.position[0] > 680 or self.position[1] > 480:
            self.deconstruct()
