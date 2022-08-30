from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
import math
import random

class WallProjectile(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[2,640], speed=[1,1], rotation=0, lifetime=150):
        self.position=position
        self.scale=scale
        self.checkForCollision=False
        self.checkForOverlap=True
        self.lifetime=lifetime
        self.rotation=rotation
        self.speed = speed
        self.walltype = random.choice(['blue','orange'])

        super().__init__(man, pde)

        if self.walltype == 'blue':
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\bluewall.png', layer=2)
        else:
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\orangewall.png', layer=2)

        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)

    def move(self):
        pass

    def update(self):
        return super().update()