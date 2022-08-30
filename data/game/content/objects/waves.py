import random
from data.game.content.objects.badblood import SickleCell
from data.game.content.objects.cancermanager import CancerManager
from data.game.content.objects.cancerwarning import CancerWarning
from data.game.content.objects.covid import Covid
from data.game.content.objects.covidmanager import CovidManager
from data.game.content.objects.covidwarning import CovidWarning
from data.game.content.objects.wave import Wave


class Wave1(Wave):
    def __init__(self, owner):
        super().__init__(owner)

        self.ticks = 0
        self.presets = [[[0,0], -45], [[640, 0], -135], [[640, 480], 135], [[0, 480], 45]]
        self.spawnvalue = 21 - self.owner.pde.game.difficulty
        self.timeTarget = 2000

    def update(self):
        self.spawnvalue = 21 - self.owner.pde.game.difficulty
        if self.active:
            self.ticks += 1
            if self.ticks == self.spawnvalue and self.owner.pde.game.difficulty != 0:
                self.preset = random.choice(self.presets)
                self.om.add_object(SickleCell(man=self.om, pde=self.owner.pde, position=list(self.preset[0]), rotation=int(self.preset[1]) + random.randint(-30, 30), speed=[3, 3], lifetime=700))
                self.ticks = 0
            self.time += 1
            if self.time == self.timeTarget:
                self.time = 0
                if self.active == True:
                    self.onfinish()
                self.active = False

    def spawnboss(self):
        if self.owner.pde.game.bossesKilled == 0:
            self.boss = self.owner.man.add_object(Covid(man=self.om, pde=self.owner.pde, position=self.warning.position, rotation=0, owner = self))
        elif self.owner.pde.game.bossesKilled == 1:
            self.boss = self.owner.man.add_object(CovidManager(man=self.om, pde=self.owner.pde, position1=self.warning.position, position2=self.warning2.position, owner = self))
        elif self.owner.pde.game.bossesKilled >= 2:
            self.boss = self.owner.man.add_object(CancerManager(man=self.om, pde=self.owner.pde, position=self.warning.position, owner = self))



    def onfinish(self):
        self.timeTarget = 2000
        if self.owner.pde.game.bossesKilled == 0:
            self.warning = self.owner.man.add_object(CovidWarning(man=self.om, pde=self.owner.pde, position=[320,240], rotation=0, owner = self))
        elif self.owner.pde.game.bossesKilled == 1:
            self.warning = self.owner.man.add_object(CovidWarning(man=self.om, pde=self.owner.pde, position=[100,100], rotation=0, owner = self))
            self.warning2 = self.owner.man.add_object(CovidWarning(man=self.om, pde=self.owner.pde, position=[540,100], rotation=0, owner = self, spawnboss = False))
        elif self.owner.pde.game.bossesKilled >= 2:
            self.warning = self.owner.man.add_object(CancerWarning(man=self.om, pde=self.owner.pde, position=[100, 240], rotation=0, owner = self))
        return super().onfinish()