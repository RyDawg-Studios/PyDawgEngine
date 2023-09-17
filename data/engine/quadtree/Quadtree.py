import pygame
from pygame.math import Vector2
from data.engine.quadtree.range import *

class QuadTree:
    def __init__(self, capacity, boundary, parent = None, color = (140, 255, 160), thickness=1, pde=None):
        self.capacity = capacity
        self.parent = parent
        self.boundary = boundary
        self.particles = []
        self.color = color
        self.lineThickness = thickness
        self.bounds = []
        self.pde = pde
        self.rows = 6
        self.columns = 8

        self.subdivide()

    def subdivide(self):
        parent = self.boundary

        for y in list(range(self.rows+1)) + [-1]:
            self.bounds.append([])
            for x in list(range(self.columns+1))  + [-1]:
                self.bounds[y].append(Rectangle(position=Vector2(x*int(self.pde.config_manager.config["config"]["dimensions"][0]/self.columns), y*int(self.pde.config_manager.config["config"]["dimensions"][1]/self.rows)), scale=[int(self.pde.config_manager.config["config"]["dimensions"][0]/self.columns), int(self.pde.config_manager.config["config"]["dimensions"][1]/self.rows)]))
            
    def insert(self, particle):
        for yinx, y in enumerate(self.bounds):
            for xinx, x in enumerate(y):
                if x.containsParticle(particle):
                    particle.quad = [xinx, yinx]
                    x.particles.append(particle)

    def getQuad(self, x=0, y=0):
        if self.isQuadLegit(x, y):
            return self.bounds[y][x]
        
    
    def isQuadLegit(self, x=0, y=0):
        isY = False
        isX = False

        if y in range(len(self.bounds)-1):
            isY = True
        else:
            return False
        
        if x in range(len(self.bounds[y])-1):
            isX = True

        if isX and isY:
            return True
        else:
            return False

       

    def queryRange(self, _range):
        particlesInRange = []

        if _range.name == "circle":
            if _range.intersects(self.boundary)==False:
                return particlesInRange
        else:
            if _range.intersects(self.boundary)==True:
                return particlesInRange

        for particle in self.particles:
            if _range.containsParticle(particle):
                particlesInRange.append(particle)
        if self.northWest != None:
            particlesInRange += self.northWest.queryRange(_range)
            particlesInRange += self.northEast.queryRange(_range)
            particlesInRange += self.southWest.queryRange(_range)
            particlesInRange += self.southEast.queryRange(_range)
        return particlesInRange
        

        # if self.boundary.intersects(_range):
        #     return particlesInRange
        # else:
        #     for particle in self.particles:
        #         if _range.containsParticle(particle):
        #             particlesInRange.append(particle)
        #
        #     if self.northWest != None:
        #         particlesInRange += self.northWest.queryRange(_range)
        #         particlesInRange += self.northEast.queryRange(_range)
        #         particlesInRange += self.southWest.queryRange(_range)
        #         particlesInRange += self.southEast.queryRange(_range)
        #
        #     return particlesInRange

    def Show(self, screen):
        self.boundary.color = self.color
        self.boundary.lineThickness = self.lineThickness
        self.boundary.Draw(screen)
        for y in self.bounds:
            for bound in y:
                bound.Draw(screen)

