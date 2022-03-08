from data.engine.debug.debugLevel import TestLevel
from data.engine.debug.stressTestLevel import StressLevel
from data.game.content.levels.battle import BattleLevel
from data.game.content.levels.game_over import GameOverLevel
from data.game.content.levels.title import TitleLevel


class Game:
    def __init__(self, pde):
        self.pde = pde

    def activate(self):
        self.pde.level_manager.addlevel(level=TitleLevel(man=self.pde.level_manager, pde=self.pde), 
                                                                        name="Main", active=True)
        self.player_controllers = []

    def update(self):
        pass

    def loadstresslevel(self):
        self.pde.level_manager.addlevel(level=StressLevel(man=self.pde.level_manager, pde=self.pde), 
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
