from . import packet


class Packet13(packet.Packet):
    def __init__(self, player):
        super(Packet13, self).__init__(13)
        self.addData(chr(player.playerID))
        self.addData(chr(0))
        self.addData(chr(0))
        self.addStructuredData("<f", world.spawnX)
        self.addStructuredData("<f", world.spawnY)
        self.addStructuredData("<f", 0)
        self.addStructuredData("<f", 0)
        self.addData(chr(255))
