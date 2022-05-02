import random
from data.engine.fl.world_fl import objectlookatposition
from data.engine.sprite.sprite_component import SpriteComponent
from data.topdownshooter.content.objects.weapon.weapons.weapon import Weapon
from data.topdownshooter.content.objects.weapon.bullets.bullets import DefaultBullet, DevBullet, Grenade, HelixBullet, HomingActor, HomingBullet, SniperBullet, ZigZagBullet, LaserBeam


class AutomaticRifle(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [40, 14]
        super().__init__(man, pde, owner)
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\cbmk2.png', layer=3)

        #----------< Weapon Info >----------#

        self.firerate = 12
        self.bullet = DefaultBullet

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

class BurstRifle(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [40, 14]
        super().__init__(man, pde, owner)
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\cbmk2.png', layer=3)
        
        #----------< Weapon Info >----------#
        
        self.firerate = 2
        self.shotspread = 3
        self.bursts = 5
        self.burst = 0
        self.burstrate = 50
        self.burstbuffer = 0
        

        self.bullet = DefaultBullet

    def update(self):
        self.burstbuffer += 1
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

    def shoot(self, angle):
        if self.burstbuffer >= self.burstrate:
            if self.shottick >= self.firerate:
                self.shottick = 0
                for shot in self.shotangles:
                    b = self.man.add_object(obj=self.bullet(man=self.man, pde=self.pde, owner=self, position=[self.owner.position[0] + 10, self.owner.position[1] + 10], rotation=angle + shot + random.randint(-self.shotspread, self.shotspread)))
                    b.onshot()
                self.burst += 1
            if self.burst >= self.bursts:
                self.burstbuffer = 0
                self.burst = 0

class Shotgun(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [30, 12]
        super().__init__(man, pde, owner)
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\shotgun\boomstick.png', layer=3)

        #----------< Weapon Info >----------#

        self.firerate = 60
        self.bullet = DefaultBullet
        self.shotspread = 0
        self.shotangles = [-10, -5, 0, 5, 10]

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

    def shoot(self, angle):
        return super().shoot(angle)


class SniperRifle(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [40, 14]
        super().__init__(man, pde, owner)
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\sniper\sniper.png', layer=3)

        #----------< Weapon Info >----------#

        self.firerate = 75
        self.bullet = SniperBullet

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

class SMG(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [24, 18]
        super().__init__(man, pde, owner)
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\smg\smg.png', layer=3)

        #----------< Weapon Info >----------#

        self.firerate = 5
        self.bullet = DefaultBullet

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()


class DevGun(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [56, 22]
        super().__init__(man, pde, owner)
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\devgun\rydawgun.png', layer=3)

        #----------< Weapon Info >----------#

        self.shotspread = 0
        self.shotangles = [0]
        self.firerate = 2
        self.bullet = DevBullet

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

class LaserRifle(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [40, 14]
        super().__init__(man, pde, owner)
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\debug\debugweapon\cbmk2.png', layer=3)

        #----------< Weapon Info >----------#

        self.firerate = 12
        self.bullet = LaserBeam

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        bs = []
        if self.shottime > 20 and not self.shooting:
            for shot in self.shotangles:
                b = self.man.add_object(obj=self.bullet(man=self.man, pde=self.pde, owner=self, scale = [self.shottime, 16], rotation=objectlookatposition(self, self.pde.input_manager.mouse_position) + shot + random.randint(-self.shotspread, self.shotspread)))
  
        return super().update()

    def shoot(self, angle):
        self.shooting = True
        return []

class GrenadeLauncher(Weapon):
    def __init__(self, man, pde, owner):
        self.scale = [56, 22]
        super().__init__(man, pde, owner)
        self.sprite = self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\topdownshooter\assets\sprites\weapons\grenadelauncher\grenadelauncher.png', layer=3)

        #----------< Weapon Info >----------#

        self.shotspread = 5
        self.shotangles = [0]
        self.firerate = 8
        self.bullet = Grenade

    def update(self):
        self.components["Sprite"].sprite.rotation = self.rotation
        return super().update()

    def shoot(self, angle):
        self.shooting = True
        bs = []
        if self.shottick >= self.firerate:
            self.shottick = 0
            for shot in self.shotangles:
                b = self.man.add_object(obj=self.bullet(man=self.man, pde=self.pde, owner=self, target=self.pde.input_manager.mouse_position, position=[self.owner.position[0] + 10, self.owner.position[1] + 10], rotation=angle + shot + random.randint(-self.shotspread, self.shotspread)))
                b.onshot()
                bs.append(b)
        return bs