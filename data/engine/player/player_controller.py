from re import I
import pygame
from data.engine.component.component import Component
from data.engine.action.queues.queue import Queue

class PlayerController(Component):
    def __init__(self, owner, **kwargs) -> None:
        super().__init__(owner, **kwargs)
        self.inpman = self.owner.pde.input_manager
        self.max_player_speed = 2
        self.saved_pos = [0,0]
        self.resetPos = False
        self.ticks = 0
        self.test_queue = Queue()

        if len(self.inpman.joysticks) > 0:
            self.resetPos = False
        else:
            self.resetPos = True

        
    def update(self):
        if self not in self.owner.pde.game.player_controllers:
            self.owner.pde.game.player_controllers.append(self)
        self.manage_input()
        self.update_debug()

        return super().update()


    def manage_input(self):
        maxSpeed = self.owner.maxSpeed
        self.ticks += 1
        if pygame.K_RIGHT in self.owner.pde.input_manager.key_inputs or pygame.K_d in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[0] = maxSpeed[0]
        elif pygame.K_LEFT in self.owner.pde.input_manager.key_inputs or pygame.K_a in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[0] = -maxSpeed[0]
        else:
            if self.resetPos:
                self.owner.speed[0] = 0

        if pygame.K_UP in self.owner.pde.input_manager.key_inputs or pygame.K_w in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[1] = -maxSpeed[1]

        elif pygame.K_DOWN in self.owner.pde.input_manager.key_inputs or pygame.K_s in self.owner.pde.input_manager.key_inputs:
            self.owner.speed[1] = maxSpeed[1]

        else:
            if self.resetPos:
                self.owner.speed[1] = 0



        if self.owner.pde.input_manager.mouse_inputs[0] or pygame.K_SPACE in self.owner.pde.input_manager.key_inputs or self.owner.pde.input_manager.controller_axis_values[5] > 0:
            if self.ticks >= self.owner.shotInfo['fireRate']:
                self.owner.shoot()
                self.ticks = 0

    def on_joystick(self, event):

        if event.axis < 2:
            self.owner.speed[event.axis] = round(event.value * self.owner.maxSpeed[0])

        elif event.axis == 2 or event.axis == 3:
            self.owner.reticle.speed[event.axis-2] = event.value * 50



    def update_debug(self):
        pass

    def on_input(self, input):
        if input == pygame.K_f:
            self.saved_pos = [self.owner.rect.x, self.owner.rect.y]
            print("Position Logged @ " + str(self.saved_pos))
        if input == pygame.K_g:
            self.owner.rect.x, self.owner.rect.y = self.saved_pos
            print("Position Loaded @ " + str(self.saved_pos))
        if input == pygame.K_r:
            self.owner.pde.level_manager.removelevel("Main")
            self.owner.pde.game.loadstresslevel()
        if input == pygame.K_c:
            for r in range(0, 360):
                if r % 2:
                    self.owner.shootatangle(r)

        if input == 6:
            self.owner.pde.game.loadtitlelevel()



    def on_mouse(self, button):
        pass

    def deconstruct(self):
        self.owner.pde.game.player_controllers.remove(self)
        return super().deconstruct()