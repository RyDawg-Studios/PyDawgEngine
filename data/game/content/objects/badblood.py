from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.game.content.objects.bullet import Bullet
import random
import math

class SickleCell(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[32,32], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=True, lifetime=150):
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.lifetime=lifetime
        self.rotation=rotation
        self.spriteRotation = random.randint(0, 360)
        self.speed = speed

        super().__init__(man, pde)


        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\sci_badblood.png', layer=2)
        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)


    def move(self, movement):
        pass

    def update(self):
        if self.position[0] < -40 or self.position[1] < -80:
            self.queuedeconstruction()
            return
        elif self.position[0] > 640 or self.position[1] > 480:
            self.queuedeconstruction()
            return
        return super().update()

    def overlap(self, obj):
        if obj.__class__ == Bullet:
            self.die()
            if obj.owner == self.man.getPlayers():
                obj.owner.score += 50
                obj.owner.roundScore += 50 
            if not obj.piercing:
                obj.queuedeconstruction()
        return super().overlap(obj)

    def die(self):
        self.queuedeconstruction()
        return
