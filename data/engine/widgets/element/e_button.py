from data.engine.actor.actor import Actor
from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.widgets.button import Button

class ButtonElement(Actor):
    def __init__(self, man, pde, position=..., scale=..., checkForOverlap=False, checkForCollision=False, useCenterForPosition=False, lifetime=-1):
        super().__init__(man, pde, position, scale, checkForOverlap, checkForCollision, useCenterForPosition, lifetime)

    def construct(self):
        super().construct()
        self.components["Button"] = Button(owner=self, bind=self.clicked)
        return
        
    def clicked(self):
        return