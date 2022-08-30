import pygame
from data.engine.component.component import Component


class Button(Component):
    def __init__(self, owner, bind=None, bindid=0):
        super().__init__(owner)
        self.state = {'Hovered': False, 'Pressed': False, 'ButtonID': -1}
        self.bind = bind
        self.bindid = bindid

    def update(self):
        if self.owner.rect.collidepoint(self.owner.pde.mouse_manager.pos):
            if self.state["Hovered"] == False:
                self.onhovered()
            self.state["Hovered"] = True
        else:
            self.state["Hovered"] = False

        for id, mb in enumerate(self.owner.pde.input_manager.mouse_inputs):
            if mb == True and self.state["Hovered"]:
                if self.state["Pressed"] == False:
                    self.onpressed(id)

                self.state["Pressed"] = True
                self.state["ButtonID"] = id
                break
            
            else:
                self.state["Pressed"] = False
                self.state["ButtonID"] = -1
                
        if self.state["Hovered"]:
            self.whilehovered()
        else:
            self.whilenothovered()

        if self.state["Pressed"]:
            self.whilepressed()
        else:
            self.whilenotpressed()
            
        #pygame.display.set_caption(str(self.state))


    def onpressed(self, mbid):
        if self.bind != None:
            if mbid == self.bindid:
                self.bind()
        pass

    def onhovered(self):
        pass

    def whilepressed(self):
        pass

    def whilehovered(self):
        pass

    def whilenotpressed(self):
        pass

    def whilenothovered(self):
        pass


        