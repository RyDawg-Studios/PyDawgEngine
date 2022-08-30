import random
from data.engine.actor.actor import Actor
from data.engine.projectile.projectile import Projectile
from data.game.content.objects.wall_projectile import WallProjectile


class ProjectileSpawner(Actor):
    def __init__(self, man, pde, position):
        self.position = position
        super().__init__(man, pde)

        self.checkForOverlap = False
        self.checkForCollision = False


        self.rot=0

        self.state = 'Single'
        self.done = False

        self.rotrate = random.randrange(-360.0, 360.0)
        self.rotoffset = 0
        self.projspeed = random.randint(3,6)
        self.ticktime = random.randint(3, 6)
        self.projlifetime = 700



    def update(self):
        self.ticks += 1

        if self.state == 'Spiral':
            self.rot += self.rotrate
            if self.ticks == self.ticktime:
                self.man.add_object(Projectile(man=self.man, pde=self.pde, position=[self.position[0], self.position[1]], rotation=self.rot, speed=[self.projspeed,self.projspeed], lifetime=self.projlifetime)) 
                self.ticks = 0
                if self.rotrate > 0:
                    if self.rot > 360:
                        self.rot = self.rot-360 + self.rotoffset
                elif self.rotrate < 0:
                    if self.rot < 360:
                        self.rot = self.rot+360 - self.rotoffset
        if self.state == "Random":
            if self.ticks == self.ticktime:
                rot = random.randint(-360, 360)
                scale = random.randint(8, 32)
                speed = random.randint(1, 8)
                self.man.add_object(Projectile(man=self.man, pde=self.pde, position=[self.position[0], self.position[1]], rotation=rot, scale=[scale, scale], speed=[speed, speed] , lifetime=self.projlifetime)) 
                self.ticks = 0
                if self.rotrate > 0:
                    if self.rot > 360:
                        self.rot = self.rot-360 + self.rotoffset
                elif self.rotrate < 0:
                    if self.rot < 360:
                        self.rot = self.rot+360 - self.rotoffset
        if self.state == "Single":
            if not self.done:
                rot = -90
                speed = 2
                self.man.add_object(Projectile(man=self.man, pde=self.pde, position=[self.position[0], self.position[1]], rotation=rot, scale=[16, 16], speed=[speed, speed] , lifetime=self.projlifetime)) 
                self.done = True


            


