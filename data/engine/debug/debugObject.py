from turtle import pos
import pygame
from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
import math
from data.engine.anim.anim_manager import AnimManager
from data.engine.anim.anim_sprite import AnimSprite
from data.engine.debug.debugController import DebugController
from data.engine.object.object import Object
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class TestSpriteActor(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[32, 32]):
        self.checkForCollision = False
        self.checkForOverlap = False
        self.position = position
        self.scale = scale
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)

        self.components["Anim"] = AnimManager(owner=self, layer=2, sprite=self.components["Sprite"])

        self.components["Anim"].addAnimation(name='runright', anim=r'data\assets\anims\runright', speed=0.2, set=True, stopFrame=-1)
        self.components["Anim"].addAnimation(name='runleft', anim=r'data\assets\anims\runleft', speed=0.2, set=True, stopFrame=-1)

        self.components["Anim"].addAnimation(name='idleright', anim=r'data\assets\anims\idleright', speed=0.2, set=False, stopFrame=-1)
        self.components["Anim"].addAnimation(name='idleleft', anim=r'data\assets\anims\idleleft', speed=0.2, set=False, stopFrame=-1)

    def update(self):
        if self.speed[0] > 0:
            self.components["Anim"].setAnimState(state='runright')

        elif self.speed[0] < 0:
            self.components["Anim"].setAnimState(state='runleft')

        else:
            if self.direction == 1:
                self.components["Anim"].setAnimState(state='idleright')
            if self.direction == -1:
                self.components["Anim"].setAnimState(state='idleleft')

        if self.speed[0] < 0:
            self.spriteScale[0] *= -1

        elif self.speed[0] > 0:
            self.spriteScale[0] = abs(self.spriteScale[0])
        return super().update()


class TestObject(Object):
    def __init__(self, man, pde, components={}, name="None") -> None:
        super().__init__(man, pde, name, components)

class TestActor(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[32, 32]):
        self.checkForOverlap = True
        self.checkForCollision = True
        self.position = position
        self.scale = scale
        self.direction = 1
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)



    def update(self):
        pass


class TestPlayer(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[18, 30]):

        self.position = position
        self.scale = scale
        self.direction = 1

        self.checkForCollision = True
        self.checkForOverlap = True
        super().__init__(man, pde)

        self.components["PlayerController"] = DebugController(owner=self)
        self.sprite = self.man.add_object(TestSpriteActor(man=man, pde=pde, position=self.position, scale=[32, 32]))



    def update(self):
        self.sprite.rect.center = self.rect.center
        self.sprite.direction = self.direction
        self.sprite.speed = self.speed

        return super().update()

    def overlap(self, obj):
        return super().overlap(obj)





class SpinProjectile(Actor):
    def __init__(self, man, pde, owner, position=[0,0], scale=[16,16], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=True, lifetime=-1):
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.lifetime=lifetime
        self.rotation=rotation
        self.speed = [1, 1]
        self.owner = owner

        super().__init__(man, pde)
        self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\Leukosite\assets\sci_wbloodcell.png', layer=1)


    def move(self, movement):
        pass

    def update(self):
        self.position = self.owner.position
        self.rotation += 1
        return super().update()


