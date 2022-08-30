# Finish This



class EventDispatcher():
    def __init__(self):
        self.bindings = []

    
    def bind(self, func):
        self.bindings.append(func)


    def call(self, **kwargs):
        for f in self.bindings:
            f(kwargs)