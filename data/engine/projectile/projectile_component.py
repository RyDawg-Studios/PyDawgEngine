import pygame
from data.engine.component.component import Component
import math

class ProjectileComponent(Component):
    def __init__(self, owner, rotation=0, velocity=[0,0], speed=0, **kwargs) -> None:
        self.rotation = rotation
        self.velocity = velocity
        self.speed = speed
        self.owner = owner
        self.position = self.owner.position
        super().__init__(owner, **kwargs)


        
    def update(self):
        self.travel()
        return super().update()

    def travel(self):
        vel = self.updatevelocity()
        self.owner.rect.centerx += vel[0]
        self.owner.rect.centery += vel[1] 


    def updatevelocity(self):
        self.rotation = self.owner.rotation
        self.velocity[0] = math.cos(math.radians(self.rotation)) * self.speed
        self.velocity[1] = math.sin(math.radians(self.rotation)) * self.speed *-1

        return self.velocity


