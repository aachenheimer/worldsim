from perlin import *

#CONSTANTS
SIZE = 8

CAMERA_RANGE_HORIZONTAL = 8

CAMERA_RANGE_VERTICAL = 8


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
	def __init__(self, pos, type, symbol, master, borderTop, borderBottom, borderLeft, borderRight):
		self.pos = pos
		self.type = type
		self.symbol = symbol
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
		for i in range(len(noisemap)):
			newTile = tile((x, y), noisemap[i], "x", chunk, (y == 0), (y == 7), (x == 0), (x == 7))
			if noisemap[i] < 0: newTile.symbol = "o" #water
			elif noisemap[i] >= 0 and noisemap[i] < -0.4: newTile.symbol = "s" #sand
			elif noisemap[i] >= -0.4 and noisemap[i] < 0.6: newTile.symbol = "x" #grass
			elif noisemap[i] > 0.7: newTile.symbol = "m" #rock
			(chunk.data).append(newTile)
			if x + 1 == 8:
				#8 = chunk size
				y += 1
				x = 0
			else:
				x += 1
	return world

def findMaxima(world):
	low = (world[0].data)[0].type
	high = 0
	for chunk in world:
		for tile in chunk.data:
			if tile.type > high:
				high = tile.type
			elif tile.type < low:
				low = tile.type
	print(high)
	print(low)

def drawMapToFile(world):
	f = open("world.txt", "w")
	for iv in range(SIZE):
		for i in range(SIZE):
			for ii in range(8):
				#prints a line in every chunk
				for iii in range(8):
					#prints a line
					tileVal = world[(i * SIZE) + ii].data[(ii * 8) + iii].symbol
					#TILES RN = WATER (o), SAND (s), GRASS (x), ROCK (m)
					f.write(tileVal)
				#f.write(" ")
			f.write("\n")
		f.write("\n")
	f.close()
	#also this doesnt really work i think unless the noisemap is fucked up

def findViewedChunks(camera):
	nodes = [
	[int((camera[0] - CAMERA_RANGE_HORIZONTAL)//8), int((camera[1] - CAMERA_RANGE_VERTICAL)//8)],
	[int(camera[0]//8), int((camera[1] - CAMERA_RANGE_VERTICAL)//8)],
	[int((camera[0] + CAMERA_RANGE_HORIZONTAL)//8), int((camera[1] - CAMERA_RANGE_VERTICAL)//8)],
	[int((camera[0] - CAMERA_RANGE_HORIZONTAL)//8), int(camera[1]//8)],
	[int(camera[0]//8),int(camera[1]//8)],
	[int((camera[0] + CAMERA_RANGE_HORIZONTAL)//8), int(camera[1]//8)],
	[int((camera[0] - CAMERA_RANGE_HORIZONTAL)//8), int((camera[1] + CAMERA_RANGE_VERTICAL)//8)],
	[int(camera[0]//8), int((camera[1] + CAMERA_RANGE_VERTICAL)//8)],
	[int((camera[0] + CAMERA_RANGE_HORIZONTAL)//8), int((camera[1] + CAMERA_RANGE_VERTICAL)//8)]
	]
	print(nodes)
	return nodes

#function to return subtile

def findSubtile(camera):
	print([camera[0]%8, camera[1]%8])
	return (int(camera[0]%8), int(camera[1]%8))

def findViewedTiles(viewedChunks, subtile, world):
	#THIS RETURNS JUST THE DATA. completely unformatted. arranged by order of viewedchunks
	#also i think this wont work for right oriented chunks lol
	#yea this is completely busted LMAO
	#then in a seperate function you display them
	#lowkey this might just be a brute force and do this for every single individual viewed chunk
	viewedTiles = []
	for chunkPos in viewedChunks:
		chunk = world[(chunkPos[1]*SIZE) + chunkPos[0]]
		for i in range(subtile[1] * 8, 63):
			if subtile[0] == 0: viewedTiles.append(chunk.data[i].symbol)
			elif i % subtile[0] < subtile[0]: continue
			else: viewedTiles.append(chunk.data[i].symbol)
	print(viewedTiles)
	print(len(viewedTiles))
	return viewedTiles







