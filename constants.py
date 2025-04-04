from perlin import *


#CONSTANTS
SIZE = 8


class chunk:
	def __init__(self, pos, data, borderTop, borderBottom, borderLeft, borderRight):
		self.pos = pos
		self.data = data
		self.borderTop = borderTop
		self.borderBottom = borderBottom
		self.borderLeft = borderLeft
		self.borderRight = borderRight

	def draw_self(self, pos = (0,0)):
		pass

	def declare_position(self):
		print(self.pos)

class tile:
	def __init__(self, pos, type, master, borderTop, borderBottom, borderLeft, borderRight):
		self.pos = pos
		self.type = type
		self.master = master
		self.borderTop = borderTop
		self.borderBottom = borderBottom
		self.borderLeft = borderLeft
		self.borderRight = borderRight

def populateWorld():
	world = []
	for yPos in range(SIZE):
		for xPos in range(SIZE):
			newChunk = chunk((xPos, yPos), [], (yPos == 0), (yPos == SIZE - 1), (xPos == 0), (xPos == SIZE - 1))
			world.append(newChunk)
	return world

def populateChunks(world):
	#this is really disgusting im so sorry
	for chunk in world:
		noisemap = genNoisemap(chunk.pos[0], chunk.pos[1])
		x = 0
		y = 0
		for i in len(noisemap):
			newTile = tile((x, y), noisemap[i], chunk, (y == 0), (y == 7), (x == 0), (x == 7))
			if x + 1 == 8:
				#8 = chunk size
				y += 1
				x = 0
			else:
				x += 1





