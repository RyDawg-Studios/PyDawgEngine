from data.game.content.objects.badblood import SickleCell
import random

class Wave():
    def __init__(self, owner):
        self.owner = owner
        self.om = owner.man
        self.ticks = 0
        self.presets = [[[0,0], -45], [[640, 0], -135], [[640, 480], 135], [[0, 480], 45]]
        self.spawnvalue = 21 - self.owner.pde.game.difficulty
        self.active = True

    def update(self):
        if self.active:
            self.ticks += 1
            if self.ticks == self.spawnvalue and self.owner.pde.game.difficulty != 0:
                self.preset = random.choice(self.presets)
                self.om.add_object(SickleCell(man=self.om, pde=self.owner.pde, position=list(self.preset[0]), rotation=int(self.preset[1]) + random.randint(-30, 30), speed=[3, 3], lifetime=700))
                self.ticks = 0