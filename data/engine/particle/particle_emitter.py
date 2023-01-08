import random
from data.engine.component.component import Component
import pygame




class ParticleEmitter(Component):
    def __init__(self, owner):
        super().__init__(owner)

        self.particles = []
        self.templates = {}

        self.ticks = 0
        self.rate = 10
        self.active = False

    def update(self):
        super().update()

        self.ticks += 1
        if self.ticks >= self.rate and self.active:
            self.ticks = 0

            self.particles.append(random.choice(list(self.templates.values())))

        for p in self.particles:
            p["ticks"] += 1
            
            if p["ticks"] >= p["lifetime"]:
                self.particles.remove(p)

            p["position"][0] += p["velocity"][0]
            p["position"][1] += p["velocity"][1]

            p["velocity"][1] += p["gravity"]

            sprite = pygame.image.load(p["sprite"])
            sprite = pygame.transform.scale(sprite, p["scale"])

            self.owner.pde.display_manager.screen.blit(source=sprite, dest=p["position"])

        return

    def createtemplate(self, name, sprite='', position=[0,0], scale=[8, 8], rotation=0, velocity=[0,0], lifetime=0, gravity=0):
        pos = position
        pos[0] = pos[0] - (scale[0] / 2)
        pos[1] = pos[1] - (scale[1] / 2)
        particle = {"sprite": sprite, "position": pos, "scale": scale, "rotation": rotation, "velocity": velocity, "lifetime": lifetime, "gravity": gravity, "ticks": 0}
        self.templates[name] = particle
        return particle


    def createparticle(self, sprite='', position=[0,0], scale=[8, 8], rotation=0, velocity=[0,0], lifetime=0, gravity=0):
        pos = position
        pos[0] = pos[0] - (scale[0] / 2)
        pos[1] = pos[1] - (scale[1] / 2)
        particle = {"sprite": sprite, "position": pos, "scale": scale, "rotation": rotation, "velocity": velocity, "lifetime": lifetime, "gravity": gravity, "ticks": 0}
        self.particles.append(particle)
        return particle