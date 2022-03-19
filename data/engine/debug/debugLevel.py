from data.engine.debug.debugObject import TestActor, TestPlayer
from data.engine.level.level import Level


class DebugLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)
        self.changebackground(r'data\assets\sprites\bg.png')


        self.objectManager.add_object(TestPlayer(man=self.objectManager, pde=pde,position=[90, 50]))
        self.objectManager.add_object(TestActor(man=self.objectManager, pde=pde))

