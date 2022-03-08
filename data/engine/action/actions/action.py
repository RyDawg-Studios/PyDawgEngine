class Action():
    def __init__(self, queue) -> None:
        self.name = ""
        self.finished = False
        self.interupt = False
        self.interuptable = False
        self.queue = queue

        self.start()

    def start(self):
        print("Action {self.name} Started")
        while not self.finish:
            self.update()
        else:
            self.finish()
        
    def update(self):
        pass

    def finish(self):
        print("Action {self.name} Finished")
        del self
