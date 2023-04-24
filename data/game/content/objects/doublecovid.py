from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.game.content.objects.bullet import Bullet
from data.engine.fl.world_fl import objectlookattarget
import random
from data.game.content.objects.covidbullet import CovidBullet

from data.engine.projectile.projectile import Projectile

class DoubleCovid(Actor):
    def __init__(self, man, pde, owner, position=[0,0], scale=[180,180], rotation=0, checkForCollision=False, checkForOverlap=True, bossman=None):
        self.position=position
        self.scale=scale
        self.pde = pde
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.useCenterForPosition = True
        self.lifetime=-1
        self.rotation=rotation
        self.spriteRotation = 0
        self.maxhp = 200 + pde.game.difficulty * 5
        self.hp = self.maxhp
        self.shottick = 0
        self.firerate = 41 - pde.game.difficulty
        self.owner = owner
        self.shotInfo = {'piercing': False, 'fireRate': self.firerate, 'offsets': [0, -30, 30], 'accuracyBand': 10, 'bulletSpeed': 6, 'bulletScale': [20, 20]}
        self.shotType = 'Normal'
        self.player = man.getPlayers()
        self.damagable = True
        self.bossman = bossman

        super().__init__(man, pde)

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\covid.png', layer=2)
        
    def move(self, movement):
        pass

    def update(self):
        self.shottick += 1
        if self.shottick == self.shotInfo['fireRate']:
            self.shottick = 0
            self.shoot()

        self.shotInfo = {'piercing': False, 'fireRate': self.firerate, 'offsets': [0, -30, 30], 'accuracyBand': 0, 'bulletSpeed': 8, 'bulletScale': [20, 20]}
        
        return super().update()

    def overlap(self, obj):
        if obj.__class__ == Bullet:
            if self.damagable:
                if obj.owner != self:
                    if not obj.piercing:
                        obj.deconstruct()
                    self.hp -= 1
                    if self.hp <= 0:
                        self.die()
                        obj.owner.score += 8000
        return super().overlap(obj)

    def die(self):
        for i in range(1, 13):
            self.man.add_object(CovidBullet(man=self.man, pde=self.pde, owner=self, position=[self.rect.center[0], self.rect.center[1]], rotation=objectlookattarget(self, self.player) + i*30, scale=[20, 20], speed=[6, 6] , lifetime=400)) 
        if self in self.bossman.segments:
            self.bossman.segments.remove(self)

        print("Dead")
        self.deconstruct()

    def shoot(self):
        rot = objectlookattarget(self, self.player)
        self.spriteRotation = rot
        rand = random.randint(-self.shotInfo['accuracyBand'], self.shotInfo['accuracyBand'])
        for inx, bl in enumerate(self.shotInfo['offsets']):
            self.man.add_object(CovidBullet(man=self.man, pde=self.pde, owner=self, position=[self.rect.center[0], self.rect.center[1]], rotation=rot + rand + self.shotInfo['offsets'][inx], scale=self.shotInfo['bulletScale'], speed=[self.shotInfo['bulletSpeed'], self.shotInfo['bulletSpeed']] , lifetime=400, piercing=self.shotInfo['piercing'])) 


