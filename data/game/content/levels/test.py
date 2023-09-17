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



    



