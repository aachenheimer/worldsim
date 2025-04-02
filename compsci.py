from pygame import *
from random import *

#general work

#size of the world
SIZE = 8 

world = []

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
	for yPos in range(SIZE):
		for xPos in range(SIZE):
			newChunk = chunk((xPos, yPos), [], (yPos == 0), (yPos == SIZE - 1), (xPos == 0), (xPos == SIZE - 1))
			world.append(newChunk)

def populateChunks():




populateWorld()



#Pygame work
def draw_text(text = "test", fontParam = font.get_default_font(), size = 12, color = Color(255, 255, 255), pos = (0,0)):
	if fontParam != font.get_default_font():
		fontParam = font.match_font(fontParam)
	newFont = font.Font(fontParam, size)
	SCREEN.blit(newFont.render(text, True, color), pos)

font.init()
display.init()

SCREEN = display.set_mode()

FONT = "bell"

#draw_text("hello world!", "bell", 144, Color(255, 255, 255), (0,0))

display.update()

while True:
	pass




