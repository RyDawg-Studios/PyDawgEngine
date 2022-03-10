import random
from data.game.content.objects.badblood import SickleCell
from data.game.content.objects.covid import Covid
from data.game.content.objects.wave import Wave


class Wave1(Wave):
    def __init__(self, owner):
        super().__init__(owner)

        self.ticks = 0
        self.presets = [[[0,0], -45], [[640, 0], -135], [[640, 480], 135], [[0, 480], 45]]
        self.spawnvalue = 21 - self.owner.pde.game.difficulty
        self.timeTarget = 2000

    def update(self):
        if self.active:
            self.ticks += 1
            if self.ticks == self.spawnvalue and self.owner.pde.game.difficulty != 0:
                self.preset = random.choice(self.presets)
                self.om.add_object(SickleCell(man=self.om, pde=self.owner.pde, position=list(self.preset[0]), rotation=int(self.preset[1]) + random.randint(-30, 30), speed=[3, 3], lifetime=700))
                self.ticks = 0
            return super().update()

    def onfinish(self):
        self.boss = self.owner.man.add_object(Covid(man=self.om, pde=self.owner.pde, position=[320,240], rotation=0, owner = self))
        return super().onfinish()