import json


class ConfigManager():
    def __init__(self, pde) -> None:
        self.active = False
        self.pde = pde
        file = open(r"data\engine\cfg\engineconfig.json")
        self.config = json.load(file)
        
    def activate(self):
        pass
        
    def update(self):
        pass
        