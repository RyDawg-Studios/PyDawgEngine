from random import random

from data.engine.object.object import Object
from data.game.content.objects.cancerboss import CancerCell

class CancerManager(Object):
    def __init__(self, man, pde, position, owner):
        self.segments = []
        self.owner = owner
        self.segments.append(man.add_object(CancerCell(man=man, pde=pde, position=position, rotation=0, owner=self, bossman=self)))

        self.done = False
        super().__init__(man, pde)

    def update(self):
        super().update()
        if len(self.segments) <= 0:
            if not self.done:
                self.done = True
                self.owner.active = True
                self.owner.owner.pde.game.bossesKilled += 1
                self.owner.owner.pde.game.score += 16000
                self.deconstruct()
                