class Component:
    def __init__(self, owner, **kwargs) -> None:
        self.kwargs = kwargs
        self.owner = owner

    def update(self):
        pass

    def deconstruct(self):
        del self
