import random
from data.engine.actor.actor import Actor
from data.game.content.objects.cancerbullet import CancerBullet
from data.game.content.objects.covidbullet import CovidBullet
from data.game.content.player.SciGameController import SciGameController
from data.engine.sprite.sprite_component import SpriteComponent
from data.game.content.objects.badblood import SickleCell
from data.game.content.objects.bullet import Bullet
from data.game.content.objects.reticle import Reticle
from data.engine.fl import world_fl


class DawgTalePlayer(Actor):
    def __init__(self, man, pde, scale=[32, 32], position=[600, 400], rotation=0):
        super().__init__(man, pde)
        self.scale = scale
        self.position=position
        self.rotation=rotation
        self.useCenterForPosition = True
        self.checkForCollision = True
        self.checkForOverlap = True
        self.maxHealth = 1
        self.health = self.maxHealth
        self.dead = False
        self.ticks = 0
        self.deadticks = 0
        self.superticks = 0
        self.accuracyRange = 5
        self.fireRate = 12
        self.score = 0
        self.roundScore = 0
        self.canShoot = True
        self.shotType = 'single'
        self.super = False
        self.supertime = 1500
        self.bulletspeed = 8
        self.shotInfo = {'piercing': False, 'fireRate': self.fireRate, 'offsets': [0], 'accuracyBand': self.accuracyRange, 'bulletSpeed': self.bulletspeed, 'bulletScale': [20, 20]}
        self.moveable = True

        pde.player_manager.__init__(pde=pde)




    def construct(self):
        super().construct()

        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\sci_wbloodcell.png', layer=6 )
        self.components["PlayerController"] = SciGameController(owner=self)

        self.reticle = self.man.add_object(Reticle(man=self.man, pde=self.pde, player=self))

        self.pde.game.bossesKilled = 0

    def overlap(self, obj):
        if isinstance(obj, SickleCell):
            if not self.dead:
                obj.deconstruct()
                self.takedamage(1)
        if isinstance(obj, CovidBullet) or isinstance(obj, CancerBullet):
            if obj.owner != self:
                obj.deconstruct()
                self.takedamage(1)

    def update(self):
        super().update()
        self.pde.game.score = self.score
        self.ticks += 1
        self.superticks += 1
        if self.dead:
            self.canShoot = False
            self.canMove = False
            self.deadticks += 1
            self.reticle.deconstruct()
            self.components["Sprite"] = None
            self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\sci_wbloodcell4.png', layer=1)
            if self.deadticks >= 100:
                self.pde.game.loadtitlelevel()

        self.checkforsuper()
        
        if self.super:
            self.superticks += 1
            if self.superticks > self.supertime:
                self.super = False
                self.shotType = 'single'
                self.superticks = 0

    def takedamage(self, dmg):
            self.health -= dmg
            if self.health <=0:
                self.dead = True

    def shoot(self):
        if self.canShoot:
            rand = random.randint(-self.shotInfo['accuracyBand'], self.shotInfo['accuracyBand'])
            for inx, bl in enumerate(self.shotInfo['offsets']):
                self.man.add_object(Bullet(man=self.man, pde=self.pde, owner=self, position=[self.rect.center[0], self.rect.center[1]], rotation=world_fl.objectlookattarget(self, self.reticle) + rand + self.shotInfo['offsets'][inx], scale=self.shotInfo['bulletScale'], speed=[self.shotInfo['bulletSpeed'], self.shotInfo['bulletSpeed']] , lifetime=400, piercing=self.shotInfo['piercing'])) 


    def shootatangle(self, angle):
        if self.canShoot:
            self.man.add_object(Bullet(man=self.man, pde=self.pde, owner=self, position=[self.rect.center[0], self.rect.center[1]], rotation=angle, scale=[15, 15], speed=[self.bulletspeed, self.bulletspeed] , lifetime=400, piercing=True)) 

    def chosepowerup(self):
        self.super = True
        self.shotType = random.choice(['triple', 'cranking', 'piercing'])
        self.superticks = 0


    def checkforsuper(self):
        if self.shotType == 'triple':
            self.shotInfo['offsets'] = [0, 20, -20]

        elif self.shotType == 'cranking':
            self.shotInfo['offsets'] = [0, 90, -90, 180]

        elif self.shotType == 'piercing':
            self.shotInfo['piercing'] = True
            self.shotInfo['fireRate'] = 6
            self.shotInfo['accuracyBand'] = 0
        
        elif self.shotType == 'huge':
            self.shotInfo['bulletScale'] = [30, 30]
            self.shotInfo['fireRate'] = 9

        else:
            self.shotInfo = {'piercing': False, 'fireRate': 12, 'offsets': [0], 'accuracyBand': 5, 'bulletSpeed': 8, 'bulletScale': [20, 20]}
            
