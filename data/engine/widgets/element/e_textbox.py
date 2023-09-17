from data.engine.actor.actor import Actor
from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.button import Button
from data.engine.widgets.text import TextComponent
import pygame

class TextBoxElement(Actor):
    def __init__(self, man, pde, position=..., scale=..., checkForOverlap=False, checkForCollision=False, useCenterForPosition=False, lifetime=-1, sprite='', layer=0):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)
        self.sprite = sprite
        self.layer=layer
        self.text = 'Begin typing to enter.'
        self.cleared = False
        self.confirm_event = EventDispatcher()
        self.checkForCollision=False
        self.checkForOverlap=False
        self.moveable=False

    def construct(self):
        super().construct()
        self.components["Text"] = TextComponent(owner=self, text=self.text, font=pygame.font.SysFont('impact.ttf', 16), layer=3)
        self.pde.input_manager.on_input_event.bind(self.on_input)
        return
        
    def update(self):
        super().update()

    def on_input(self, key):
        if not self.cleared:
            self.text = ''
            self.cleared = True

        if key == '\r':
            self.confirm_event.call(self.text)
            return
        elif key == '\x08':
            self.text = self.text[:-1]
            self.components["Text"].sprite.text = self.text 
            return

        self.text += key
        self.components["Text"].sprite.text = self.text 


    