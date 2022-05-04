from data.engine.networking.network import Network


class NetworkManager():
    def __init__(self, pde):
        self.active = False
        self.pde = pde
        
    def activate(self):
        self.network = Network(server="45.33.80.41")
        self.startpos = self.network.getpos()

    def update(self):
        return