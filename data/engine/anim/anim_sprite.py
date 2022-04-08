import os
from data.engine.component.component import Component

import pygame
from pygame.sprite import AbstractGroup
from data.engine.component.component import Component


class Sprite(pygame.sprite.Sprite):
    def __init__(self, parent, images, layer: AbstractGroup) -> None:
        super().__init__()

        self.parent = parent
        self.layer = layer
        self.animframe = 0
        self.framelen = 2

        self.images = images

        parent.pde.display_manager.group.add(self)

    def update(self):
        self.animframe += 0.3
        if self.animframe < len(self.images):
            self.ogimage = self.images[int(self.animframe)]
            self.image = pygame.transform.scale(self.ogimage, (self.parent.spriteScale[0],self.parent.spriteScale[1]))
            self.image = pygame.transform.rotate(self.ogimage, self.parent.spriteRotation)
            self.rect = self.parent.rect
        else:
            self.animframe = 0

        super().update()

    
    def deconstruct(self):
        self.kill()
        del self


class AnimSprite(Component):
    def __init__(self, owner, anim, time=1, layer=0, **kwargs):
        super().__init__(owner, **kwargs)

        self.anim = anim
        self.time = time
        self.layer = layer
        self.images = []

    
        # iterate over files in
        # that directory
        for filename in os.listdir(self.anim):
            f = os.path.join(self.anim, filename)
            # checking if it is a file
            #Use sprite from cache if already loaded, otherwise load it and add it to cache
            if f in self.owner.pde.sprite_manager.sprites:
                self.images.append(self.owner.pde.sprite_manager.sprites[f])
            else:
                img = pygame.image.load(f)
                self.owner.pde.sprite_manager.sprites[f] = img
                self.images.append(img)

        

        self.anim = Sprite(parent=self.owner, images=self.images, layer=self.layer)

    

        


