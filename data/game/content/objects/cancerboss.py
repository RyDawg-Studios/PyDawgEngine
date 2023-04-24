from data.engine.actor.actor import Actor
from data.engine.projectile.projectile_component import ProjectileComponent
from data.engine.sprite.sprite_component import SpriteComponent
from data.game.content.objects.bullet import Bullet
from data.engine.fl.world_fl import objectlookattarget
import random
from data.game.content.objects.cancerbullet import CancerBullet
from data.engine.projectile.projectile import Projectile

class CancerCell(Actor):
    def __init__(self, man, pde, owner, bossman, position=[0,0], scale=[30,30], rotation=0, checkForCollision=False, checkForOverlap=True, spawner=None, hp=30, duperate = random.randint(10, 20), gen=1):
        super().__init__(man, pde)
        self.position=position
        self.scale=scale
        self.checkForCollision=checkForCollision
        self.checkForOverlap=checkForOverlap
        self.useCenterForPosition = True
        self.lifetime=-1
        self.rotation=rotation
        self.spriteRotation = 0
        self.maxhp = hp
        self.hp = self.maxhp
        self.shottick = 0
        self.dupetick = 0
        self.duperate = duperate
        self.firerate = 141 - pde.game.difficulty
        self.owner = owner
        self.shotInfo = {'piercing': False, 'fireRate': self.firerate, 'offsets': [0], 'accuracyBand': 40, 'bulletSpeed': 6, 'bulletScale': [20, 20]}
        self.shotType = 'Normal'
        self.player = man.getPlayers()
        self.damagable = True
        self.freespots = ['up', 'down', 'left', 'right']
        self.gen = gen
        self.bossman = bossman
        if spawner != None:
            self.freespots.remove(spawner)

    def construct(self):
        super().construct()

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\cancercell.png', layer=2)

    def update(self):
        self.dupetick += 1
        if self.dupetick >= self.duperate:
            if self.gen < 12:
                if len(self.freespots) > 0:
                    self.duperate += 10
                    spot = random.choice(self.freespots)
                    self.freespots.remove(spot)

                    if spot == 'down':
                        obj = self.man.add_object(CancerCell(man=self.man, pde=self.pde, position=self.rect.midbottom, owner=self, hp=self.maxhp*0.70, duperate=self.duperate*3.3, gen=self.gen+1, spawner='up', bossman=self.bossman))
                    elif spot == 'up':
                        obj = self.man.add_object(CancerCell(man=self.man, pde=self.pde, position=self.rect.midtop, owner=self, hp=self.maxhp*0.70, duperate=self.duperate*3.3, gen=self.gen+1, spawner='down',bossman=self.bossman))
                    elif spot == 'left':
                        obj = self.man.add_object(CancerCell(man=self.man, pde=self.pde, position=self.rect.midleft, owner=self, hp=self.maxhp*0.70, duperate=self.duperate*3.3, gen=self.gen+1, spawner='right',bossman=self.bossman))
                    elif spot == 'right':
                        obj = self.man.add_object(CancerCell(man=self.man, pde=self.pde, position=self.rect.midright, owner=self, hp=self.maxhp*0.70, duperate=self.duperate*3.3, gen=self.gen+1, spawner='left',bossman=self.bossman))

                    self.bossman.segments.append(obj)
                    self.dupetick = 0





        self.shottick += 1
        if self.shottick == self.shotInfo['fireRate']:
            self.shottick = 0
            self.shoot()

        
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
            self.man.add_object(CancerBullet(man=self.man, pde=self.pde, owner=self, position=[self.rect.center[0], self.rect.center[1]], rotation=objectlookattarget(self, self.player) + i*30, scale=[20, 20], speed=[6, 6] , lifetime=400)) 

        if self in self.bossman.segments:
            self.bossman.segments.remove(self)
        self.deconstruct()

    def shoot(self):
        rot = objectlookattarget(self, self.player)
        self.spriteRotation = rot
        rand = random.randint(-self.shotInfo['accuracyBand'], self.shotInfo['accuracyBand'])
        for inx, bl in enumerate(self.shotInfo['offsets']):
            self.man.add_object(CancerBullet(man=self.man, pde=self.pde, owner=self, position=[self.rect.center[0], self.rect.center[1]], rotation=rot + rand + self.shotInfo['offsets'][inx], scale=self.shotInfo['bulletScale'], speed=[self.shotInfo['bulletSpeed'], self.shotInfo['bulletSpeed']] , lifetime=400, piercing=self.shotInfo['piercing'])) 


