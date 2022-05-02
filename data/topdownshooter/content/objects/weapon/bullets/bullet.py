from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.tiles.tile import Tile

class Bullet(Actor):
    def __init__(self, man, pde, owner, rotation=0, position=[0,0], scale=[14, 7], proj=True):
        self.checkForCollision = False
        self.useCenterForPosition = True
        self.rotation = rotation
        self.scale = scale
        self.position = position
        self.speed = 12
        self.damage = 1
        self.owner = owner
        self.kb = 2
        self.destroyOnCollide = True
        super().__init__(man, pde)
        if proj:
            self.proj = self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)
        else:
            self.proj = None

    def move(self, movement):
        return

    def update(self):
        if self.proj is not None:
            self.proj.speed = self.speed
            self.proj.rotation = self.rotation
        if self.position[0] < -80 or self.position[1] < -80:
            self.deconstruct()
        elif self.position[0] > 720 or self.position[1] > 560:
            self.deconstruct()
        return super().update()


    def onshot(self):
        pass

    def overlap(self, obj):
        if self.ticks >= 2:
            if obj != self.owner and obj != self.owner.owner and obj.__class__ != self.owner.owner.__class__:
                if (hasattr(obj, 'hp') and obj.takedamage(self)) or isinstance(obj, Tile) and self.destroyOnCollide:
                        self.deconstruct()

        return super().overlap(obj)