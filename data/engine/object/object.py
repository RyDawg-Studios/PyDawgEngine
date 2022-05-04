class Object:
    def __init__(self, man, pde):
        self.man = man
        self.pde = pde
        self.components = {}
        self.replicate = False


    def removecomponent(self, component):
        self.components.pop(component)

    def update(self):
        for component in self.components:
            self.components[component].update()

    def deconstruct(self):
        self.man.remove_object(self)
        for component in self.components.values():
            component.deconstruct()
        del self

    


