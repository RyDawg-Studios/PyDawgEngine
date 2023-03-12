from data.engine.eventdispatcher.eventdispatcher import EventDispatcher
from data.engine.networking.network import Network
import threading


class NetworkManager():
    def __init__(self, pde):
        self.active = True
        self.pde = pde
        self.network = None

        self.onjoinednetwork = EventDispatcher()

    def activate(self):
        net = threading.Thread(target=self.network_thread, args=())
        net.start()

    def network_thread(self):
        if self.pde.config_manager.config["config"]["network"]["connectToServer"]:
            self.network = Network(owner=self, server="127.0.0.1")
            print("Network Active")

        while self.active:
            self.network.update()

    def disconnect(self):
        try:
            self.network.disconnect()
        except:
            pass
        self.active = False
        return

        
    def update(self):
        pass