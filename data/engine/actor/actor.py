from shutil import move
import pygame
from data.engine.object.object import Object
from data.engine.widgets.button import Button


class Actor(Object):
    def __init__(self, man, pde):
        self.canMove = True
        self.overlapInfo = {"Overlapping" : False, "Objects" : [], "Count": 0}
        self.collideInfo = {"Top": False, "Bottom": False, "Left": False, "Right": False, "Objects": []}
        self.collisionThreshHold = 2
        self.ticks = 0
        self.movement=[0, 0]

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

        if eval(self.pde.config_manager.config["config"]["debugMode"]):
            self.components["DebugButton"] = Button(owner=self, bind=self.printDebugInfo)



    def update(self):
        self.getoverlaps()
        self.ticks += 1    
        self.checklifetime() 
        self.move(self.movement)

        super().update()



    def getoverlaps(self):
        hits = []
        if self.checkForOverlap:
            for level in self.pde.level_manager.levels.values():
                for object in list(level.objectManager.objects.values()):
                    if hasattr(object, 'checkForOverlap'):
                        if self.checkForOverlap == True:
                            if self.collideRect.colliderect(object.collideRect) and object != self:
                                hits.append(object)
                                object.whileoverlap(self)
                                self.whileoverlap(object)
                                if object not in self.overlapInfo["Objects"]:
                                    self.overlapInfo["Objects"].append(object)
                                    object.overlap(self)
                                    self.overlap(object)
                            else:
                                if object in self.overlapInfo["Objects"]:
                                    self.overlapInfo["Objects"].remove(object)
        return hits

    def checkoverlaps(self):
        pass

    def overlap(self, obj):
        pass

    def whileoverlap(self, obj):
        pass

    def move(self, movement):
        if self.canMove:
            self.speed = movement
            if movement[0] > 0 and movement[0] > 6:
                movement[0] = 6

            if movement[0] < 0 and movement[0] < -6:
                movement[0] = -6
            self.rect.x += movement[0]
            for object in self.getoverlaps():
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if movement[0] > 0:
                        self.rect.right = object.rect.left
                        self.collideInfo["Right"] = True
                    else:
                        self.collideInfo["Right"] = False      
                    if movement[0] < 0:
                        self.rect.left = object.rect.right
                        self.collideInfo["Left"] = True
                    else:
                        self.collideInfo["Left"] = False  

                    if object not in self.collideInfo["Objects"]:
                        self.collideInfo["Objects"].append(object)
                    
            self.rect.y += movement[1]
            for object in self.getoverlaps():
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if movement[1] > 0:
                        self.rect.bottom = object.rect.top
                        self.collideInfo["Bottom"] = True
                    else:
                        self.collideInfo["Bottom"] = False   
                    if movement[1] < 0:
                        self.rect.top = object.rect.bottom
                        self.collideInfo["Top"] = True
                    else:
                        self.collideInfo["Top"] = False  
            
                    if object not in self.collideInfo["Objects"]:
                        self.collideInfo["Objects"].append(object) 
                else:
                    self.collideInfo["Top"], self.collideInfo["Bottom"] = False, False


        self.position[0] = self.rect.center[0]
        self.position[1] = self.rect.center[1]
        self.scale[0] = self.rect.size[0]
        self.scale[1] = self.rect.size[1]

        if self.movement[0] < 0:
            self.direction = -1

        elif self.movement[0] > 0:
            self.direction = 1


    def checklifetime(self):
        if self.ticks >= self.lifetime and self.lifetime != -1:
            self.deconstruct()

    def scrollcameratocenter(self):
        self.pde.display_manager.scroll[0] = (self.rect.centerx - 320)

    def printDebugInfo(self):
        print(f"Name: {str(self)}\n   Position: {self.position}\n   Scale: {self.scale}\n   Rotation: {self.rotation}\n   Movement: {self.movement}\n   Overlap Info: {self.overlapInfo}\n   Collide Info: {self.collideInfo}\n   Components: {self.components.keys()}")