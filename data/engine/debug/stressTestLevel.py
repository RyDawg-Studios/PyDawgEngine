from data.engine.level.level import Level
from data.engine.debug.debugObject import TestActor, TestPlayer

import random

class StressLevel(Level):
    def __init__(self, man, pde) -> None:
        super().__init__(man, pde)
        self.changebackground(r'assets\debug\sprites\xp.png')

        self.objectManager.objects["Player"] = TestPlayer(man=self.objectManager, pde=pde)
        for obj in range(0, 50):
            self.objectManager.objects["Enemy" + str(obj)] = TestActor(man=self.objectManager, pde=pde, position=[random.randint(0, 700), random.randint(0,500)], scale=[32, 32])