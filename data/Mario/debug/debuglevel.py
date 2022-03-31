import random
from data.engine.debug.debugObject import TestActor, TestPlayer
from data.engine.level.level import Level
from data.game.content.objects.mario import MarioPlayer


class MarioDebugLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)


        self.objectManager.add_object(MarioPlayer(man=self.objectManager, pde=pde, position=[200, 200]))


        for r in range(-100, 100):
            if r != 10:
                for c in range(1, 3):
                    self.objectManager.add_object(TestActor(man=self.objectManager, pde=pde, position=[r*32, 492-c*32]))





