import struct

class Packet7Parser(object):

	def parse(self, world, player, data):
		world.time = struct.unpack("<i", data[1:5])[0]
		world.daynight = ord(data[5])
		world.moonphase = ord(data[6])
		world.maxX = struct.unpack("<h", data[7:9])[0]
		world.maxY = struct.unpack("<h", data[9:11])[0]
		world.spawnX = struct.unpack("<h", data[11:13])[0]
		world.spawnY = struct.unpack("<h", data[13:15])[0]

		print world.spawnX
		print world.spawnY
