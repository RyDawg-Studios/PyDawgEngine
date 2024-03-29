import pygame
import _thread as threading

from data.engine.display.display_manager import DisplayManager
from data.engine.event.event_manager import EventManager
from data.engine.input.input_manager import InputManager
from data.engine.level.level_manager import LevelManager
from data.engine.mouse.mouse_manager import MouseManager
from data.engine.networking.network import Network
from data.engine.networking.network_manager import NetworkManager
from data.engine.player.player_manger import PlayerManager
from data.engine.cfg.config_manager import ConfigManager
from data.engine.sprite.sprite_manager import SpriteManager
from data.engine.debug.debugGame import DebugGame
from data.engine.networking.network import Network
from data.engine.networking import pde_network_table
from data.game.content.sci_game import Leukosite


class PyDawgEngine:

    def __init__(self) -> None:

        game = Leukosite

        self.game = game(pde=self)
        
        self.config_manager = ConfigManager(pde=self)
        self.config_manager.active = True

        self.event_manager = EventManager(pde=self)
        self.event_manager.active = True

        self.mouse_manager = MouseManager(pde=self)
        self.mouse_manager.active = True

        self.level_manager = LevelManager(pde=self)
        self.level_manager.active = True

        self.input_manager = InputManager(pde=self)
        self.input_manager.active = True

        self.player_manager = PlayerManager(pde=self)
        self.player_manager.active = True


        self.sprite_manager = SpriteManager(pde=self)
        self.sprite_manager.active = True

        self.display_manager = DisplayManager(pde=self)
        self.display_manager.active = True


        self.network_manager = NetworkManager(pde=self)
        self.network_manager.active = True

        self.active = False

        self.clock = pygame.time.Clock()
        self.dt = 0
        self.targetFPS = 60
        self.fps = 0

        self.replication_tables = {"pde": pde_network_table}

        self.startengine()

    def startengine(self):
        for man in [self.network_manager, self.config_manager, self.input_manager, self.display_manager, self.event_manager, self.mouse_manager, self.level_manager, self.player_manager]:
            if man.active == False:
                raise Exception(str(man) + " Was not active on engine start. Did you properly initialize it?")
            else: man.active == True

        for man in [self.config_manager, self.input_manager, self.display_manager, self.event_manager, self.mouse_manager, self.level_manager, self.player_manager]:
            if man.active == False:
                raise Exception(str(man) + " Was not active on engine start. Did you properly initialize it?")
            else: man.activate()

        self.active = True

        self.game.activate()

        while True:
            self.update()

    def update(self):
        self.dt = (self.clock.tick(60) / 1000) * self.targetFPS
        self.fps = round(self.clock.get_fps())

        self.network_manager.update()

        self.config_manager.update()
        self.event_manager.update()
        self.input_manager.update()
        self.mouse_manager.update()
        self.level_manager.update()
        self.player_manager.update()
        self.game.update()

        self.display_manager.update()

        pygame.display.set_caption(str(self.fps))

    def quit(self):
        return


        
