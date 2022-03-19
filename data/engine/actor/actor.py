import imp


import math
import pygame
from data.engine.object.object import Object


class Actor(Object):
    def __init__(self, man, pde):
        self.canMove = True
        self.overlapInfo = {"Overlapping" : False, "Objects" : []}
        self.collideInfo = {"Type": "None"}
        self.collisionThreshHold = 2
        self.ticks = 0

        if not hasattr(self, 'position'):
            self.position = [0, 0]

        if not hasattr(self, 'scale'):
            self.scale = [30, 30]

        if not hasattr(self, 'rotation'):
            self.rotation = 0

        if not hasattr(self, 'name'):
            self.name = str(self)

        if not hasattr(self, 'components'):
            self.components = {}
        
        if not hasattr(self, 'maxSpeed'):
            self.maxSpeed = [2,2]

        if not hasattr(self, 'checkForOverlap'):
            self.checkForOverlap = True

        if not hasattr(self, 'checkForCollision'):
            self.checkForCollision = True

        if not hasattr(self, 'lifetime'):
            self.lifetime = -1

        if not hasattr(self, 'speed'):
            self.speed = [0,0]

        if not hasattr(self, 'direction'):
            self.direction = [0,0]

        if not hasattr(self, 'velocity'):
            pass
        
        if not hasattr(self, 'spriteScale'):
            self.spriteScale = self.scale

        if not hasattr(self, 'spriteRotation'):
            self.spriteRotation = self.rotation

        if not hasattr(self, 'useSriteRectForCollision'):
            self.useSpriteRectForCollision = False

        if not hasattr(self, 'useCenterForPosition'):
            self.useCenterForPosition = False

        if not hasattr(self, 'rect'):
            self.rect = pygame.rect.Rect(self.position[0], self.position[1], self.scale[0], self.scale[1])
            if self.useCenterForPosition:
                self.rect.center = [self.position[0], self.position[1]]

        if not hasattr(self, 'collideRect'):
            self.collideRect = self.rect


        super().__init__(man, pde, self.components)



    def update(self):
        self.ticks += 1    
        self.checkoverlap()
        self.checklifetime()
        self.move()   
        super().update()


    def checkoverlap(self):

        for level in self.pde.level_manager.levels.values():
            for object in list(level.objectManager.objects.values()):
                if hasattr(object, 'checkForOverlap'):
                    if self.checkForOverlap == True:
                        if self.collideRect.colliderect(object.collideRect) and object != self:
                            self.whileoverlap(object)
                            if object not in self.overlapInfo["Objects"]:
                                self.overlapInfo["Objects"].append(object)
                                self.overlap(object)

                    if object.checkForCollision and self.checkForCollision and hasattr(object, 'checkForCollision'):
                        if self.collideRect.colliderect(object.collideRect) and object != self:
                            if abs(object.rect.bottom - self.rect.top) < self.collisionThreshHold:
                                self.rect.top = object.rect.bottom
                            if abs(object.rect.top - self.rect.bottom) < self.collisionThreshHold:
                                self.rect.bottom = object.rect.top
                            if abs(object.rect.left - self.rect.right) < self.collisionThreshHold:
                                self.rect.right = object.rect.left
                            if abs(object.rect.right - self.rect.left) < self.collisionThreshHold:
                                self.rect.left = object.rect.right

                    if not self.rect.colliderect(object.rect) and object in self.overlapInfo['Objects']:
                        self.overlapInfo["Objects"].remove(object)

            for object in self.overlapInfo["Objects"]:
                if object not in level.objectManager.objects.values():
                    self.overlapInfo["Objects"].remove(object)
                    pass

        if len(self.overlapInfo["Objects"]) > 0:
            self.overlapInfo["Overlapping"] = True
        else:
            self.overlapInfo["Overlapping"] = False


    def overlap(self, obj):
        pass

    def whileoverlap(self, obj):
        pass


    def move(self):
        if self.canMove:

            self.rect.x += self.speed[0]
            self.rect.y += self.speed[1]

        self.position[0] = self.rect.x
        self.position[1] = self.rect.y

        if self.useCenterForPosition:
            self.position[0] = self.rect.center[0]
            self.position[1] = self.rect.center[1]
        



        self.scale[0] = self.rect.size[0]
        self.scale[1] = self.rect.size[1]


    def checklifetime(self):
        if self.ticks >= self.lifetime and self.lifetime != -1:
            self.deconstruct()