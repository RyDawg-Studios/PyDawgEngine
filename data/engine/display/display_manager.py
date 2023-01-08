import pygame
import json


class DisplayManager:
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        self.group = pygame.sprite.LayeredUpdates()
        self.bg = False
        self.bgimg = ''
        self.scroll = [0, 0]
        

    def activate(self):
        self.configurewindow()

    def update(self):
        pygame.display.update()
        
        if self.bg == False:
            self.screen.fill((0,0,0))
        else:
            self.screen.blit(self.bg, (0, 0))

        for object in list(self.pde.level_manager.level.objectManager.objects):
            if hasattr(object, "rect"):
                if object.scroll == True:
                    object.rect.centerx -= self.scroll[0]
                    object.rect.centery -= self.scroll[1]

        self.group.update()
        self.group.draw(self.screen)


    def configurewindow(self):
        if self.pde.config_manager.config["config"]["fullscreen"]:
            self.screen = pygame.display.set_mode(self.pde.config_manager.config["config"]["dimensions"], pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.pde.config_manager.config["config"]["dimensions"])



        pygame.display.set_icon(pygame.image.load(eval(self.pde.config_manager.config["config"]["icon"])))
        pygame.display.set_caption(self.pde.config_manager.config["config"]["caption"])

    def changebackground(self, image):
        self.bg = pygame.image.load(image)
        self.bg = pygame.transform.scale(image, [100, 100])

        self.bg = True



