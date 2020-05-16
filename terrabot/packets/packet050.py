from . import packet


class Packet50(packet.Packet):

    def __init__(self, player):
        super(Packet50, self).__init__(50)
        self.add_data(player.playerID)
        for i in range(0, 22):
            self.add_data(0)
