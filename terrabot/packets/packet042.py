from . import packet


class Packet42(packet.Packet):
    def __init__(self, player):
        super(Packet42, self).__init__(42)
        self.add_data(player.playerID)
        self.add_structured_data("<h", player.currMana)
        self.add_structured_data("<h", player.maxMana)
