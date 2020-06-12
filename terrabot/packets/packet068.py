from . import packet

class Packet68(packet.Packet):
    def __init__(self, player):
        super().__init__(68)
        self.add_data(player.uuid, pascal_string=True)
