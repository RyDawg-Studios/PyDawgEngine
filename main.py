import pygame 
import struct
from data.engine.PyDawgEngine import PyDawgEngine

#Initialize Important Pygame Libs
pygame.init()
pygame.font.init()
pygame.joystick.init()

#Create Engine Object
if __name__ == '__main__':
    engine = PyDawgEngine()