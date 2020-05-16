from terrabot.events.events import Events
import logging

class Packet37Parser(object):

    def parse(self, world, player, data, ev_man):
        logging.debug('Received packet 37 (login password requested)')
        ev_man.raise_event(Events.PasswordRequested, None)
