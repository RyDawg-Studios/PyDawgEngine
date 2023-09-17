import hashlib
import pickle


class Connection():
    def __init__(self, pde, serv, conn, addr):
        self.pde = pde
        self.serv = serv
        self.conn = conn
        self.addr = addr
        
    def update(self):
        return

    def disconnect(self):
        print(f"Lost Connection to {self.conn}")
        self.conn.close()