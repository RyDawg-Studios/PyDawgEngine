import pygame
from data.engine.actor.actor import Actor
from data.engine.sprite.sprite_component import SpriteComponent
from data.engine.widgets.button import Button
from data.engine.widgets.text import TextComponent
from data.game.content.objects.widgets.loadgame import LoadGameButton




class DifficultyChangerActor(Actor):
    def __init__(self, man, pde, state, position):
        super().__init__(man, pde)
        self.position=position
        self.scale=[60, 18]
        self.useCenterForPosition = True
        self.buttonTicks = 0
        
        self.state = state
        
    def construct(self):
        super().construct()
        self.components["Sprite"] = SpriteComponent(owner=self, sprite=r'data\game\assets\sci_up.png', layer=3)

        if self.state == 'up':
            self.components["Button"] = Button(owner=self, bind=self.raisedifficulty)

        elif self.state == 'down':
            self.components["Sprite"].sprite.rotation = 180
            self.components["Button"] = Button(owner=self, bind=self.lowerdifficulty)


    def raisedifficulty(self):
        if self.pde.game.difficulty < 20: 
            self.pde.game.difficulty += 1

    def lowerdifficulty(self):
        if self.pde.game.difficulty > 0: 
            self.pde.game.difficulty -= 1

    def update(self):
        if self.state == 'up':
            if self.pde.input_manager.hat_inputs[1] == 1:
                if self.buttonTicks == 0:
                    self.raisedifficulty()
                self.buttonTicks += 1
                if self.buttonTicks == 20:
                    self.buttonTicks = 0
            else:
                self.buttonTicks = 0

        if self.state == 'down':
            if self.pde.input_manager.hat_inputs[1] == -1:
                if self.buttonTicks == 0:
                    self.lowerdifficulty()
                self.buttonTicks += 1
                if self.buttonTicks == 20:
                    self.buttonTicks = 0
            else:
                self.buttonTicks = 0
        return super().update()

class DifficultyTextActor(Actor):
    def __init__(self, man, pde, position):
        super().__init__(man, pde)
        self.position = position
        self.scale=[60, 60]
        self.useCenterForPosition = True
        self.font = pygame.font.SysFont('impact.ttf', 72)

    def construct(self):
        super().construct()

        self.components["Text"] = TextComponent(owner=self, text=self.pde.game.difficulty, layer=3, font=self.font, color=(255, 255, 255))

    def update(self):

        self.components["Text"].sprite.text = str(self.pde.game.difficulty)
        return super().update()


class ScoreTextActor(Actor):
    def __init__(self, man, pde, position, scale):
        super().__init__(man, pde)
        self.position = position
        self.checkForCollision = False
        self.scale=scale
        self.useCenterForPosition = True
        self.spriteScale = [60, 20]
        self.font = pygame.font.SysFont('impact.ttf', 32)

    def construct(self):
        super().construct()

        self.components["Text"] = TextComponent(owner=self, text='score', layer=9, font=self.font, color=(255, 255, 255))

    def update(self):
        self.components["Text"].sprite.text = f'Score: {self.pde.game.score}'
        return super().update()





    