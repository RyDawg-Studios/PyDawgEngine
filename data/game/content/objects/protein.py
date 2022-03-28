from data.engine.actor.actor import Actor
from data.engine.object.object import Object
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
import random

from data.game.content.objects.bullet import Bullet

class Protein(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[16,16], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=True, lifetime=150):
        self.useCenterForPosition = True
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.lifetime=lifetime
        self.rotation=rotation
        self.speed = speed
        self.spriteRotation = random.randint(0, 360)

        super().__init__(man, pde)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\protein.png', layer=5)
        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)
        
    def move(self, movement):
        pass

    def update(self):
        if self.position[0] < -40 or self.position[1] < -80:
            self.deconstruct()
        elif self.position[0] > 640 or self.position[1] > 480:
            self.deconstruct()
        return super().update()

    def overlap(self, obj):
        if obj.__class__ == Bullet:
            obj.owner.chosepowerup()
            self.deconstruct()
        return super().overlap(obj)







class ProteinSpawner(Object):
    def __init__(self, man, pde):
        super().__init__(man, pde)

        self.ticks = 0

        self.state = 'Random'
        self.done = False

        self.projspeed = random.randint(3,6)
        self.ticktime = random.randint(0, 200)
        self.projlifetime = 700



    def update(self):
        self.ticks += 1
        if self.state == "Random":
            if self.ticks == self.ticktime:
                self.man.add_object(Protein(man=self.man, pde=self.pde, position=[random.randint(0, 640), 0], rotation=-90, scale=[42, 18], speed=[3, 3] , lifetime=self.projlifetime)) 
                self.ticktime = random.randint(1500, 3000)
                self.ticks = 0




            