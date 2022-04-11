class Component:
    def __init__(self, owner):
        self.owner = owner

    def update(self):
        pass

    def deconstruct(self):
        del self
