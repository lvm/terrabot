from . import packet


class Packet38(packet.Packet):

    def __init__(self, password):
        super(Packet38, self).__init__(38)
        self.add_data(password, pascal_string=True)
