from . import packet


class Packet8(packet.Packet):

    def __init__(self, player, world):
        super().__init__(8)
        self.add_structured_data("<i", -1)
        self.add_structured_data("<i", -1)
