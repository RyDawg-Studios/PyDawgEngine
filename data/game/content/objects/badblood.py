from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.game.content.objects.bullet import Bullet
import random
import math

class SickleCell(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[32,32], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=True, lifetime=150):
        super().__init__(man, pde)
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.lifetime=lifetime
        self.rotation=rotation
        self.speed = speed
        self.moveable = True

    def construct(self):
        super().construct()

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\sci_badblood.png', layer=2)



    def update(self):
        super().update()

        if self.rect.centerx not in range(-100, 740) or self.rect.centery not in range(-100, 580):
            self.deconstruct()
    

        self.movement[0] = math.cos(math.radians(self.rotation)) * self.speed[0]
        self.movement[1] = math.sin(math.radians(self.rotation)) * self.speed[1] *-1


    def overlap(self, obj):
        super().overlap(obj)
        if isinstance(obj, Bullet):
            self.die()
            if obj.owner == self.man.getPlayers():
                obj.owner.score += 50
                obj.owner.roundScore += 50 
            if not obj.piercing:
                obj.deconstruct()

    def die(self):
        self.deconstruct()
