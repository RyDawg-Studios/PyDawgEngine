import random
from data.engine.component.component import Component


class AIComponent(Component):
    def __init__(self, owner):
        self.states = {}
        self.state = 'default'
        self.owner = owner
        super().__init__(owner)

    def addstate(self, name, state):
        self.states[name] = state(man=self.owner.man, pde=self.owner.pde, owner=self)

    def update(self):
        if self.state != None:
            if self.state in self.states:
                self.states[self.state].update()
            else:
                return super().update()
        return super().update()

    def deconstruct(self):
        for state in self.states.values():
            state.deconstruct()
        return super().deconstruct()
