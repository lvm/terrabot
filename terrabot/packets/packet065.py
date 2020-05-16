from . import packet


class Packet65(packet.Packet):

    def __init__(self, id, x, y):
        super(Packet65, self).__init__(65)
        self.add_data(2)  # Player tp flag
        self.add_data(id)
        self.add_structured_data("<h", x)
        self.add_structured_data("<h", y)
