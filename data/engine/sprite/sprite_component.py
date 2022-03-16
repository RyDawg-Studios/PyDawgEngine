import pygame
from pygame.sprite import AbstractGroup
from data.engine.component.component import Component


class Sprite(pygame.sprite.Sprite):
    def __init__(self, parent, sprite, rotation, scale, layer: AbstractGroup) -> None:
        super().__init__()

        self.parent = parent
        self.layer = layer

        self.sprite = sprite

        self.scale = scale
        self.rotation = rotation



        #Use sprite from cache if already loaded, otherwise load it and add it to cache
        if self.sprite in self.parent.pde.sprite_manager.sprites:
            self.image = self.parent.pde.sprite_manager.sprites[self.sprite]
        else:
            self.image = pygame.image.load(self.sprite)
            self.parent.pde.sprite_manager.sprites[self.sprite] = self.image


        #apply approprite sprite transformation
        self.image = pygame.transform.scale(self.image, (self.scale[0],self.scale[1]))
        self.image = pygame.transform.rotate(self.image, self.rotation)

        self.rect = self.image.get_rect()
 
        #add sprite to sprite layer
        parent.pde.display_manager.group.add(self)

    def update(self):
        self.rect = self.parent.rect
        super().update()

    
    def deconstruct(self):
        self.kill()
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
