import math

from pygame import Vector2

def objectlookattarget(object, target):
    sx = object.rect.center[0] - target.rect.center[0]
    sy = object.rect.center[1] - target.rect.center[1]

    a = math.atan2(sx, sy)
    d = math.degrees(a) 

    return d + 90

def objectlookatposition(object, position=[0,0]):
    sx = object.rect.center[0] - position[0]
    sy = object.rect.center[1] - position[1]

    a = math.atan2(sx, sy)
    d = math.degrees(a) 

    return d + 90

def getpositionlookatvector(object, target):
    d = objectlookatposition(object, target)
    r = math.radians(d)
    f = [round(math.cos(r), 3), -round(math.sin(r), 3)]
    return Vector2(f)

def getobjectlookatvector(object, target):
    d = objectlookattarget(object, target)
    r = math.radians(d)
    return [round(math.cos(r), 3), -round(math.sin(r), 3)]