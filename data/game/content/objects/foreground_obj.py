from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent


class Fg(Actor):
    def __init__(self, man, pde, position=[50, 50], scale=[640, 480]):
        self.checkForCollision = False
        self.checkForOverlap = False
        self.position = position
        self.scale = scale
        super().__init__(man, pde)
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\sci_vessel_fg.png', layer=6)

        self.components.pop("DebugButton")