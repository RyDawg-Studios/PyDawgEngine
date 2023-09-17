import pygame

from data.engine.quadtree.Quadtree import QuadTree
from data.engine.quadtree.range import Rectangle


class ObjectManager:

    def __init__(self, pde) -> None:
        self.objects = []
        self.pde = pde
        self.clearing = False

        self.quadsize = 16

        self.quadtree = QuadTree(self.quadsize, Rectangle(pygame.Vector2(0, 0), pygame.Vector2(self.pde.config_manager.config["config"]["dimensions"])), pde=self.pde)

        self.pde.event_manager.net_events["spawn"] = self.deserializeNetObject

    def add_object(self, obj):
        if obj not in self.objects:
            self.objects.append(obj)
            obj.construct()

        return obj

    def remove_object(self, obj, outer=None):
        if obj in self.objects:
            self.objects.remove(obj)
            return True
        else:
            return False

    def update(self):
        self.quadtree = QuadTree(self.quadsize, Rectangle(pygame.Vector2(0, 0), pygame.Vector2(self.pde.config_manager.config["config"]["dimensions"])), pde=self.pde)
        for obj in list(self.objects):
            self.quadtree.insert(obj)
            
        for obj in list(self.objects):
            if not obj.paused:
                obj.update()
                for component in list(obj.components.values()):
                    component.update()


        if self.pde.config_manager.config["config"]["debugMode"]:
            self.quadtree.Show(screen=self.pde.display_manager.screen)

    def clear(self):
        for obj in self.objects:
            obj.deconstruct()
            
        self.objects = []

        self.quadtree = QuadTree(self.quadsize, Rectangle(pygame.Vector2(0, 0), pygame.Vector2(self.pde.config_manager.config["config"]["dimensions"])), pde=self.pde)

    def printobjects(self):
        print("----------------< Objects >----------------")
        i=0
        for o in self.objects:
            print(o)
            i += 1
        print(f"Count: {i}")
        
    def getPlayers(self):
        for obj in list(self.objects):
            for comp in obj.components:
                if comp == "PlayerController":
                    return obj

    def deserializeNetObject(self, data, owner=None):
        for spawned in self.objects:
            if spawned.hash == data[0]['hash']:
                for attr in data[0]['attributes']:
                    if data[0]['attributes'][attr][1] == False: #Should Deserialize?
                        setattr(spawned, attr[0], data[0]['attributes'][attr][0])
                    else:
                        setattr(spawned, attr[0], self.deserializeNetObject([data[0]['attributes'][attr][0]], owner=spawned))
                spawned.onNetworkUpdate_Event.call(data[0])
                return

        obj = self.pde.replication_tables[data[0]["package_id"]].object_table[data[0]['object_id']](man=self, pde=self.pde)
        obj.hash = data[0]['hash']
                
        for attr in data[0]['attributes']:
                if attr[0] == "owner":
                    if owner is not None:
                        setattr(obj, attr[0], owner)
                else:
                    if data[0]['attributes'][attr][1] == False: #Should Deserialize?
                        setattr(obj, attr[0], data[0]['attributes'][attr][0])
                    else:
                        setattr(obj, attr[0], self.deserializeNetObject([data[0]['attributes'][attr][0]], owner=obj))
            
        self.add_object(obj)
        obj.onNetworkSpawn_Event.call(data[0])
        return obj
    
    def updateNetObject(self, data):
        return



