import pygame
from pygame.sprite import AbstractGroup
from data.engine.component.component import Component
from data.engine.fl.sys_fl import resource_path
import math

class Sprite(pygame.sprite.Sprite):
    def __init__(self, parent, sprite, rotation, scale, layer: AbstractGroup) -> None:
        super().__init__()

        self.parent = parent
        self.layer= layer

        self.sprite = sprite

        self.scale = scale
        self.rotation = rotation


        self.image = pygame.image.load(self.sprite)
        self.image = pygame.transform.scale(self.image, (self.scale[0],self.scale[1]))
        self.image = pygame.transform.rotate(self.image, self.rotation)
 



        if layer in parent.pde.display_manager.surfs:
            parent.pde.display_manager.surfs[self.layer].append(self)
        else:
            parent.pde.display_manager.createsurf(id=layer)
            parent.pde.display_manager.surfs[self.layer].append(self)

    def update(self):
        super().update()

    
    def deconstruct(self):
        self.kill()
        try:
            if self in self.parent.pde.display_manager.surfs[self.layer]:
                self.parent.pde.display_manager.surfs[self.layer].remove(self)
            else:
                #print(f"Warning: Invalid Sprite Removal\nParent: {self.parent}\nSprite: {self}\nLayer: {self.layer}\nSurface: {self.parent.pde.display_manager.surfs[self.layer]}")
                pass
        except:
            print(f'Warning: Attempted to access invalid Sprite Layer: {self.layer}')
            pass
        del self




class SpriteComponent(Component):
    def __init__(self, owner, sprite, layer=0, **kwargs) -> None:
        super().__init__(owner, **kwargs)

        if self.owner.useSpriteRectForCollision:
            self.owner.rect = self.sprite.image.get_rect()


        self.sprite = Sprite(parent=owner, sprite=sprite, layer=layer, rotation=self.owner.spriteRotation, scale=self.owner.spriteScale)


    
    def update(self):
        self.sprite.update()

    def deconstruct(self):
        self.sprite.deconstruct()
        super().deconstruct()
