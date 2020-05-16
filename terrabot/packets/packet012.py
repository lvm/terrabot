from . import packet


class Packet12(packet.Packet):
    def __init__(self, player, world):
        super(Packet12, self).__init__(12)
        self.add_data(player.playerID)
        self.add_structured_data("<h", world.spawnX)
        self.add_structured_data("<h", world.spawnY)
