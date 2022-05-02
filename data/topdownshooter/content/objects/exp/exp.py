import random
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import objectlookattarget
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent

class ExpAreaActor(Actor):
    def __init__(self, man, pde, position=[0, 0], owner=None):
        self.position = position
        self.scale = [100, 100]
        self.owner = owner
        self.target = None
        self.foundtarget = False
        self.checkForCollision = False
        super().__init__(man, pde)
        #self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=1)


    def overlap(self, obj):
        if self.foundtarget == False:
            self.target = obj
            if hasattr(obj, 'canCollectExp'):
                if obj.canCollectExp:
                    self.owner.speed = [4, 4]
                    self.owner.rotation = objectlookattarget(self, obj)
                    print(self.owner.rotation)
        return super().overlap(obj)

    def update(self):
        self.rect.center = self.owner.rect.center
        return super().update()
        
class EXP(Actor):
    def __init__(self, man, pde, position=[0, 0]):
        self.position = position
        self.checkForCollision = False
        self.scale = [8, 8]

        self.speed = [2, 2]
        self.rotation = 180

        super().__init__(man, pde)

        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\objects\exp\exp.png', layer=2)
        self.proj = self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)
        self.area = self.man.add_object(obj=ExpAreaActor(man=self.man, pde=self.pde, position=list(self.rect.center), owner=self))

    def move(self, movement):
        return

    def update(self):
        self.proj.speed = self.speed
        self.proj.rotation = self.rotation
        self.sprite.sprite.rotation = self.rotation

        if self.position[0] < -80 or self.position[1] < -80:
            self.deconstruct()
        elif self.position[0] > 720 or self.position[1] > 560:
            self.deconstruct()

        self.speed[0] -= 0.2
        self.speed[1] -= 0.2

        if self.speed[0] < 0:
            self.speed[0] = 0
        if self.speed[1] < 0:
            self.speed[1] = 0

        return super().update()