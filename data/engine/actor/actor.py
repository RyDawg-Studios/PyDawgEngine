import gc
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
        self.movement=pygame.Vector2([0, 0])
        self.components = {}

        if not hasattr(self, 'position'):
            self.position = [0, 0]
        self.position = pygame.Vector2(self.position)

        if not hasattr(self, 'scale'):
            self.scale = [32, 32]

        if not hasattr(self, 'rotation'):
            self.rotation = 0

        if not hasattr(self, 'name'):
            self.name = str(self)
        
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
            self.velocity = 1

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


        super().__init__(man, pde)

        if self.pde.config_manager.config["config"]["debugMode"]:
            self.components["DebugButton"] = Button(owner=self, bind=self.printDebugInfo)



    def update(self):
        super().update()
        self.ticks += 1    
        self.checklifetime() 
        self.getoverlaps()
        self.move(self.movement)

    def getoverlaps(self):
        hits = []
        if self.checkForOverlap:
            for object in list(self.pde.level_manager.level.objectManager.objects):
                if isinstance(object, Actor):
                    if self.checkForOverlap and object.checkForOverlap:
                        if self.collideRect.colliderect(object.collideRect) and object != self and not object.decompose:
                            if object not in self.overlapInfo["Objects"]:
                                self.overlap(object)
                            self.whileoverlap(object)
                            hits.append(object)
        self.overlapInfo["Objects"] = hits
        return hits

    def checkoverlaps(self):
        return

    def overlap(self, obj):
        return

    def whileoverlap(self, obj):
        return

    def collide(self, obj, side):
        return

    def move(self, movement):
        self.movement = pygame.math.Vector2(self.movement)
        self.collideInfo = {"Top": False, "Bottom": False, "Left": False, "Right": False, "Objects": []}
        
        self.checkXcollision(movement)
        self.checkYcollision(movement)

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
            self.expire()
            self.deconstruct()

    def expire(self): #Runs before deconstruct.
        return

    def scrollcameratocenterx(self):
        self.pde.display_manager.scroll[0] = (self.rect.centerx - 320)
    def scrollcameratocentery(self):
        self.pde.display_manager.scroll[1] = (self.rect.centery - 240)

    def printDebugInfo(self):
        print(f"Name: {str(self)}\n   Position: {self.position}\n   Scale: {self.scale}\n   Rotation: {self.rotation}\n   Movement: {self.movement}\n   Overlap Info: {self.overlapInfo}\n   Collide Info: {self.collideInfo}\n   Components: {self.components.keys()}")

    def checkXcollision(self, movement):
        if self.canMove:
            self.rect.x += self.movement.x
            hits = self.getoverlaps()  
            for object in hits:
                if isinstance(object, Actor) and object.checkForCollision and self.checkForCollision:
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

    def checkYcollision(self, movement):
        if self.canMove:
            self.rect.y += self.movement.y
            hits = self.getoverlaps()  
            for object in hits:
                if isinstance(object, Actor) and object.checkForCollision and self.checkForCollision:
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