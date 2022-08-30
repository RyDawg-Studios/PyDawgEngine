from data.engine.level.level import Level
from data.engine.projectile.projectile import Projectile
from data.game.content.objects.projectile_spawner import ProjectileSpawner
from data.game.content.player.DawgTalePlayer import DawgTalePlayer
import random

class GameOverLevel(Level):
    def __init__(self, man, pde, pos) -> None:
        self.ticks = 0
        self.rot=0
        self.pos = pos
        super().__init__(man, pde)
        #self.changebackground(r'assets\debug\sprites\xp.png')

        self.objectManager.add_object(DawgTalePlayer(man=self.objectManager, pde=pde, position=pos))


    def update(self):
        pass

        
        return super().update()
        