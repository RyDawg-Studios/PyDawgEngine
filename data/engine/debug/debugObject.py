import pygame
from data.engine.actor.actor import Actor
from data.engine.ai.ai_component import AIComponent
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.debug.debugAI import debugAI
from data.engine.anim.anim_manager import AnimManager
from data.engine.anim.anim_sprite import AnimSprite
from data.engine.debug.debugController import DebugController
from data.engine.object.object import Object
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import objectlookattarget
from data.engine.sprite.sprite_component import SpriteComponent

class TestRepObject(Object):
    def __init__(self, man, pde):
        super().__init__(man, pde)
        self.replicate = True
        self.replicable_attributes = [
            "count"
        ]
        self.replication_id = 'test_rep_object'

        self.count = 0

    def construct(self):
        super().construct()

        print(self.count)


class TestSpriteActor(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[32, 32]):
        super().__init__(man, pde)
        self.checkForCollision = False
        self.checkForOverlap = False
        self.position = position
        self.scale = scale

    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)

        self.components["Anim"] = AnimManager(owner=self, sprite=self.components["Sprite"])

        self.components["Anim"].addAnimation(name='runright', anim=r'data\assets\anims\runright', speed=0.2, set=True, stopFrame=-1)
        self.components["Anim"].addAnimation(name='runleft', anim=r'data\assets\anims\runleft', speed=0.2, set=True, stopFrame=-1)

        self.components["Anim"].addAnimation(name='idleright', anim=r'data\assets\anims\idleright', speed=0.2, set=False, stopFrame=-1)
        self.components["Anim"].addAnimation(name='idleleft', anim=r'data\assets\anims\idleleft', speed=0.2, set=False, stopFrame=-1)

    def update(self):
        if self.movement[0] > 0:
            self.components["Anim"].setAnimState(state='runright')

        elif self.movement[0] < 0:
            self.components["Anim"].setAnimState(state='runleft')

        else:
            if self.direction == 1:
                self.components["Anim"].setAnimState(state='idleright')
            if self.direction == -1:
                self.components["Anim"].setAnimState(state='idleleft')

        if self.movement[0] < 0:
            self.spriteScale[0] *= -1

        elif self.movement[0] > 0:
            self.spriteScale[0] = abs(self.spriteScale[0])

        #self.components["Sprite"].sprite.rotation += 1
        
        return super().update()


class TestObject(Object):
    def __init__(self, man, pde, components={}, name="None") -> None:
        super().__init__(man, pde, name, components)

class TestActor(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[32, 32]):
        super().__init__(man, pde)
        self.checkForOverlap = True
        self.checkForCollision = True
        self.position = position
        self.scale = scale
        self.direction = 1
        self.hp = 100
        self.useCenterForPosition = True
    
    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=2)

    def takedamage(self, obj):
        return True

    def update(self):
        pass


class TestPlayer(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[18, 30]):
        super().__init__(man, pde)

        self.position = position
        self.scale = scale
        self.direction = 1

        self.checkForCollision = True
        self.checkForOverlap = True


    def construct(self):
        super().construct()
        self.components["PlayerController"] = DebugController(owner=self)
        self.sprite = self.man.add_object(TestSpriteActor(man=self.man, pde=self.pde, position=self.position, scale=[32, 32]))

        self.replicate = True
        self.replicateInfo = {'position': self.position, 'sprite': r'data\assets\sprites\me.png'}

    def update(self):
        self.sprite.rect.center = self.rect.center
        self.sprite.direction = self.direction
        self.sprite.speed = self.speed

        return super().update()

    def overlap(self, obj):
        return super().overlap(obj)

    def serialize(self):
        data = bytes(str(self.position), 'utf-8')
        return super().serialize(data)

    def sendself(self):
        print(self.serialize())





class SpinProjectile(Actor):
    def __init__(self, man, pde, player, owner=None, position=[0,0], scale=[16,16], speed=[1,1], rotation=0, checkForCollision=False, checkForOverlap=True, lifetime=-1):
        super().__init__(man, pde)
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.lifetime=lifetime
        self.rotation=rotation
        self.player = player
        self.speed = [2, 2]
        self.owner = owner


    def construct(self):
        super().construct()
        self.proj = self.components["Projectile"] = ProjectileComponent(owner=self, rotation=self.rotation, speed=self.speed)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\debug.png', layer=1)
        ai = self.components["AI"] = AIComponent(owner=self)
        ai.addstate(name="default", state=debugAI)

    def move(self, movement):
        pass

    def update(self):
        self.proj.speed = self.speed
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()


