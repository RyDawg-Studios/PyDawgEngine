from data.engine.level.level import Level
from data.game.content.objects.bgBlood_spawner import BloodSpawner
from data.game.content.objects.collider import Collider
from data.game.content.objects.difficulty_setter import ScoreTextActor
from data.game.content.objects.foreground_obj import Fg
from data.game.content.objects.protein import ProteinSpawner
from data.game.content.player.DawgTalePlayer import DawgTalePlayer
from data.game.content.objects.wave_manager import WaveManager
from data.game.content.objects.waves import Wave1

class BattleLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        self.rot=0
        super().__init__(man, pde)
        self.changebackground(r'data\game\assets\sci_vessel_bg.png')

        self.objectManager.add_object(DawgTalePlayer(man=self.objectManager, pde=pde, position=[310, 400]))
        self.objectManager.add_object(BloodSpawner(man=self.objectManager, pde=pde, position=[640, 0]))
        self.objectManager.add_object(Fg(man=self.objectManager, pde=pde, position=[0,0]))
        self.objectManager.add_object(WaveManager(man=self.objectManager, pde=pde, wave=Wave1))
        self.objectManager.add_object(ScoreTextActor(man=self.objectManager, pde=pde, position=[320, 15], scale=[60, 20]))
        #self.objectManager.add_object(ProteinSpawner(man=self.objectManager, pde=pde))



        self.objectManager.add_object(Collider(man=self.objectManager, pde=pde, position=[0,-50], scale=[640, 40])) #Top
        self.objectManager.add_object(Collider(man=self.objectManager, pde=pde, position=[0,490], scale=[640, 40])) #Bottom
        self.objectManager.add_object(Collider(man=self.objectManager, pde=pde, position=[-20,0], scale=[10, 480])) #Left
        self.objectManager.add_object(Collider(man=self.objectManager, pde=pde, position=[660,0], scale=[10, 480])) #Right





    def update(self):
        return super().update()
        