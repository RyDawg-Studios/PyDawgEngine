from turtle import pos
import pygame
from data.engine.actor.actor import Actor
from data.engine.ai.ai_component import AIComponent
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.anim.anim_manager import AnimManager
from data.engine.anim.anim_sprite import AnimSprite
from data.engine.debug.debugController import DebugController
from data.engine.object.object import Object
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent


class TestSpriteActor(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[32, 32]):
        super().__init__(man, pde, position=position, scale=scale, checkForCollision=False, checkForOverlap=False)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)

        self.components["Anim"] = AnimManager(owner=self, sprite=self.components["Sprite"])

        self.components["Anim"].addAnimation(name='runright', anim=r'data\assets\anims\runright', speed=0.1, set=True, stopFrame=-1)
        self.components["Anim"].addAnimation(name='runleft', anim=r'data\assets\anims\runleft', speed=0.1, set=True, stopFrame=-1)

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
            self.scale[0] *= -1

        elif self.speed[0] > 0:
            self.scale[0] = abs(self.scale[0])

        #self.components["Sprite"].sprite.rotation += 1
        
        return super().update()


class TestObject(Object):
    def __init__(self, man, pde, components={}, name="None") -> None:
        super().__init__(man, pde, name, components)

class TestActor(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[32, 32]):
        self.direction = 1
        self.hp = 100
        super().__init__(man, pde, position=position, scale=scale, checkForCollision=True, checkForOverlap=True, useCenterForPosition=True)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=2)
    def takedamage(self, obj):
        return True

    def update(self):
        pass


class TestPlayer(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[18, 30]):
        super().__init__(man, pde)
        self.direction = 1

        super().__init__(man, pde, position=position, scale=scale, checkForCollision=True, checkForOverlap=True)
        self.components["PlayerController"] = DebugController(owner=self)
        self.sprite = self.man.add_object(TestSpriteActor(man=man, pde=pde, position=self.position, scale=[32, 32]))



    def update(self):
        self.sprite.rect.center = self.rect.center
        self.sprite.direction = self.direction
        self.sprite.speed = self.movement

        return super().update()

    def overlap(self, obj):
        return super().overlap(obj)





class SpinProjectile(Actor):
    def __init__(self, man, pde, player, owner=None, position=[0,0], scale=[16,16], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=True, lifetime=-1):
        super().__init__(man, pde)
        self.owner = owner

        super().__init__(man, pde, position=position, scale=scale, rotation=rotation, checkForCollision=False, checkForOverlap=True)

        self.proj = self.components["Projectile"] = ProjectileComponent(owner=self, rotation=rotation, speed=self.speed)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\debug.png', layer=1)


    def move(self, movement):
        pass

    def update(self):
        self.proj.speed = self.speed
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()


