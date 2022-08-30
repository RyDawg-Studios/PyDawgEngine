from data.engine.component.component import Component

class ReplicationComponent(Component):
    def __init__(self, owner):
        self.pde = owner.pde

        super().__init__(owner)

    def update(self):
        self.pde.network_manager.network.send({self.owner.man.objects[str(self.owner)]: self.owner})
        return super().update()
    
    def addReplicativeVariable(self, name):
        return