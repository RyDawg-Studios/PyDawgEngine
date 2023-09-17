import socket
import json

class Network():
    def __init__(self, owner, server="127.0.0.1", port=8080):
        self.owner = owner
        self.server = server
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = (self.server, self.port)


        self.connected = False

        self.send_event({'message_type': 'ping', 'message_data': {'data': 'Joining!', 'event_args': []}})



    def send_event(self, data):
        #print(f"Sending: {data}")
        dump = json.dumps(data)
        event = bytes(dump, "utf-8")
        self.connection.sendto(event, self.address)

    def update(self):
        data = self.connection.recv(1024)
        self.handle_data(data)

    def handle_data(self, data):
        self.handle_event(data)   
    
    def handle_event(self, data):
            if data:
                data = json.loads(data)

                #print(f"Receiving event: {data}")

                if data["message_type"] == 'ping':
                    print(data['message_data']['data'])
                elif data['message_type'] == 'event':
                    self.owner.pde.event_manager.handle_netevent_client(data)
                if not data:
                    self.disconnect()
