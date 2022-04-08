import random
from data.engine.debug.debugObject import SpinProjectile, TestActor, TestPlayer
from data.engine.level.level import Level


class DebugLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)
        self.changebackground(r'data\assets\sprites\bg.png')


        p = self.objectManager.add_object(TestPlayer(man=self.objectManager, pde=pde, position=[200, 200], scale=[32, 32]))
        self.objectManager.add_object(TestActor(man=self.objectManager, pde=pde, position=[125, 125]))
        self.objectManager.add_object(TestActor(man=self.objectManager, pde=pde, position=[100, 100]))
        self.objectManager.add_object(SpinProjectile(man=self.objectManager, pde=pde, position=[200, 200], player=p))



