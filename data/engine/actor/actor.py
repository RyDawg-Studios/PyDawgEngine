from shutil import move
import pygame
from data.engine.object.object import Object
from data.engine.widgets.button import Button


class Actor(Object):
    def __init__(self, man, pde, position=[0,0], scale=[32, 32], rotation=0, maxSpeed=4, lifetime=-1, components={}, useCenterForPosition=False, checkForCollision = True, checkForOverlap = True):
        super().__init__(man, pde)


        #---------< General Info >---------#

        self.name = str(self)
        self.lifetime = lifetime
        self.ticks = 0
        self.components = components

        #---------< Transform Info >---------#

        self.position = pygame.math.Vector2(position)
        self.scale = scale
        self.rotation = rotation
        self.useCenterForPosition = useCenterForPosition
        self.rect = pygame.rect.Rect(self.position[0], self.position[1], self.scale[0], self.scale[1])

        #---------< Physics Info >---------#
        
        self.velocity = 5
        self.canMove = True
        self.movement=pygame.math.Vector2([1, 1]).normalize()
        self.maxSpeed = maxSpeed
        self.speed = [0, 0]
        self.direction = 1

        #---------< Collision Info >---------#

        self.overlapInfo = {"Overlapping" : False, "Objects" : [], "Count": 0}
        self.collideInfo = {"Top": False, "Bottom": False, "Left": False, "Right": False, "Objects": []}
        self.checkForOverlap = checkForOverlap
        self.checkForCollision = checkForCollision

        #---------< Debug Info >---------#

        if eval(self.pde.config_manager.config["config"]["debugMode"]):
            self.components["DebugButton"] = Button(owner=self, bind=self.printDebugInfo)




    def update(self):
        self.ticks += 1    
        self.checklifetime() 
        self.getoverlaps()
        self.move(self.movement)
        super().update()

    def getoverlaps(self):
        hits = []
        if self.checkForOverlap:
            for level in self.pde.level_manager.levels.values():
                for object in list(level.objectManager.objects.values()):
                    if hasattr(object, 'checkForOverlap'):
                        if self.checkForOverlap == True:
                            if self.rect.colliderect(object.rect) and object != self:
                                hits.append(object)
                                object.whileoverlap(self)
                                self.whileoverlap(object)
                                object.overlap(self)
                                self.overlap(object)
        self.overlapInfo["Objects"] = hits
        return hits

    def checkoverlaps(self):
        pass

    def overlap(self, obj):
        pass

    def whileoverlap(self, obj):
        pass

    def collide(self, obj, side):
        pass

    def move(self, movement):
        self.collideInfo = {"Top": False, "Bottom": False, "Left": False, "Right": False, "Objects": []}
        if self.canMove:
            self.speed = movement
            self.position.x += movement.x * self.velocity
            self.rect.x = self.position.x
            print(self.position.x)
            hits = self.getoverlaps()  
            for object in hits:
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if object not in self.collideInfo["Objects"]:
                        self.collideInfo["Objects"].append(object)
                    if movement[0] > 0:
                        self.rect.right = object.rect.left
                        self.collideInfo["Right"] = True
                        object.collide(self, "Left")
                    elif movement[0] < 0:
                        self.rect.left = object.rect.right
                        self.collideInfo["Left"] = True
                        object.collide(self, "Right")
            self.rect.y += movement[1]
            hits = self.getoverlaps()  
            for object in hits:
                if hasattr(object, 'checkForCollision') and object.checkForCollision and self.checkForCollision:
                    if object not in self.collideInfo["Objects"]:
                        self.collideInfo["Objects"].append(object)
                    if movement[1] > 0:
                        self.rect.bottom = object.rect.top
                        self.collideInfo["Bottom"] = True
                        object.collide(self, "Top")
                    elif movement[1] < 0:
                        self.rect.top = object.rect.bottom
                        self.collideInfo["Top"] = True
                        object.collide(self, "Bottom")





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

    def scrollcameratocenterx(self):
        self.pde.display_manager.scroll[0] = (self.rect.centerx - 320)
    def scrollcameratocentery(self):
        self.pde.display_manager.scroll[1] = (self.rect.centery - 240)

    def printDebugInfo(self):
        print(f"Name: {str(self)}\n   Position: {self.position}\n   Scale: {self.scale}\n   Rotation: {self.rotation}\n   Movement: {self.movement}\n   Overlap Info: {self.overlapInfo}\n   Collide Info: {self.collideInfo}\n   Components: {self.components.keys()}")