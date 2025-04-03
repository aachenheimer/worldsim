from pynoise import *
from pynoise.noisemodule import Perlin
from pynoise.noiseutil import noise_map_plane

perlin = Perlin()
noisemap = noise_map_plane(width=64, height=64, lower_x=1, upper_x=2, lower_z=1, upper_z=2, source=perlin)

print(noisemap)

f = open("perlin.txt", "w")
for x in range(64):
    for y in range(64):
        f.write(str(noisemap[x*y]))
        f.write("\n")

