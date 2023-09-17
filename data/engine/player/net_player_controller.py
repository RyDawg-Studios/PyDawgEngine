
from data.engine.player.player_controller import PlayerController

class NetPlayerController(PlayerController):
    def __init__(self, owner):
        super().__init__(owner)

        self.inpman.on_input_event.bind(self.on_keydown)
        self.inpman.on_output_event.bind(self.on_keyup)

    def on_keydown(self, data):
        self.owner.pde.network_manager.network.send_event({'message_type': 'event', 'message_data': {'event_name': 'input', 'event_args': [data, True]}})
        return

    def on_keyup(self, data):
        self.owner.pde.network_manager.network.send_event({'message_type': 'event', 'message_data': {'event_name': 'input', 'event_args': [data, False]}})
        return
    
    def deconstruct(self):
        super().deconstruct()
        return
    
