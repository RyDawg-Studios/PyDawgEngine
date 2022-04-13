from data.engine.ai.ai_state import AIState
from data.engine.fl.world_fl import objectlookatposition
import random

from data.topdownshooter.content.objects.enemy.aitarget import AIMovementTarget


class debugAI(AIState):
    def __init__(self, man, pde, owner):
        self.destination = [random.randint(0, 640), random.randint(0, 480)]
        self.waitticks = 0
        self.waittime = random.randint(0, 40)
        self.destactor = man.add_object(obj=AIMovementTarget(man, pde))
        super().__init__(man, pde, owner)

    def update(self):
        if abs(self.owner.owner.position[0] - self.destination[0]) < 5 and abs(self.owner.owner.position[1] - self.destination[1]) < 5:
            self.waitticks += 1
            self.owner.owner.speed = [0, 0]
            if self.waitticks >= self.waittime:
                self.waitticks = 0
                self.owner.owner.speed = self.owner.owner.defaultspeed
                self.destination = [random.randint(0, 640), random.randint(0, 480)]
        else:
            self.owner.owner.rotation = objectlookatposition(self.owner.owner, self.destination)
        return super().update()