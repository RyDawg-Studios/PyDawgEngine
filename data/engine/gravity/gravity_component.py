from data.engine.component.component import Component

class GravityComponent(Component):
    def __init__(self, owner, **kwargs) -> None:
        super().__init__(owner, **kwargs)

    def update(self):
        self.owner.position[1] -= 1
        return super().update()