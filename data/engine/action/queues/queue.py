class Queue():
    def __init__(self):
        self.actions = {}

    def addaction(self, action, name):
        action.name = name
        self.actions[name] = action

    def removeaction(self, name):
        self.actions[name].finished=True
        self.actions.pop[name]
