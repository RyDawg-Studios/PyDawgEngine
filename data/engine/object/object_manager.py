import pygame


class ObjectManager:

    def __init__(self, pde) -> None:
        self.objects = []
        self.pde = pde
        self.clearing = False

    def add_object(self, obj):
        if obj not in self.objects:
            self.objects.append(obj)
            obj.construct()
        return obj

    def remove_object(self, obj, outer=None):
        if obj in self.objects:
            self.objects.remove(obj)
        else:
            print(f"ObjectManager.remove_object failed to remove {obj.__class__.__name__} because it was not found. Outer was {outer}")


    def update(self):
        for obj in list(self.objects):
            if not obj.paused:
                obj.update()
                for component in list(obj.components.values()):
                    component.update()
            #if hasattr(obj, 'owner'):
                #print(f'Object {obj.__class__.__name__} Owner {obj.owner.__class__.__name__}')

    def clear(self):
        for obj in self.objects:
            obj.queuedeconstruction()
            
        self.objects = []

    def printobjects(self):
        print("----------------< Objects >----------------")
        i=0
        for o in self.objects:
            print(o)
            i += 1
        print(f"Count: {i}")
        
    def getPlayers(self):
        for obj in list(self.objects.values()):
            for comp in obj.components:
                if comp == "PlayerController":
                    return obj



