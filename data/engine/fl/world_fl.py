import math

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