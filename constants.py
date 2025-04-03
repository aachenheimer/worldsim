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

def populateChunks():
	pass