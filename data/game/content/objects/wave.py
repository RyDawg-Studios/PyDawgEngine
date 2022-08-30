class Wave():
    def __init__(self, owner):
        self.owner = owner
        self.om = owner.man
        self.active = True
        self.time = 0
        self.timeTarget = 1400

    def update(self):
        if self.active:
            self.time += 1
            if self.time == self.timeTarget:
                self.time = 0
                if self.active == True:
                    self.onfinish()
                self.active = False

    def onfinish(self):
        pass
