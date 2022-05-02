import random
from data.engine.ai.ai_component import AIComponent
from data.engine.debug.debugAI import debugAI
from data.engine.debug.debugController import DebugController
from data.engine.fl.world_fl import objectlookatposition, objectlookattarget
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.ai.ai_wander import WanderAI
from data.topdownshooter.content.objects.shooterentity.shooterentity import ShooterEntity
from data.topdownshooter.content.objects.weapon.weapons.weapons import SMG, AutomaticRifle, BurstRifle, Shotgun, SniperRifle


class ShooterEnemy(ShooterEntity):
    def __init__(self, man, pde, position=None, scale=[32, 32], player=None, velocity=4):
        super().__init__(man, pde, position, scale)
        self.velocity = velocity
        self.player = pde.game.player
        self.defaultspeed = [8, 8]
        self.speed = self.defaultspeed
        self.rotation = 0
        self.hp = 100
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\assets\sprites\badme.png', layer=2)
        ai = self.components["AI"] = AIComponent(owner=self)
        ai.addstate(name="default", state=WanderAI)
        w = random.choice([SMG, AutomaticRifle, Shotgun, SniperRifle])
        self.weapon = man.add_object(obj=w(man=man, pde=pde, owner=self))
    def update(self):
        if self.weapon != None and self.player != None and self.player.dead == False:
            self.weapon.shoot(angle=objectlookattarget(self, self.player))
            self.weapon.rotation = objectlookattarget(self, self.player)

        return super().update()
