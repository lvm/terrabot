from . import packet


class Packet30(packet.Packet):

    def __init__(self, player):
        super(Packet30, self).__init__(30)
        self.add_data(chr(player.playerID))
        self.add_data(chr(1))
