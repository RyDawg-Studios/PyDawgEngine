from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.game.content.objects.bullet import Bullet
from data.engine.fl.world_fl import objectlookattarget
import random
from data.game.content.objects.covidbullet import CovidBullet

from data.game.content.objects.projectile import Projectile

class CovidWarning(Actor):
    def __init__(self, man, pde, owner, position=[0,0], scale=[180,180], rotation=0, checkForCollision=False, checkForOverlap=True):
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.useCenterForPosition = True
        self.lifetime=300
        self.rotation=rotation
        self.spriteRotation = 0
        self.owner = owner

        super().__init__(man, pde)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\covidwarning.png', layer=2)

    def move(self):
        pass

    def update(self):
        return super().update()

    def die(self):
        for i in range(1, 13):
            self.man.add_object(CovidBullet(man=self.man, pde=self.pde, owner=self, position=[self.rect.center[0], self.rect.center[1]], rotation=objectlookattarget(self, self.player) + i*30, scale=[20, 20], speed=[6, 6] , lifetime=400)) 

        self.owner.active = True
        self.deconstruct()

    def deconstruct(self):
        self.owner.spawnboss()
        return super().deconstruct()



