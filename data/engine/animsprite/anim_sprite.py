from data.engine.component.component import Component


class AnimSprite(Component):
    def __init__(self, owner, anim, time=1, **kwargs):
        super().__init__(owner, **kwargs)

        self.anim = anim
        self.time = time

        


