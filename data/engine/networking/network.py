import sys, socket
from _thread import *
import pickle

class Network():
    def __init__(self, server="", port=5555):
        self.server = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (self.server, self.port)
        print(self.connect())

    def connect(self, name='RyDawgE'):
        try:
            self.client.connect(self.address)
            self.client.send(str.encode(name))
            val = self.client.recv(1024)
            return (val.decode('utf-8'))
        except Exception as e:
            print(e)

    def disconnect(self):
        self.client.close()

    def sendstring(self, data=""):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as error:
            print(error)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as error:
            print(error)
        
    def getpos(self):
        return self.pos

    def update(self):
        print(self.client.recv(4096).decode('utf-8'))