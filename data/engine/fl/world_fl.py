import math
import random
import numpy as np
import random as rng

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

def positionlookatposition(position1 = [0, 0], position2=[0,0]):
    sx = position1[0] - position2[0]
    sy = position1[1] - position2[1]

    a = math.atan2(sx, sy)
    d = math.degrees(a) 

    return d + 90

def getpositionlookatpositionvector(position, target):
    d = positionlookatposition(position, target)
    r = math.radians(d)
    f = [math.cos(r), -math.sin(r)]
    return Vector2(f)

def getpositionlookatvector(object, target):
    d = objectlookatposition(object, target)
    r = math.radians(d)
    f = [math.cos(r), -math.sin(r)]
    return Vector2(f)

def getobjectlookatvector(object, target):
    d = objectlookattarget(object, target)
    r = math.radians(d)
    return [round(math.cos(r), 3), -round(math.sin(r), 3)]


def getvectorfromrotation(rotation):
    v = Vector2(float(math.cos(math.radians(rotation))), float(math.sin(math.radians(rotation))))
    return v

def getobjectdistance(object1, object2):
    y1=object1.rect.centery
    y2=object2.rect.centery
    x1=object1.rect.centerx
    x2=object2.rect.centerx


    return abs(y2-y1/x2-x1)

def getpointdistance(x1, y1, x2, y2):
    try:
        a = abs(y2-y1/x2-x1)
    except ZeroDivisionError:
        a = 0
    return a

def normal_cut(mean,std,diff=3):
    """ Returns a value from a normal distribution, but limited to +-3std (no extreme outliers allowed)"""
    x = random.gauss(mean,std)
    x = max(mean-diff*std, min(mean+diff*std, x))
    return x

def normal_clamped_resample(mu=0, sigma=1, size=1, clamp_sigmas=2):
    """
        Normal distribution that guarantees no outliers futher than clamp_sigmas STDs.
        This is done by rerolling such outliers once, and clamping them if that doesn't help.
    """
    arr = rng.normal(loc=mu, scale=sigma, size=size)
    # find bad positions:
    inds = (arr < mu-clamp_sigmas*sigma) | (arr > mu+clamp_sigmas*sigma)
    to_resample = inds.sum()
    arr[inds] = rng.normal(loc=mu, scale=sigma, size=to_resample)
    # and finally clamp just in case, but should rarely ever be required
    return np.clip(arr, mu-clamp_sigmas*sigma, mu+clamp_sigmas*sigma)