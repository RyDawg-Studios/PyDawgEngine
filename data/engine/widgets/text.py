import pygame
from pygame.sprite import AbstractGroup
from data.engine.component.component import Component

class Sprite(pygame.sprite.Sprite):
    def __init__(self, parent, rotation, scale, font, text, color, layer: AbstractGroup) -> None:
        super().__init__()

        self.parent = parent
        self.layer= layer

        self.text = text
        self.font = font
        self.color = color

        self.scale = scale
        self.rotation = rotation

        self.image = self.font.render(str(self.parent.__getattribute__(self.text)), True, self.color)
        self.image = pygame.transform.scale(self.image, (self.scale[0],self.scale[1]))
        self.image = pygame.transform.rotate(self.image, self.rotation)
 
        self.rect = self.image.get_rect()

    def update(self):
        #self.image = self.font.render(str(self.parent.__getattribute__(self.text)), True, self.color)
        self.rect = self.parent.rect
        super().update()

    
    def deconstruct(self):
        self.kill()
        del self




class TextComponent(Component):
    def __init__(self, owner, font, layer=0, text='textVar', color=(0, 0, 0), **kwargs) -> None:
        super().__init__(owner, **kwargs)


        self.sprite = Sprite(parent=owner, layer=layer, rotation=self.owner.spriteRotation, scale=self.owner.spriteScale, text=text, font=font, color=color)


    
    def update(self):
        self.sprite.update()

    def deconstruct(self):
        self.sprite.deconstruct()
        super().deconstruct()
