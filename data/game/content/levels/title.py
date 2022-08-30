from data.engine.level.level import Level
from data.game.content.objects.bgBlood_spawner import BloodSpawner
from data.game.content.objects.collider import Collider
from data.game.content.objects.difficulty_setter import DifficultyChangerActor, DifficultyTextActor, ScoreTextActor
from data.game.content.objects.foreground_obj import Fg
from data.game.content.objects.logo import Logo
from data.game.content.objects.signature import SignatureActor
from data.game.content.objects.startbutton import StartButtonActor
from data.game.content.player.DawgTalePlayer import DawgTalePlayer
from data.game.content.objects.wave_manager import WaveManager
from data.game.content.objects.wave import Wave

class TitleLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        self.rot=0
        super().__init__(man, pde)
        self.changebackground(r'data\game\assets\black.png')

        self.objectManager.add_object(Logo(man=self.objectManager, pde=pde, position=[310, 50]))
        self.objectManager.add_object(SignatureActor(man=self.objectManager, pde=pde, position=[580, 460]))

        self.objectManager.add_object(StartButtonActor(man=self.objectManager, pde=pde, position=[310, 340]))
        self.objectManager.add_object(DifficultyChangerActor(man=self.objectManager, pde=pde, position=[310, 140], state='up'))
        self.objectManager.add_object(DifficultyChangerActor(man=self.objectManager, pde=pde, position=[310, 240], state='down'))
        self.objectManager.add_object(DifficultyTextActor(man=self.objectManager, pde=pde, position=[310, 190]))
        self.objectManager.add_object(ScoreTextActor(man=self.objectManager, pde=pde, position=[310, 100], scale=[60, 20]))





    def update(self):
        return super().update()
        