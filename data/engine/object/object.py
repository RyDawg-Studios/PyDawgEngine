import struct

from data.engine.eventdispatcher.eventdispatcher import EventDispatcher


class Object:
    def __init__(self, man, pde):

        # -----< Actor Info >----- #

        self.man = man
        self.pde = pde
        self.components = {}
        self.scroll = True

        # -----< Replcation Info >----- #

        self.replicate = False
        self.replicable_attributes = {} # Var name, then replicable var type
        self.replication_id = 'empty_object' #Unique to a given object
        self.replication_package = 'pde' #Where the object is located
        self.hash = 000


        # -----< Object Info >----- #

        self.pausable = True
        self.paused = False
        self.decompose = False

        # -----< Quadtree Info >----- #

        self.quadtree = None

        # -----< Network Info >----- #
        
        self.onNetworkUpdate_Event = EventDispatcher()
        self.onNetworkSpawn_Event = EventDispatcher()


    def construct(self):
        self.onNetworkSpawn_Event.bind(self.onNetworkSpawn)
        self.onNetworkUpdate_Event.bind(self.onNetworkUpdate)
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

    def serialize(self, _id=''):
        rep_id = ''

        if _id == '':
            rep_id = self.replication_id
        else:
            rep_id = _id
            

        data = {'package_id': self.replication_package, 'object_id': rep_id, 'attributes': {}, 'hash': hash(self)}

        for attr, attr_type in self.replicable_attributes.items():

            if attr_type is not object:
                data["attributes"][attr] = [attr_type((getattr(self, str(attr)))), False]
            else:
                if getattr(self, str(attr)) is not None:
                    data["attributes"][attr] = [getattr(self, str(attr)).serialize(), True]
                else:
                    data["attributes"][attr] = [None, False]
        return data
    
    def onNetworkUpdate(self, data):
        return
    
    def onNetworkSpawn(self, data):
        return
    
    def server_replicate_object(self, server, client):
        server.emit_event({'message_type': 'event', 'message_data': {'event_name': 'spawn', 'event_args': [self.serialize()]}})

    def deconstruct(self, outer=None):
        self.pause()
        self.man.remove_object(self, outer)
        for component in self.components.values():
            component.deconstruct()
            component = None
        self.components = {}
        return
    

    


