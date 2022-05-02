import random
from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.weapons.weapons import AutomaticRifle
import copy

class PickupWeapon(Actor):
    def __init__(self, man, pde, position=[0, 0], speed=[4, 4], rotation=0, weapon=None):
        self.weapon = weapon
        self.position = position
        self.scale = self.weapon.scale
        self.checkForCollision = False
        self.speed = speed
        self.rotation = rotation
        self.rotdir = random.choice([-0.35, 0.35])
        self.rotticks = 0
        self.rottime = 100


        super().__init__(man, pde)
        self.components['Sprite'] = SpriteComponent(owner=self, sprite=self.weapon.components["Sprite"].path, layer=1)
        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=speed)

    def update(self):
        self.rotticks += 1
        if self.rotticks >= self.rottime:
            self.components["Projectile"].rotation += self.rotdir
        self.components["Projectile"].speed[0] -= 0.2
        self.components["Projectile"].speed[1] -= 0.2

        if self.components["Projectile"].speed[0] < 0:
            self.components["Projectile"].speed[0] = 0
        if self.components["Projectile"].speed[1] < 0:
            self.components["Projectile"].speed[1] = 0
        return super().update()