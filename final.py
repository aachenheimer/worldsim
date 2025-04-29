from pynoise.noisemodule import Perlin
from pynoise.noiseutil import noise_map_plane
#pynoise developed by Tim Butram - https://pynoise.readthedocs.io/en/latest/

from pygame import *
#pygame developed by Pete Shinners - https://www.pygame.org

from random import *
seed()

from math import *

from time import *

#CONSTANTS
SIZE = 32

CAMERA_VERTICAL = 12
CAMERA_HORIZONTAL = 18

CLOCKSPEED = 0.75

#COLOR CONSTANTS
BACKGROUND = [0,0,0]
WATER = [0,127,127]
SAND = [255,213,66]
GRASS = [0,127,14]
ROCK = [99,99,99]

#VARIABLES
world = []
camera = [0, 0]

clock = time()

#PYNOISE WORK
perlin = Perlin(octaves=randint(1,5), persistence=random())
noisemap = noise_map_plane(width=SIZE, height=SIZE, lower_x=1, upper_x=randint(5,12), lower_z=1, upper_z=randint(5,12), source=perlin)

#PYGAME WORK
font.init()
display.init()
SCREEN = display.set_mode((720, 360))
FONT = font.Font(font.match_font("consolas"), 48)
display.update()

#GENERAL FUNCTIONS
class tile:
    def __init__(self, pos, data, symbol, color, borderTop, borderBottom, borderLeft, borderRight):
        self.pos = pos
        self.data = data
        self.symbol = symbol
        self.color = color
        self.borderTop = borderTop
        self.borderBottom = borderBottom
        self.borderLeft = borderLeft
        self.borderRight = borderRight
    def influence(self):
        if self.borderTop == False and randint(0,4) == 0:
            #affects above
            t = world[(self.pos[1]*SIZE)+self.pos[0]-SIZE]
            val = self.data
            t.data += val*0.001
            #deteriorates
            if val < -0.2:
                #water
                t.color[2] -= val
                self.symbol = "w"
            elif val >= -0.2 and val < 0:
                #sand
                t.color[0] -= val
                t.color[1] -= val
                self.symbol = "s"
            #additive
            elif val >= 0 and val < 0.7:
                #grass
                t.color[0] -= val * 2
                t.color[2] -= val
                self.symbol = "x"
            else:
                #rock
                if t.color[0] > 100: t.color[0] -= val
                else: t.color += val
                if t.color[1] > 100: t.color[1] -= val
                else: t.color[1] += val
                if t.color[2] > 100: t.color[1] -= val
                else: t.color[2] += val
                self.symbol = "m"
            if t.color[0] > 255: t.color[0] = 255
            elif t.color[0] < 0: t.color[0] = 0
            if t.color[1] > 255: t.color[1] = 255
            elif t.color[1] < 0: t.color[1] = 0
            if t.color[2] > 255: t.color[2] = 255
            elif t.color[2] < 0: t.color[2] = 0
        if self.borderBottom == False and randint(0,4) == 0:
            #affects below
            t = world[(self.pos[1]*SIZE)+self.pos[0]+SIZE]
            val = self.data
            t.data += val*0.001
            #deteriorates
            if val < -0.2:
                #water
                t.color[2] -= val
                self.symbol = "w"
            elif val >= -0.2 and val < 0:
                #sand
                t.color[0] -= val
                t.color[1] -= val
                self.symbol = "s"
            #additive
            elif val >= 0 and val < 0.7:
                #grass
                t.color[0] -= val * 2
                t.color[2] -= val
                self.symbol = "x"
            else:
                #rock
                if t.color[0] > 100: t.color[0] -= val
                else: t.color += val
                if t.color[1] > 100: t.color[1] -= val
                else: t.color[1] += val
                if t.color[2] > 100: t.color[1] -= val
                else: t.color[2] += val
                self.symbol = "m"
            if t.color[0] > 255: t.color[0] = 255
            elif t.color[0] < 0: t.color[0] = 0
            if t.color[1] > 255: t.color[1] = 255
            elif t.color[1] < 0: t.color[1] = 0
            if t.color[2] > 255: t.color[2] = 255
            elif t.color[2] < 0: t.color[2] = 0
        if self.borderLeft == False and randint(0,4) == 0:
            #affects left
            t = world[(self.pos[1]*SIZE)+self.pos[0]-1]
            val = self.data
            t.data += val*0.001
            #deteriorates
            if val < -0.2:
                #water
                t.color[2] -= val
                self.symbol = "w"
            elif val >= -0.2 and val < 0:
                #sand
                t.color[0] -= val
                t.color[1] -= val
                self.symbol = "s"
            #additive
            elif val >= 0 and val < 0.7:
                #grass
                t.color[0] -= val * 2
                t.color[2] -= val
                self.symbol = "x"
            else:
                #rock
                if t.color[0] > 100: t.color[0] -= val
                else: t.color += val
                if t.color[1] > 100: t.color[1] -= val
                else: t.color[1] += val
                if t.color[2] > 100: t.color[1] -= val
                else: t.color[2] += val
                self.symbol = "m"
            if t.color[0] > 255: t.color[0] = 255
            elif t.color[0] < 0: t.color[0] = 0
            if t.color[1] > 255: t.color[1] = 255
            elif t.color[1] < 0: t.color[1] = 0
            if t.color[2] > 255: t.color[2] = 255
            elif t.color[2] < 0: t.color[2] = 0
        if self.borderRight == False and randint(0,4) == 0:
            #affects right
            t = world[(self.pos[1]*SIZE)+self.pos[0]-1]
            val = self.data
            t.data += val*0.001
            #deteriorates
            if val < -0.2:
                #water
                t.color[2] -= val
                self.symbol = "w"
            elif val >= -0.2 and val < 0:
                #sand
                t.color[0] -= val
                t.color[1] -= val
                self.symbol = "s"
            #additive
            elif val >= 0 and val < 0.7:
                #grass
                t.color[0] -= val * 2
                t.color[2] -= val
                self.symbol = "x"
            else:
                #rock
                if t.color[0] > 100: t.color[0] -= val
                else: t.color += val
                if t.color[1] > 100: t.color[1] -= val
                else: t.color[1] += val
                if t.color[2] > 100: t.color[1] -= val
                else: t.color[2] += val
                self.symbol = "m"
            if t.color[0] > 255: t.color[0] = 255
            elif t.color[0] < 0: t.color[0] = 0
            if t.color[1] > 255: t.color[1] = 255
            elif t.color[1] < 0: t.color[1] = 0
            if t.color[2] > 255: t.color[2] = 255
            elif t.color[2] < 0: t.color[2] = 0
            
def populateWorld(size, noisemap):
    world = []
    for y in range(size):
        for x in range(size):
            val = noisemap[(y * size) + x]
            newTile = tile((x, y), val, "x", [255,255,255], (y == 0), (y == size - 1), (x == 0), (x == size - 1))
            if val < -0.2: 
                newTile.symbol = "w" #water
                newTile.color = [0,127,127]
            elif val >= -0.2 and val < 0: 
                newTile.symbol = "s" #sand
                newTile.color = [255,213,66]
            elif val >= 0 and val < 0.7: 
                newTile.symbol = "x" #ground
                newTile.color = [0,127,14]
            elif val > 0.7: 
                newTile.symbol = "m" #rock
                newTile.color = [99,99,99]
            world.append(newTile)
    return world
    
def findViewedTiles(world, camera, camera_horizontal, camera_vertical, size):
    origin = (camera[1]*size)+camera[0]
    tiles = [] #stores indices of which tiles are viewed
    for y in range(camera_vertical):
        for x in range(camera_horizontal):
            pos = (origin + (y*size))+x
            tiles.append(pos)
    return tiles
    
def findMaxima(world):
    low = world[0].data
    high = 0
    for i in world:
        if i.data > high:
            high = i.data
        elif i.data < low:
            low = i.data
    print(high)
    print(low)
    
def drawMapToFile(world, size):
    f = open("world.txt", "w")
    for y in range(size):
        for x in range(size):
            f.write(world[(y * size)+x].symbol)
        f.write("\n")
    f.close()
    
def printViewedTiles(world, viewedTiles, camera_horizontal, camera_vertical):
    print()
    for y in range(camera_vertical):
        for x in range(camera_horizontal):
            print(world[viewedTiles[x+(y*camera_horizontal)]].symbol, end='')
        print()
    
#PYGAME FUNCTIONS
def draw_text(text = "test", fontParam = font.get_default_font(), size = 12, color = Color(255, 255, 255), pos = (0,0)):
	if fontParam != font.get_default_font():
		fontParam = font.match_font(fontParam)
	newFont = font.Font(fontParam, size)
	SCREEN.blit(newFont.render(text, True, color), pos)
    
def drawTiles(world, viewedTiles, camera_horizontal, camera_vertical, fontParam):
    SCREEN.fill(BACKGROUND)
    for y in range(camera_vertical):
        for x in range(camera_horizontal):
            tile = world[viewedTiles[(y*camera_horizontal)+x]]
            SCREEN.blit(fontParam.render(tile.symbol, True, (int(tile.color[0]), int(tile.color[1]), int(tile.color[2]))), (x*24,y*24))
    display.update()
    
    
#NEARLY THERE, INITIALIZING
world = populateWorld(SIZE, noisemap)
viewedTiles = findViewedTiles(world, camera, CAMERA_HORIZONTAL, CAMERA_VERTICAL, SIZE)

drawMapToFile(world, SIZE)

drawTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL, FONT)

#MAIN LOOP
print("ready!")
while True:
    for events in event.get([KEYUP]):
        if events.key == K_UP and camera[1] - 1 >= 0:
            camera[1] -= 1
            viewedTiles = findViewedTiles(world, camera, CAMERA_HORIZONTAL, CAMERA_VERTICAL, SIZE)
            #printViewedTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL)
            drawTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL, FONT)
        if events.key == K_DOWN and camera[1] + 1 + CAMERA_VERTICAL < SIZE:
            camera[1] += 1
            viewedTiles = findViewedTiles(world, camera, CAMERA_HORIZONTAL, CAMERA_VERTICAL, SIZE)
            #printViewedTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL)
            drawTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL, FONT)
        if events.key == K_RIGHT and camera[0] + 1 + CAMERA_HORIZONTAL < SIZE:
            camera[0] += 1
            viewedTiles = findViewedTiles(world, camera, CAMERA_HORIZONTAL, CAMERA_VERTICAL, SIZE)
            #printViewedTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL)
            drawTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL, FONT)
        if events.key == K_LEFT and camera[0] - 1 >= 0:
            camera[0] -= 1
            viewedTiles = findViewedTiles(world, camera, CAMERA_HORIZONTAL, CAMERA_VERTICAL, SIZE)
            #printViewedTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL)
            drawTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL, FONT)
        for t in world:
            t.influence()
    event.pump()
    if time() - clock > CLOCKSPEED:
        clock = time()
        for tile in world:
            tile.influence()
        drawTiles(world, viewedTiles, CAMERA_HORIZONTAL, CAMERA_VERTICAL, FONT)