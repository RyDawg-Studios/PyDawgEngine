import pygame

class Rectangle:
    def __init__(self, position, scale):
        self.position = position
        self.scale = scale
        self.color = (255, 255, 255)
        self.lineThickness = 1
        self.particles = []


    def containsParticle(self, particle):
        try:
            x, y = particle.rect.center
            bx, by = self.position
            w, h = self.scale
            if x >= bx and x <= bx+w and y >= by and y <= by+h:
                return True
            else:
                return False
        except:
            return False
        

    def containsPoint(self, point):
        try:
            x, y = point
            bx, by = self.position
            w, h = self.scale
            if x >= bx and x <= bx+w and y >= by and y <= by+h:
                return True
            else:
                return False
        except:
            return False

    def intersects(self, _range):
        selfrect = pygame.rect.Rect(self.position[0], self.position[1], self.scale[0], self.scale[1])
        rangerect = pygame.rect.Rect(_range.position[0], _range.position[1], _range.scale[0], _range.scale[1])
        return pygame.rect.Rect.colliderect(selfrect, rangerect)
    
    def getOverlapState(self, object):
        return
    
    def Draw(self, screen):
        x, y = self.position
        w, h = self.scale
        pygame.draw.rect(screen, self.color, [x, y, w, h], self.lineThickness)
        
class Circle:
    def __init__(self, position, radius):
        self.position = position
        self.radius = radius
        self.sqradius = self.radius * self.radius
        self.scale = None
        self.color = (255, 255, 255)
        self.lineThickness = 1

    def containsParticle(self, particle):
        x1, y1 = self.position
        x2, y2 = particle.position
        dist = pow(x2-x1, 2) + pow(y2-y1, 2)
        if dist <= self.sqradius:
            return True
        else:
            return False

    def intersects(self, _range):
        x1, y1 = self.position
        x2, y2 = _range.position
        w, h = _range.scale
        r = self.radius
        dist_x, dist_y = abs(x2-x1), abs(y2-y1)

        edges = pow(dist_x-w, 2) + pow(dist_y-h, 2)

        if dist_x > (r+w) or dist_y > (r+h):
            return False

        if dist_x <= w or dist_y <= h:
            return True

        return (edges <= self.sqradius)

    def Draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.lineThickness)
