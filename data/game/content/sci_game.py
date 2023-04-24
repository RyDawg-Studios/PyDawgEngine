from data.engine.debug.stressTestLevel import StressLevel
from data.engine.game.game import Game
from data.game.content.levels.battle import BattleLevel
from data.game.content.levels.game_over import GameOverLevel
from data.game.content.levels.test import LeukositeTest
from data.game.content.levels.title import TitleLevel


class Leukosite(Game):
    def __init__(self, pde):
        super().__init__(pde)
        self.difficulty = 10
        self.score = 0
        self.bossesKilled = 0

    def activate(self):
        self.loadtitlelevel()

    def loadstresslevel(self):
        self.pde.level_manager.addelevel(level=StressLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
    def loadbattlelevel(self):
        self.pde.level_manager.addlevel(level=BattleLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
    def loadgameoverlevel(self, pos):
        self.pde.level_manager.addlevel(level=GameOverLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True, pos=pos)

    def loadtitlelevel(self):
        self.pde.level_manager.addlevel(level=TitleLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)