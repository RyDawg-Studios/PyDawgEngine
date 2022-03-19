import pygame
from data.engine.anim.anim_manager import AnimManager
from data.engine.anim.anim_sprite import AnimSprite
from data.engine.debug.debugController import DebugController
from data.engine.object.object import Object
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.player.player_controller import PlayerController
from data.engine.action.actions.action import Action

class TestObject(Object):
    def __init__(self, man, pde, components={}, name="None") -> None:
        super().__init__(man, pde, name, components)

class TestActor(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[30, 30]):
        self.checkForCollision = True
        self.checkForOverlap = True
        self.position = position
        self.scale = scale
        self.direction = 1
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)

    def update(self):
        return super().update()



class TestPlayer(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[30, 30]):

        self.position = position
        self.scale = scale
        self.direction = 1

        self.collideRect = pygame.rect.Rect(0, 0, 8, 16)

        self.checkForCollision = True
        self.checkForOverlap = True

    
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)
        self.components["CollideBox"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=2)


        self.components["Anim"] = AnimManager(owner=self, layer=2, sprite=self.components["Sprite"])
        self.components["Anim"].addAnimation(name='runright', anim=r'data\assets\anims\runright', speed=0.2, set=True, stopFrame=-1)
        self.components["Anim"].addAnimation(name='runleft', anim=r'data\assets\anims\runleft', speed=0.2, set=True, stopFrame=-1)

        self.components["Anim"].addAnimation(name='idleright', anim=r'data\assets\anims\idleright', speed=0.2, set=False, stopFrame=-1)
        self.components["Anim"].addAnimation(name='idleleft', anim=r'data\assets\anims\idleleft', speed=0.2, set=False, stopFrame=-1)

        self.components["PlayerController"] = DebugController(owner=self)

        self.collideRect.center = self.rect.center

    def update(self):
        pygame.display.set_caption(str(self.overlapInfo))
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

    def overlap(self, obj):
        return super().overlap(obj)


class TestAction(Action):
    def __init__(self, queue, name) -> None:
        super().__init__(queue, name)

    def update(self):
        print("Action Updated")
        self.finished = True
        return






        


