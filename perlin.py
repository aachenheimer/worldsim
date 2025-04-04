#from pynoise import *
from pynoise.noisemodule import Perlin
from pynoise.noiseutil import noise_map_plane
from pynoise.noiseutil import terrain_gradient
from pynoise.noiseutil import RenderImage

perlin = Perlin(octaves=1, persistence=0.20)

def genNoisemap(shift_x, shift_y):
	lower_x = (shift_x * 2) + 1
	upper_x = (shift_x * 2) + 2
	lower_z = (shift_y * 2) + 1
	upper_z = (shift_y * 2) + 2
	noisemap = noise_map_plane(width = 8, height=8, lower_x, upper_x, lower_z, upper_z, source=perlin)
	return noisemap

#noisemap = noise_map_plane(width=64, height=64, lower_x=1, upper_x=2, lower_z=1, upper_z=2, source=perlin)
#SHOULD BE SIZE * 8

'''f = open("perlin.txt", "w")
for x in noisemap:
	f.write(str(x))
#FOR TESTING
print(len(noisemap))
'''

'''gradient = terrain_gradient()
render = RenderImage()
render.render(64, 64, noisemap, 'test.png', gradient)
THIS REFUSES TO WORK'''

