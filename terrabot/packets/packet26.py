from . import packet


class Packet26(packet.Packet):

    def __init__(self, password):
        super(Packet26, self).__init__(0x26)
        self.add_data(password, pascal_string=True)
