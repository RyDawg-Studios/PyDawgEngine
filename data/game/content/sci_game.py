from data.engine.debug.stressTestLevel import StressLevel
from data.engine.game.game import Game
from data.game.content.levels.battle import BattleLevel
from data.game.content.levels.game_over import GameOverLevel
from data.game.content.levels.title import TitleLevel


class Eukaryosite(Game):
    def __init__(self, pde):
        super().__init__(pde)
        self.difficulty = 10
        self.score = "No Score"

    def activate(self):
        self.pde.level_manager.changelevel(level=TitleLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)

    def loadstresslevel(self):
        self.pde.level_manager.changelevel(level=StressLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
    def loadbattlelevel(self):
        self.pde.level_manager.changelevel(level=BattleLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
    def loadgameoverlevel(self, pos):
        self.pde.level_manager.addlevel(level=GameOverLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True, pos=pos)

    def loadtitlelevel(self):
        self.pde.level_manager.changelevel(level=TitleLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)