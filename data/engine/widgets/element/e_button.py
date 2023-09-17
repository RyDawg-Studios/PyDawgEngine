from data.engine.actor.actor import Actor
from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.button import Button

class ButtonElement(Actor):
    def __init__(self, man, pde, position=[0, 0], scale=[32, 32], checkForOverlap=False, checkForCollision=False, useCenterForPosition=False, lifetime=-1, bind=None, sprite='', layer=0):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.sprite = sprite
        self.bind = bind
        self.layer=layer
        self.checkForCollision=False
        self.checkForOverlap=False
        self.moveable=False

    def construct(self):
        super().construct()
        self.components["Button"] = Button(owner=self, bind=self.clicked)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=self.sprite, layer=self.layer)
        return
        
    def clicked(self):
        self.bind()