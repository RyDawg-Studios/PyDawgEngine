import pygame
from data.engine.input.input_manager import InputManager
import sys

class EventManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.events = {}

    def activate(self):
        return
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.pde.network_manager.disconnect()
                pygame.quit()
                sys.exit()
            else:
                self.pde.input_manager.manage_inputs(event)
        return

    def handle_netevent(self, event):
        if event['message_type'] == 'event':
            if event['message_data']['event_name'] in self.events:
                self.events[event['message_data']['event_name']](event['message_data']['event_args'])
