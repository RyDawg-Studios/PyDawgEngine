import math
import random
from numpy import isin
import pygame
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getpositionlookatvector, objectlookatposition, objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.bullets.bullet import Bullet
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon

class DefaultBullet(Bullet):
    def __init__(self, man, pde, owner, speed=16, rotation=0, position=...):
        super().__init__(man, pde, owner, rotation, position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png', layer=1)
        self.speed = speed
        self.damage = 3

    def update(self):
        return super().update()

class DefaultBullet2(Bullet):
    def __init__(self, man, pde, owner, speed=16, rotation=0, position=...):
        super().__init__(man, pde, owner, rotation, position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png', layer=1)
        self.speed = speed
        self.damage = 20
        
class ZigZagBullet(Bullet):
    def __init__(self, man, pde, owner, rotation=0, position=...):
        super().__init__(man, pde, owner, rotation, position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png', layer=1)
        self.speed = 4
        self.zigrate = 10
        self.zigticks = 0
        self.zig = self.rotation + 60
        self.zag = self.rotation - 60
        self.zigzag = 1

    def update(self):
        self.zigticks += 1
        if self.zigticks >= self.zigrate:
            self.zigticks = 0
            if self.zigzag == 0:
                self.rotation = self.zig
                self.zigzag = 1
            elif self.zigzag == 1:
                self.rotation = self.zag
                self.zigzag = 0
        return super().update()

class HelixBullet(Bullet):
    def __init__(self, man, pde, owner, rotation=0, position=...):
        super().__init__(man, pde, owner, rotation, position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png', layer=1)

    def update(self):
        self.rotation += math.sin(self.rotation)
        return super().update()
        
class SniperBullet(Bullet):
    def __init__(self, man, pde, owner, speed=8, rotation=0, position=...):
        self.scale=[12, 12]
        super().__init__(man, pde, owner, rotation, position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png', layer=1)
        self.speed = [22, 22]
        self.damage = random.randint(40, 70)
        self.kb = 8

class HomingActor(Actor):
    def __init__(self, man, pde, position=[0, 0], owner=None):
        self.position = position
        self.scale = [400, 400]
        self.owner = owner
        self.target = None
        self.foundtarget = False
        self.checkForCollision = False
        super().__init__(man, pde)

    def overlap(self, obj):
        if self.foundtarget == False:
            self.target = obj
            if hasattr(obj, 'homable'):
                if obj.homable and obj != self.owner.owner.owner:
                    self.owner.rotation = objectlookattarget(self, obj)
        return super().overlap(obj)

    def update(self):
        self.rect.center = self.owner.rect.center
        return super().update()

class HomingBullet(Bullet):
    def __init__(self, man, pde, owner, speed=8, rotation=0, position=...):
        self.scale=[12, 12]
        super().__init__(man, pde, owner, rotation, position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png', layer=1)
        self.speed = [4, 4]
        self.damage = 1
        self.homing = False
        self.hometicks = 0
        self.starthometime = 15

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        self.hometicks += 1
        if self.hometicks >= self.starthometime:
            if not self.homing:
                self.area = self.man.add_object(obj=HomingActor(man=self.man, pde=self.pde, position=list(self.rect.center), owner=self))
                self.homing = True

        return super().update()

    def deconstruct(self):
        if hasattr(self, 'area'):
            self.area.deconstruct()
        return super().deconstruct()

class DevBullet(Bullet):
    def __init__(self, man, pde, owner, speed=8, rotation=0, position=...):
        self.scale=[12, 12]
        super().__init__(man, pde, owner, rotation, position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png', layer=1)
        self.speed = [16, 16]
        self.damage = 5
        self.homing = False
        self.hometicks = 0
        self.starthometime = 15

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        self.hometicks += 1
        if self.hometicks >= self.starthometime:
            if not self.homing:
                self.area = self.man.add_object(obj=HomingActor(man=self.man, pde=self.pde, position=list(self.rect.center), owner=self))
                self.homing = True

        return super().update()

    def deconstruct(self):
        if hasattr(self, 'area'):
            self.area.deconstruct()
        return super().deconstruct()

class RicochetBullet(Bullet):
    # WIP
    def __init__(self, man, pde, owner, speed=16, rotation=0, position=...):
        super().__init__(man, pde, owner, rotation, position)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\rocket.png', layer=1)
        self.speed = speed
        self.damage = 3

    def overlap(self, obj):
        return


class LaserBeam(Bullet):
    def __init__(self, man, pde, owner, speed=16, rotation=0, position=[0, 0], scale=[0, 0]):
        self.scale = scale
        self.owner = owner
        super().__init__(man, pde, owner, rotation, self.owner.rect.midtop, scale)
        self.destroyOnCollide = False
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\lasergun\beam.png', layer=1)
        self.speed = 0
        self.damage = 3
        self.lifetime = 120

class Grenade(Bullet):
    def __init__(self, man, pde, owner, speed=16, rotation=0, target=[0,0], position=[0, 0], scale=[20, 14]):
        self.scale = scale
        self.owner = owner
        self.lifetime = 50
        self.target = target
        rotation = 0
        super().__init__(man, pde, owner, rotation, self.owner.rect.midtop, scale, proj=False)
        self.destroyOnCollide = False
        self.checkForCollision = True
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\grenadelauncher\grenade.png', layer=1)
        self.speed = 8
        self.damage = 3
        self.target = getpositionlookatvector(self, target)
        self.movement = pygame.Vector2(self.target * speed)

    def update(self):   
        self.movement = pygame.Vector2(self.target * self.speed)
        if self.speed > 0.1:
            self.speed -= 0.1
        return super().update()

    def overlap(self, obj):
        return super().overlap(obj)

    def collide(self, obj, side):
        return super().collide(obj, side)

    def explode(self):
        return

    def deconstruct(self):
        self.explode()
        self.man.remove_object(self)
        for component in self.components.values():
            component.deconstruct()
        del self

    def collide(self, obj, side):
        print("W")
        return super().collide(obj, side)

    def move(self, movement):
        self.movement = pygame.math.Vector2(self.movement)
        self.collideInfo = {"Top": False, "Bottom": False, "Left": False, "Right": False, "Objects": []}
        if self.canMove:
            self.rect.x += self.movement.x * self.velocity
            hits = self.getoverlaps()  
            for object in hits:
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if object not in self.collideInfo["Objects"] and object != self.owner.owner:
                        self.collideInfo["Objects"].append(object)
                    if movement[0] > 0:
                        self.rect.right = object.rect.left
                        self.collideInfo["Right"] = True
                        object.collide(self, "Left")
                    elif movement[0] < 0:
                        self.rect.left = object.rect.right
                        self.collideInfo["Left"] = True
                        object.collide(self, "Right")
        if self.canMove:
            self.rect.y += self.movement.y * self.velocity
            hits = self.getoverlaps()  
            for object in hits:
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if object not in self.collideInfo["Objects"] and object != self.owner.owner:
                        self.collideInfo["Objects"].append(object)
                    if movement[1] > 0:
                        self.rect.bottom = object.rect.top
                        self.collideInfo["Bottom"] = True
                        object.collide(self, "Top")
                    elif movement[1] < 0:
                        self.rect.top = object.rect.bottom
                        self.collideInfo["Top"] = True
                        object.collide(self, "Bottom")
        self.position[0] = self.rect.center[0]
        self.position[1] = self.rect.center[1]
        self.scale[0] = self.rect.size[0]
        self.scale[1] = self.rect.size[1]

        if self.movement[0] < 0:
            self.direction = -1

        elif self.movement[0] > 0:
            self.direction = 1
