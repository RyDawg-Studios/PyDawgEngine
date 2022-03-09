import json


class ConfigManager():
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        
    def activate(self):
        file = open(r"data\engine\cfg\engineconfig.json")
        self.config = json.load(file)
        
    def update(self):
        pass
        
    def activate(self):
        pass