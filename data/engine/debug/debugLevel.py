from data.engine.level.level import Level
from data.engine.debug.debugObject import TestActor, TestObject, TestPlayer
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.player.player_controller import PlayerController
from data.game.content.objects.projectile import Projectile
from data.game.content.player.DawgTalePlayer import DawgTalePlayer

class TestLevel(Level):
    def __init__(self, man, pde) -> None:
        self.ticks = 0
        super().__init__(man, pde)
        self.changebackground(r'assets\debug\sprites\xp.png')

        self.objectManager.add_object(DawgTalePlayer(man=self.objectManager, pde=pde, position=[600, 400]))
        self.objectManager.add_object(Projectile(man=self.objectManager, pde=self.pde, position=[300, 300], rotation=45))
