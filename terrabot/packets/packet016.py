from . import packet


class Packet16(packet.Packet):
    def __init__(self, player):
        super(Packet16, self).__init__(16)
        self.add_data(player.playerID)
        self.add_structured_data("<h", player.currHP)
        self.add_structured_data("<h", player.maxHP)
