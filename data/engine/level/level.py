from data.engine.object.object_manager import ObjectManager
import pygame

class Level:
    def __init__(self, man, pde) -> None:
        self.pde = pde
        self.pde.display_manager.__init__(pde=self.pde)
        self.manager = man
        self.objectManager = ObjectManager(pde=pde)
        self.background = ''
        
    def changebackground(self, bg):
        self.background = bg
        self.pde.display_manager.bg = pygame.image.load(self.background)

    def update(self):
        self.objectManager.update()
