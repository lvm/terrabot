from . import packets
from . import client

from terrabot.data.player import Player
from terrabot.data.world import World
from .events import Events, EventManager


class TerraBot(object):
    """A class that handles basic functions of a terraria bot like movement and login"""

    # Defaults to 7777, because that is the default port for the server
    def __init__(self, ip, port=7777, protocol=230,
                 name="Terrabot", password="", difficulty=0, uuid=""):
        super(TerraBot, self).__init__()

        self.protocol = protocol

        self.world = World()
        self.player = Player(name, difficulty, uuid)
        self.password = password
        self.evman = EventManager()
        self.client = client.Client(ip, port, self.player, self.world, self.evman)

        self.evman.method_on_event(Events.PlayerID, self.received_player_id)
        self.evman.method_on_event(Events.Initialized, self.initialized)
        self.evman.method_on_event(Events.Login, self.logged_in)
        self.evman.method_on_event(Events.ItemOwnerChanged, self.item_owner_changed)
        self.evman.method_on_event(Events.PasswordRequested, self.send_password)
        self.evman.method_on_event(Events.ClientUUID, self.client_uuid)
        # self.event_manager.method_on_event(events.Events.)

    def start(self):
        self.client.start()
        self.client.add_packet(packets.Packet1(self.protocol))

    def item_owner_changed(self, id, data):
        if self.player.logged_in:
            self.client.add_packet(packets.Packet22(data[0], data[1]))

    def received_player_id(self, event_id, data):
        self.client.add_packet(packets.Packet4(self.player))
        self.client.add_packet(packets.Packet16(self.player))
        self.client.add_packet(packets.Packet42(self.player))
        self.client.add_packet(packets.Packet50(self.player))
        for i in range(0, 83):
            self.client.add_packet(packets.Packet5(self.player, i))
        self.client.add_packet(packets.Packet6())

    def initialized(self, event, data):
        self.client.add_packet(packets.Packet8(self.player, self.world))

    def logged_in(self, event, data):
        self.client.add_packet(packets.Packet12(self.player, self.world))

    def send_password(self, event, data):
        if self.password:
            self.client.add_packet(packets.Packet38(self.password))
        else:
            print("ERROR: Server needed password to login but none was given!")
            self.stop()

    def client_uuid(self, event, data):
        self.client.add_packet(packets.Packet68(self.player))

    def message(self, msg, color=None):
        if self.player.logged_in:
            if color:
                hex_code = "%02x%02x%02x" % color
                msg = "[c/" + hex_code + ":" + msg + "]"
            self.client.add_packet(packets.Packet25(self.player, msg))

    def get_event_manager(self):
        return self.evman

    def stop(self):
        self.client.stop()
