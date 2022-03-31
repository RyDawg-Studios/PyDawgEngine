from data.engine.actor.actor import Actor
from data.engine.anim.anim_manager import AnimManager
from data.engine.sprite.sprite_component import SpriteComponent
from data.game.content.objects.mario_controller import MarioController

class MarioSpriteActor(Actor):
    def __init__(self, man, pde, position=[0,0], scale=[16, 16]):
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


class MarioPlayer(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[16, 32]):

        self.position = position
        self.scale = scale
        self.direction = 1

        self.checkForCollision = True
        self.checkForOverlap = True
        super().__init__(man, pde)

        self.components["PlayerController"] = MarioController(owner=self)
        self.sprite = self.man.add_object(MarioSpriteActor(man=man, pde=pde, position=self.position, scale=[32, 32]))
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\me.png', layer=2)

    
    def update(self):
        self.scrollcameratocenter()
        self.movement[1] += .5
        if self.collideInfo["Bottom"]:
            self.movement[1] = 0

        self.sprite.rect.center = self.rect.center
        self.sprite.speed = self.speed
        self.sprite.direction = self.direction
        return super().update()


        