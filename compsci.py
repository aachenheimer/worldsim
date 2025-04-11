from pygame import *
from random import *
from constants import *

#general work

#size of the world

world = []

#9 chunks viewed at once

viewedChunks = []

subtile = [0, 0]

world = populateWorld()

world = populateChunks(world)

camera = [(SIZE * 8)/2, (SIZE * 8)/2]

findMaxima(world)

drawMapToFile(world)

viewedChunks = findViewedChunks(camera)

subtile = findSubtile(camera)

viewedTiles = findViewedTiles(viewedChunks, subtile, world)



#Pygame work
def draw_text(text = "test", fontParam = font.get_default_font(), size = 12, color = Color(255, 255, 255), pos = (0,0)):
	if fontParam != font.get_default_font():
		fontParam = font.match_font(fontParam)
	newFont = font.Font(fontParam, size)
	SCREEN.blit(newFont.render(text, True, color), pos)

font.init()
display.init()

SCREEN = display.set_mode((720, 360))

FONT = "bell"

#draw_text("hello world!", "bell", 144, Color(255, 255, 255), (0,0))

display.update()
while True:
	for events in event.get([KEYUP]):
		#remember that moving up is negative
		if events.key == K_UP and camera[1] - CAMERA_RANGE_VERTICAL > 0: 
			camera[1] -= 1
			print(camera)
			viewedChunks = findViewedChunks(camera)
			print("subtiles : ", end = '')
			subtile = findSubtile(camera)
		if events.key == K_DOWN and camera[1] + 1 + CAMERA_RANGE_VERTICAL < SIZE * 8: 
			camera[1] += 1
			print(camera)
			viewedChunks = findViewedChunks(camera)
			print("subtiles : ", end = '')
			subtile = findSubtile(camera)
		if events.key == K_RIGHT and camera[0] + 1 + CAMERA_RANGE_HORIZONTAL < SIZE * 8: 
			camera[0] += 1
			print(camera)
			viewedChunks = findViewedChunks(camera)
			print("subtiles : ", end = '')
			subtile = findSubtile(camera)
		if events.key == K_LEFT and camera[0] - CAMERA_RANGE_HORIZONTAL > 0: 
			camera[0] -= 1
			print(camera)
			viewedChunks = findViewedChunks(camera)
			print("subtiles : ", end = '')
			subtile = findSubtile(camera)
	event.pump()




