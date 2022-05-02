from turtle import pos
from data.engine.actor.actor import Actor
from data.engine.fl.world_fl import getobjectlookatvector, getpositionlookatvector, objectlookattarget
from data.topdownshooter.content.objects.weapon.hitmarker.hitmarker import Hitmarker
from data.topdownshooter.content.objects.weapon.pickup.pickupweapon import PickupWeapon


class ShooterEntity(Actor):
    def __init__(self, man, pde, position=None, scale=[32, 32]):

        #----------< Transform Info >----------#
        if position is None: position = [0,0]
        self.position = position
        self.scale = scale
        self.useCenterForPosition = True

        #----------< Weapon Info >----------#
        
        self.weapon = None
        self.item = None

        #----------< Stat Info >----------#

        self.hp = 100
        self.dead = False
        self.damagable = True

        #----------< Dodge Info >----------#

        self.dodgeframe = 0
        self.dodgetime = 10
        self.dodging = False
        self.dodgecooldown = 200
        self.dodgecooldowntime = 50

        #----------< Tag Info >----------#
        
        self.homable = True
        self.canPickupWeapons = True
        self.canCollectExp = True
        self.canShoot = True

        #----------< Timer Info >----------#

        self.deadticks = 0


        super().__init__(man, pde)

    def shootweapon(self):
        pass

    def update(self):
        if self.dead:
            self.deadticks += 1
        self.dodgebuffer()
        self.weaponoffset()
        return super().update()

    def collide(self, obj, side):
        return super().collide(obj, side)

    def takedamage(self, obj):
        if self.damagable:
            self.hp -= obj.damage
            self.man.add_object(obj=Hitmarker(man=self.man, pde=self.pde, position=obj.position))
            #self.movement = getpositionlookatvector(self, obj.position) * -obj.kb
            if self.hp <= 0:
                if not self.dead:
                    self.dead = True
                    self.die(obj)
            return True
        else:
            return False

    def dodgeroll(self):
        self.damagable = False
        if self.movement[0] != 0 and abs(self.movement[0]) == abs(self.movement[1]):
            self.rect.centerx += (self.movement[0] * 3) * 0.6
            self.rect.centery += (self.movement[1] * 3) * 0.6
        else:
            self.rect.centerx += (self.movement[0] * 3)
            self.rect.centery += (self.movement[1] * 3)

    def dodgebuffer(self):
        self.dodgecooldown += 1
        if self.dodgecooldown >= self.dodgecooldowntime:
            if self.dodging:
                self.dodgeframe += 1
                self.dodgeroll()
                if self.dodgeframe >= self.dodgetime:
                    self.dodging = False
                    self.dodgeframe = 0
                    self.dodgecooldown = 0
                    self.damagable = True
        else:
            self.dodging = False


    def die(self, killer):
        rot = killer.rotation
        self.dropweapon(rot)
        if self.weapon != None:
            self.weapon.deconstruct()
        self.deconstruct()

    def weaponoffset(self):
        if self.weapon != None:
            self.weapon.rect.centerx = self.rect.centerx + 10
            self.weapon.rect.centery = self.rect.centery + 10

    def dropweapon(self, rotation=0):
        if self.weapon != None:
            self.man.add_object(obj=PickupWeapon(man=self.man, pde=self.pde, position=list(self.rect.center), rotation=rotation, weapon=self.weapon, speed=[4, 4]))
            self.removeweapon()

    def interact(self):
        for o in self.overlapInfo["Objects"]:
            if o.__class__ == PickupWeapon:
                if self.canPickupWeapons:
                    self.dropweapon(rotation=objectlookattarget(self, o))
                    self.changeweapon(o.weapon.__class__)
                    o.deconstruct()
                    return
            

    def changeweapon(self, cls):
        self.weapon = self.man.add_object(obj=cls(man=self.man, pde=self.pde, owner=self))

    def removeweapon(self):
        if self.weapon != None:
            self.weapon.deconstruct()
            self.weapon = None

    def useitem(self, item):
        item.use()