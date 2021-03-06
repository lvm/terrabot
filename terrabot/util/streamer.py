import string
import struct


class Streamer(object):
    """A class for streaming data from a databuffer."""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def next_short(self):
        result = struct.unpack("<h", self.data[self.index : self.index + 2])[0]
        self.index += 2
        return result

    def next_u_short(self):
        result = struct.unpack("<H", self.data[self.index : self.index + 2])[0]
        self.index += 2
        return result

    def next_int32(self):
        result = struct.unpack("<i", self.data[self.index : self.index + 4])[0]
        self.index += 4
        return result

    def next_byte(self):
        result = self.data[self.index]
        self.index += 1
        return result

    def next_str(self):
        idx = 1
        result = ""
        while True:
            (b,) = struct.unpack("1b", self.data[self.index + idx : self.index + idx + 1])
            if chr(b) not in string.printable:
                break
            result += chr(b)
            idx += 1

        self.index += idx
        return result

    def next_float(self):
        result = struct.unpack("<f", self.data[self.index : self.index + 4])[0]
        self.index += 4
        return result

    def remainder(self):
        return self.data[self.index :]
