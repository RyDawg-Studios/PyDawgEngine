class Component:
    def __init__(self, owner):
        self.owner = owner

    def update(self):
        return

    def deconstruct(self):
        self.owner = None
        return

    def checkForOwner(self):
        return