import gc
import pygame
from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.object.object import Object
from data.engine.widgets.button import Button
from data.engine.sprite.sprite_component import SpriteComponent



class Actor(Object):
    def __init__(self, man, pde, position=[0,0], scale=[32,32], checkForOverlap=True, checkForCollision=True, useCenterForPosition=False, lifetime=-1):
        super().__init__(man, pde)

        # -----< Actor Info >----- #

        self.name = str(self)
        self.components = {}
        self.quad = [0, 0]

        # -----< Transform Info >----- #

        self.position = position
        self.scale = scale
        self.rotation = 0
        self.canMove = True
        self.movement = pygame.Vector2([0, 0])
        self.useCenterForPosition = useCenterForPosition

        self.direction = [0,0]
        self.speed = 3
        self.velocity = 1

        # -----< Lifetime Info >----- #

        self.ticks = 0
        self.lifetime = lifetime

        # -----< Collision Info >----- #

        self.overlapInfo = {"Overlapping" : False, "Objects" : [], "Count": 0}
        self.collideInfo = {"Top": False, "Bottom": False, "Left": False, "Right": False, "Objects": []}
        self.collisionThreshHold = 2
        self.checkForOverlap = checkForOverlap
        self.checkForCollision = checkForCollision
        self.useSpriteRectForCollision = False
        self.moveable = False

        # -----< Debug Info >----- #

        if self.pde.config_manager.config["config"]["debugMode"]:
            self.components["DebugButton"] = Button(owner=self, bind=self.printDebugInfo)




    def construct(self):
        super().construct()
        self.position = pygame.Vector2(self.position)
        self.rect = pygame.rect.Rect(self.position[0], self.position[1], self.scale[0], self.scale[1])

        if self.pde.config_manager.config["config"]["debugMode"]:
            self.components["DebugSprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\mariohitbox.png', layer=4)

        if self.useCenterForPosition:
            self.rect.center = [self.position[0], self.position[1]]

        self.collideRect = self.rect
        return

    def update(self):
        super().update()
        self.ticks += 1    
        self.checklifetime() 
        self.move(self.movement)

    def getoverlaps(self):
        self.overlapInfo["Objects"] = []
        hits = []
        objects = []
        
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                objs = self.man.quadtree.getQuad(abs(self.quad[0]+x), abs(self.quad[1]+y))
                if objs is not None:
                    objects += objs.particles
            
        if self.moveable:
            for object in objects:
                if isinstance(object, Actor):
                    if object.checkForOverlap:
                        if self.collideRect.colliderect(object.collideRect) and object != self and not object.decompose:
                            if object not in self.overlapInfo["Objects"]:
                                self.overlap(object)
                            self.whileoverlap(object)
                            hits.append(object)
                if object not in objects and object in self.overlapInfo["Objects"]:
                    self.overlapInfo["Objects"].remove(object)
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

    def checklifetime(self):
        if self.ticks >= self.lifetime and self.lifetime != -1:
            self.expire()
            self.deconstruct()

    def expire(self): #Runs before deconstruct.
        return

    def scrollcameratocenterx(self):
        self.pde.display_manager.scroll[0] = (self.rect.centerx - self.pde.config_manager.config["config"]["dimensions"][0]/2)
    def scrollcameratocentery(self):
        self.pde.display_manager.scroll[1] = (self.rect.centery - self.pde.config_manager.config["config"]["dimensions"][1]/2)

    def printDebugInfo(self):
        print(f"Name: {str(self)}\n   Position: {self.position}\n   Scale: {self.scale}\n   Rotation: {self.rotation}\n   Movement: {self.movement}\n   Overlap Info: {self.overlapInfo}\n   Collide Info: {self.collideInfo}\n   Components: {self.components.keys()}")

    def checkXcollision(self, movement):
        if self.canMove:
            self.rect.x += round(self.movement.x * (self.pde.dt))
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
            self.rect.y += round(self.movement.y * (self.pde.dt))
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
    
    def getNeighboringObjects(self):
        objects = []
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                objs = self.man.quadtree.getQuad(abs(self.quad[0]+x), abs(self.quad[1]+y))
                if objs is not None:
                    objects += objs.particles
        return objects

    def deconstruct(self, outer=None):
        self.collideInfo["Objects"] = []
        return super().deconstruct(outer)