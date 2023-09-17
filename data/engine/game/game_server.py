from data.engine.game.game import Game


class GameServer(Game):
    def __init__(self, pde):
        super().__init__(pde)

    def activate(self):
        super().activate()
        self.pde.server_manager.server.onPlayerJoin_Dispatcher.bind(self.add_player)
        return
