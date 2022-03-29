import pygame
import json


class DisplayManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.group = pygame.sprite.LayeredUpdates()
        self.bg = False
        self.bgimg = ''
        

    def activate(self):
        self.configurewindow()

    def update(self):
        if self.bg == False:
            self.screen.fill((0,0,0))
        else:
            self.screen.blit(self.bg, (0, 0))

        self.group.update()
        self.group.draw(self.screen)

        pygame.display.update()

    def configurewindow(self):
        if eval(self.pde.config_manager.config["config"]["fullscreen"]):
            self.screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((640, 480))



        pygame.display.set_icon(pygame.image.load(eval(self.pde.config_manager.config["config"]["icon"])))
        pygame.display.set_caption(self.pde.config_manager.config["config"]["caption"])

    def changebackground(self, image):
        self.bg = pygame.image.load(image)
        self.bg = pygame.transform.scale(image, [100, 100])

        self.bg = True



