from . import packet


class Packet61(packet.Packet):
    def __init__(self, player):
        super(Packet61, self).__init__(61)
        self.addData(chr(player.playerID))
        self.addData(chr(1))
