import sys, socket
from _thread import *
import pickle

class Network():
    def __init__(self, server="", port=5555):
        self.server = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (self.server, self.port)
        self.pos = self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            print("Failed to connect")

    def send(self, data=""):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as error:
            print(error)
        
    def getpos(self):
        return self.pos