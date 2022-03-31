import random
from data.engine.actor.actor import Actor
from data.game.content.objects.bloodproj import Blood
from data.engine.projectile.projectile import Projectile
from data.game.content.objects.wall_projectile import WallProjectile
from data.engine.fl import world_fl



class BloodSpawner(Actor):
    def __init__(self, man, pde, position):
        self.position = position
        super().__init__(man, pde)

        self.checkForOverlap = False
        self.checkForCollision = False

        self.rot=0

        self.state = 'Random'
        self.done = False

        self.rotrate = 0
        self.rotoffset = 0
        self.projspeed = random.randint(3,6)
        self.ticktime = 16
        self.projlifetime = 700



    def update(self):
        self.ticks += 1
        if self.state == "Random":
            if self.ticks == self.ticktime:
                scale = random.randint(8, 12)
                speed = random.randint(1, 8)
                self.man.add_object(Blood(man=self.man, pde=self.pde, position=[self.position[0], random.randint(0, 480)], rotation=180, scale=[scale, scale], speed=[speed, speed] , lifetime=self.projlifetime)) 
                self.ticks = 0

        if self.state == "Single":
            if not self.done:
                rot = -90
                speed = 2
                self.man.add_object(Projectile(man=self.man, pde=self.pde, position=[self.position[0], self.position[1]], rotation=rot, scale=[16, 16], speed=[speed, speed] , lifetime=self.projlifetime)) 
                self.done = True
        
        if self.state == "Target":
            if not self.done:
                if self.ticks == self.ticktime:
                    scale = random.randint(8, 12)
                    speed = random.randint(1, 8)
                    self.man.add_object(Blood(man=self.man, pde=self.pde, position=[self.position[0], self.position[1]], rotation=world_fl.objectlookattarget(self, self.player), scale=[scale, scale], speed=[speed, speed] , lifetime=self.projlifetime)) 

                    self.ticks = 0


            


