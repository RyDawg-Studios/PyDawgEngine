import pygame 
from data.engine.PyDawgEngine import PyDawgEngine

#Initialize Important Pygame Libs
pygame.init()
pygame.font.init()
pygame.joystick.init()

#Create Engine Object
if __name__ == '__main__':
    engine = PyDawgEngine()

#-------< TODO >-------#
#  Fix AI freaking out when not having a weapon #
#  Health Component  #
#  HasComponent()    #
#  GetComponents()   #
#  Change References in Bullet from hasattr('hp') to HasComponent(HealthComponent) (Make an HP component while you're at it) #

