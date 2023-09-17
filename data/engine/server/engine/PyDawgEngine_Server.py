from time import sleep
import pygame
import _thread as threading

from data.engine.display.display_manager import DisplayManager
from data.engine.event.event_manager import EventManager
from data.engine.input.input_manager import InputManager
from data.engine.input.input_manager_server import InputManagerServer
from data.engine.level.level_manager import LevelManager
from data.engine.mouse.mouse_manager import MouseManager
from data.engine.player.player_manger import PlayerManager
from data.engine.cfg.config_manager import ConfigManager
from data.engine.sprite.sprite_manager import SpriteManager
from data.engine.debug.debugGame import DebugGame
from data.engine.server.server_manager import ServerManager
from data.topdownshooter.content.objects.server.game.TopDownShooter_Server import ShooterGameServer

class PyDawgEngineServer:

    def __init__(self) -> None:

        game = ShooterGameServer

        self.server_manager = ServerManager(pde=self)
        self.server_manager.active = True

        self.game = game(pde=self)
        
        self.event_manager = EventManager(pde=self)
        self.event_manager.active = True

        self.mouse_manager = MouseManager(pde=self)
        self.mouse_manager.active = True

        self.level_manager = LevelManager(pde=self)
        self.level_manager.active = True

        self.input_manager = InputManagerServer(pde=self)
        self.input_manager.active = True

        self.player_manager = PlayerManager(pde=self)
        self.player_manager.active = True

        self.config_manager = ConfigManager(pde=self)
        self.config_manager.active = True

        self.sprite_manager = SpriteManager(pde=self)
        self.sprite_manager.active = True
        
        self.display_manager = DisplayManager(pde=self)
        self.display_manager.active = True
        

        self.active = False

        self.clock = pygame.time.Clock()
        self.dt = 0
        self.targetFPS = 30
        self.fps = 0

        self.startengine()

    def startengine(self):
        for man in [self.server_manager, self.config_manager, self.input_manager, self.display_manager, self.event_manager, self.mouse_manager, self.level_manager, self.player_manager]:
            if man.active == False:
                raise Exception(str(man) + " Was not active on engine start. Did you properly initialize it?")
            else: man.active = True

        for man in [self.server_manager, self.config_manager, self.input_manager, self.display_manager, self.event_manager, self.mouse_manager, self.level_manager, self.player_manager]:
            if man.active == False:
                raise Exception(str(man) + " Was not active on engine start. Did you properly initialize it?")
            else: man.activate()

        self.active = True

        sleep(2)

        self.game.activate()

        while True:
            self.update()

    def update(self):
        self.dt = (self.clock.tick(60) / 1000) * self.targetFPS
        self.fps = round(self.clock.get_fps())

        self.server_manager.update()

        self.config_manager.update()
        self.event_manager.update()
        self.input_manager.update()
        self.mouse_manager.update()
        self.level_manager.update()
        self.player_manager.update()
        self.game.update()

        self.display_manager.update()

        pygame.display.set_caption(str(self.fps))

        
