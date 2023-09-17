from data.engine.server.server import Server
import threading


class ServerManager():
    def __init__(self, pde):
        self.pde = pde
        self.active = False
        self.server = None
        
    def server_thread(self):
        self.server = Server(pde=self.pde, server="localhost")

        while True:
            self.server.update()

    def activate(self):
        print("Server Manager Active")
        t = threading.Thread(target=self.server_thread)
        t.start()

    def update(self):
        return

    def disconnect(self):
        return