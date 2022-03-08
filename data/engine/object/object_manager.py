import pygame


class ObjectManager:

    def __init__(self, pde) -> None:
        self.objects = {}
        self.pde = pde
    

    def add_object(self, obj):
        self.objects[str(obj)] = obj
        return obj

    def remove_object(self, obj):
        try:
            self.objects.pop(str(obj))
        except:
            pass


    def update(self):
        for obj in list(self.objects.values()):
            obj.update()



