import pygame
import json


class DisplayManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.surfs = {}
        self.bg = False
        self.bgimg = ''
        

    def activate(self):
        self.configurewindow()



    def update(self):
        if self.bg == False:
            self.screen.fill((0,0,0))
        else:
            self.screen.blit(self.bg, (0, 0))
        for surf in self.surfs:
            for spr in self.surfs[surf]:
                self.screen.blit(spr.image, (spr.parent.rect.x, spr.parent.rect.y))
                

        pygame.display.update()



    def configurewindow(self):

        self.screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)

        pygame.display.set_icon(pygame.image.load(eval(self.pde.config_manager.config["config"]["icon"])))
        pygame.display.set_caption(self.pde.config_manager.config["config"]["caption"])

        self.createsurf(id=0)

    def createsurf(self, id=None):
        if id != None:
            self.surfs[id] = []

    def changebackground(self, image):
        self.bg = pygame.image.load(image)
        self.bg = pygame.transform.scale(image, [100, 100])
        self.surfs[0] = self.bg

        self.bg = True
    def activate(self):
        self.configurewindow()




