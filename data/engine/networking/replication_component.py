from data.engine.component.component import Component
import struct

class ReplicationComponent(Component):
    def __init__(self, owner):
        self.pde = owner.pde

        super().__init__(owner)

    def update(self):
        return super().update()
    
    def addReplicativeVariable(self, name):
        return