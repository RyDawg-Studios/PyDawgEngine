from turtle import speed
from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.game.content.objects.bullet import Bullet
from data.engine.fl.world_fl import objectlookattarget
import random
from data.game.content.objects.covidbullet import CovidBullet
from data.engine.anim.anim_manager import AnimManager

from data.engine.projectile.projectile import Projectile

class CovidWarning(Actor):
    def __init__(self, man, pde, owner, position=[0,0], scale=[180,180], rotation=0, checkForCollision=False, checkForOverlap=True, spawnboss = True):
        super().__init__(man, pde)
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.useCenterForPosition = True
        self.lifetime=-1
        self.ticktime = 300
        self.ticks = 0
        self.rotation=rotation
        self.spawnboss = spawnboss
        self.spriteRotation = 0
        self.owner = owner
        


    def construct(self):
        super().construct()

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\covidwarning.png', layer=2)
        self.components["BlinkAnim"] = AnimManager(owner=self, sprite=self.components["Sprite"])
        self.components["BlinkAnim"].addAnimation(name='Blinking', anim=r'data\game\assets\blink', speed=0.1, looping=True, set=True)

    def move(self, movement):
        pass

    def update(self):
        self.ticks += 1
        if self.ticks >= self.ticktime:
            if self.spawnboss == True:
                self.owner.spawnboss()
                self.spawnboss = False
            self.deconstruct()
        return super().update()

    def die(self):
        for i in range(1, 13):
            self.man.add_object(CovidBullet(man=self.man, pde=self.pde, owner=self, position=[self.rect.center[0], self.rect.center[1]], rotation=objectlookattarget(self, self.player) + i*30, scale=[20, 20], speed=[6, 6] , lifetime=400)) 

        self.owner.active = True
        self.deconstruct()

    def deconstruct(self):
        return super().deconstruct()



