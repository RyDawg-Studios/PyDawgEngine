import struct


class Object:
    def __init__(self, man, pde):
        self.man = man
        self.pde = pde
        self.components = {}
        self.scroll = True
        self.replicate = False
        self.pausable = True
        self.paused = False
        self.decompose = False


    def construct(self):
        return

    def pause(self):
        if self.pausable:
            self.paused = True

    def update(self):
        self.checkdeconstruct()
        return

    def checkdeconstruct(self):
        if self.decompose:
            self.deconstruct()
        else:
            return

    def queuedeconstruction(self):
        self.decompose = True

    def removecomponent(self, component):
        self.components.pop(component)

    def hascomponent(self, component):
        return component in self.components.keys()
            
    def getcomponent(self, component):
        if component in self.components:
            return self.components[component]

    def getcomponents(self):
        return self.components

    def getcomponentsoftype(self, component):
        components = []
        for c in self.components.values():
            if isinstance(c, component):
                components.append(c)
        return components

    def deconstruct(self, outer=None):
        self.pause()
        self.man.remove_object(self, outer)
        for component in self.components.values():
            component.deconstruct()
            component = None
        self.components = {}
 
    def serialize(self, data=None):
        return struct.pack(data)
        
    def deserialize(self):
        return

    

    


