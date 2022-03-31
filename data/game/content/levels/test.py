from data.engine.debug.debugObject import SpinProjectile, TestActor, TestPlayer
from data.engine.level.level import Level
from data.game.content.objects.cancermanager import CancerManager
from data.game.content.objects.collider import Collider
from data.game.content.objects.covidmanager import CovidManager
from data.game.content.player.DawgTalePlayer import DawgTalePlayer


class LeukositeTest(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)
        self.changebackground(r'data\assets\sprites\bg.png')

        player = self.objectManager.add_object(DawgTalePlayer(man=self.objectManager, pde=pde, position=[310, 400]))
        self.objectManager.add_object(SpinProjectile(man=self.objectManager, pde=pde, position=[120, 120], owner=player))



        self.objectManager.add_object(Collider(man=self.objectManager, pde=pde, position=[0,-50], scale=[640, 40])) #Top
        self.objectManager.add_object(Collider(man=self.objectManager, pde=pde, position=[0,490], scale=[640, 40])) #Bottom
        self.objectManager.add_object(Collider(man=self.objectManager, pde=pde, position=[-20,0], scale=[10, 480])) #Left
        self.objectManager.add_object(Collider(man=self.objectManager, pde=pde, position=[660,0], scale=[10, 480])) #Right
    



