import pygame
import json


class DisplayManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.surfs = {}

        self.screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
        #, pygame.FULLSCREEN
        self.bg = False

        self.bgimg = ''

        file = open(r"data\engine\cfg\engineconfig.json")
        self.cfg = json.load(file)

        self.icon = pygame.image.load(eval(self.cfg["config"]["icon"]))
        pygame.display.set_icon(self.icon)


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

        cap = self.cfg["config"]["caption"]
        pygame.display.set_caption(cap)

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




