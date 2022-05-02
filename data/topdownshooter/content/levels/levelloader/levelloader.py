import json
from data.engine.debug.debugObject import TestActor
from data.engine.object.object import Object
from data.topdownshooter.content.objects.enemy.enemy import ShooterEnemy
from data.topdownshooter.content.objects.player.player import ShooterPlayer
from data.topdownshooter.content.tiles.tile import Tile


class LevelLoader(Object):
    def __init__(self, man, pde, level="default"):
        super().__init__(man, pde)
        f = open(r"data\topdownshooter\data\leveldata.json")
        self.levels = json.load(f)
        self.level = level

        self.tilekey = {'x': r'data\topdownshooter\assets\sprites\tiles\wall1.png'}
        self.objectkey = {'x': ShooterEnemy, 'p': ShooterPlayer}


        self.placeobjects()

    def placeobjects(self):
        for rinx, row in enumerate(self.levels[self.level]["layers"][0]):
            for oinx, obj in enumerate(row):
                if obj != '#':
                    self.man.add_object(obj=Tile(man=self.man, pde=self.pde, position=[(oinx*32) + 16, (rinx*32+ 16)], sprite=self.tilekey[obj]))
        
        for rinx, row in enumerate(self.levels[self.level]["layers"][1]):
            for oinx, obj in enumerate(row):
                if obj != '#':
                    self.man.add_object(obj=self.objectkey[obj](man=self.man, pde=self.pde, position=[(oinx*32) + 16, (rinx*32+ 16)]))
