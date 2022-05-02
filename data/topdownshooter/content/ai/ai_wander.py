from data.engine.ai.ai_state import AIState
from data.engine.fl.world_fl import objectlookatposition, getpositionlookatvector
import random
from data.topdownshooter.content.ai.ai_target import AITarget

from data.topdownshooter.content.objects.enemy.aitarget import AIMovementTarget


class WanderAI(AIState):
    def __init__(self, man, pde, owner):
        self.target = man.add_object(AITarget(man=man, pde=pde, position=[random.randint(0, 600), random.randint(0, 400)]))
        self.waitticks = 0
        self.destination = self.target.position
        self.waitticks = 0
        self.waittime = random.randint(0, 40)
        self.travelticks = 0
        self.r = 0
        super().__init__(man, pde, owner)

    def update(self):
        if abs(self.owner.owner.position[0] - self.destination[0]) < 5 and abs(self.owner.owner.position[1] - self.destination[1]) < 5:
            self.waitticks += 1
            self.owner.owner.movement = [0, 0]
            if self.waitticks >= self.waittime:
                self.picknewlocation()
        else:
            self.travelticks += 1
            if self.travelticks >= 300:
                self.picknewlocation()
            self.r = getpositionlookatvector(self.owner.owner, self.destination)
            self.owner.owner.movement = self.r
        return super().update()


    def picknewlocation(self):
        self.waitticks = 0
        self.target.deconstruct()
        self.target = self.man.add_object(AITarget(man=self.man, pde=self.pde, position=[random.randint(0, 600), random.randint(0, 400)]))
        self.destination = self.target.position
        self.travelticks = 0