from . import packet


class Packet6(packet.Packet):
    def __init__(self):
        super().__init__(6)
