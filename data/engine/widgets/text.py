import pygame
from pygame.sprite import AbstractGroup
from data.engine.component.component import Component

class Sprite(pygame.sprite.Sprite):
    def __init__(self, parent, rotation, scale, font, text, color, layer: AbstractGroup) -> None:
        super().__init__()

        self.parent = parent
        self.layer = layer
        self.opacity = 255

        self.text = text
        self.font = font
        self.color = color

        self.scale = scale
        self.rotation = rotation
        

        self.image = self.font.render(str(self.text), True, self.color)
        self.ogimage = self.image

        self.rect = self.ogimage.get_rect()

        self.updatetransform()
 
        #add sprite to sprite layer
        parent.pde.display_manager.group.add(self)

    def update(self):
        if self.text == '':
            self.text = ' '
        self.updatetransform()
        super().update()

    def updatetransform(self):
        self.scale = self.font.size(str(self.text))

        img = self.font.render(str(self.text), True, self.color)
        img = pygame.transform.scale(img, self.scale)
        img = pygame.transform.rotate(img, self.rotation)
        self.image = img
        self.image.set_alpha(self.opacity)
        self.rect = self.image.get_rect()
        self.rect.center = self.parent.rect.center

    
    def deconstruct(self):
        self.kill()
        del self




class TextComponent(Component):
    def __init__(self, owner, font, layer=0, text='textVar', color=(0, 0, 0), **kwargs) -> None:
        super().__init__(owner, **kwargs)
        self.sprite = Sprite(parent=owner, layer=layer, rotation=self.owner.rotation, scale=self.owner.scale, text=text, font=font, color=color)
    
    def update(self):
        self.sprite.update()

    def deconstruct(self):
        self.sprite.deconstruct()
        super().deconstruct()
