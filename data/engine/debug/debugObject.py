import pygame
from data.engine.object.object import Object
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.player.player_controller import PlayerController
from data.engine.action.actions.action import Action

class TestObject(Object):
    def __init__(self, man, pde, components={}, name="None") -> None:
        super().__init__(man, pde, name, components)

class TestActor(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[30, 30]):
        self.checkForCollision = True
        self.position = position
        self.scale = scale
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'assets\debug\sprites\pixel_measure.png', layer=0)

class TestPlayer(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[30, 30]):

        self.position = position
        self.scale = scale
    
        super().__init__(man, pde)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite='assets\debug\sprites\me.png', layer=2)
        self.components["PlayerController"] = PlayerController(owner=self)

class TestAction(Action):
    def __init__(self, queue, name) -> None:
        super().__init__(queue, name)

    def update(self):
        print("Action Updated")
        self.finished = True
        return






        


