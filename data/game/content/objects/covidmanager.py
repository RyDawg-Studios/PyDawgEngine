from random import random

from data.engine.object.object import Object
from data.game.content.objects.cancerboss import CancerCell
from data.game.content.objects.doublecovid import DoubleCovid

class CovidManager(Object):
    def __init__(self, man, pde, position1, position2, owner):
        super().__init__(man, pde)
        self.pde = pde
        self.segments = []
        self.owner = owner
        self.segments.append(man.add_object(DoubleCovid(man=man, pde=pde, position=position1, rotation=0, owner=self, bossman=self)))
        self.segments.append(man.add_object(DoubleCovid(man=man, pde=pde, position=position2, rotation=0, owner=self, bossman=self)))

        self.done = False

    def update(self):
        if len(self.segments) <= 0:
            if not self.done:
                self.done = True
                self.owner.active = True
                self.pde.game.bossesKilled += 1
                self.pde.game.score += 16000
                self.deconstruct()


                
        return super().update()