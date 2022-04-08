import os

import pygame
from data.engine.component.component import Component


class AnimManager(Component):
    def __init__(self, owner, sprite, **kwargs) -> None:
        super().__init__(owner, **kwargs)
        self.sprite = sprite
        self.anims = {}
        self.animstate = ''
        self.animframe = 0
        self.animspeed = 0
        self.paused = False

    def addAnimation(self, anim, name, speed=0.2, looping=True, stopFrame=-1, set=False):
        images = []
        for filename in os.listdir(anim):
            f = os.path.join(anim, filename)
            if f in self.owner.pde.sprite_manager.sprites:
                images.append(self.owner.pde.sprite_manager.sprites[f])
            else:
                img = pygame.image.load(f)
                self.owner.pde.sprite_manager.sprites[f] = img
                images.append(img)
        self.anims[str(name)] = [images, speed, looping, stopFrame]
        if set:
            self.setAnimState(state=str(name))

    def setAnimState(self, state):
        if self.animstate != state:
            self.animframe = 0
        self.animstate = state
        self.animspeed = self.anims[self.animstate][1]

    def update(self):
        if not self.paused:
            if int(self.animframe) != int(self.anims[self.animstate][3]):
                self.animframe += self.animspeed
                if self.animframe >= len(self.anims[self.animstate][0]):
                    self.animframe = 0
                else:
                    self.sprite.sprite.ogimage = self.anims[self.animstate][0][int(self.animframe)]
                    self.sprite.sprite.updatetransform()
                    # self.sprite.sprite.image = pygame.transform.scale(self.sprite.sprite.image, ([abs(self.sprite.sprite.parent.spriteScale[0]),abs(self.sprite.sprite.parent.spriteScale[1])]))
                    # self.sprite.sprite.image = pygame.transform.rotate(self.sprite.sprite.image, self.sprite.sprite.parent.spriteRotation)
                    # self.sprite.sprite.rect = self.sprite.sprite.parent.rect
            


    

