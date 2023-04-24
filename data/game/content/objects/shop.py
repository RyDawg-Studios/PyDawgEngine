from data.engine.object.object import Object



class Upgrade():
    def __init__(self, shop) -> None:
        self.shop = shop

    def onpurchase(self):
        pass


class ShopManager(Object):
    def __init__(self, man, pde, components={}) -> None:
        super().__init__(man, pde, components)