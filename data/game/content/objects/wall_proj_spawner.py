import random
from data.engine.actor.actor import Actor
from data.engine.projectile.projectile import Projectile
from data.game.content.objects.wall_projectile import WallProjectile


class WallProjectileSpawner(Actor):
    def __init__(self, man, pde, position):
        self.position = position
        super().__init__(man, pde)

        self.checkForOverlap = False
        self.checkForCollision = False

        self.ticks = 0

        self.rot=0

        self.projspeed = random.randint(1,4)

        self.presets = {'left': [[0,0], 0], 'right': [[640, 0], 180]}


        self.projlifetime = 700
        self.ticktime = random.randint(150, 200)



    def update(self):
        self.ticks += 1

        if self.ticks == self.ticktime:
            self.projspeed = random.randint(3,6)
            self.preset = random.choice(list(self.presets.values()))
            self.man.add_object(WallProjectile(man=self.man, pde=self.pde, position=[self.preset[0][0], self.preset[0][1]], rotation=self.preset[1], speed=[self.projspeed,self.projspeed], lifetime=self.projlifetime)) 
            self.ticks = 0
