#!/usr/bin/python
import Image
import sys
import random
import os
	
if __name__ == "__main__":

	folder = sys.argv[1]
	noise = float(sys.argv[2])
	dest = sys.argv[3]


	for file in os.listdir(folder):
		if file.endswith(".png"):

			image = Image.open(folder+file).convert('L')

			xsize = image.size[0]
			ysize = image.size[1]

			pixels = image.load()

			for x in range(xsize):
				for y in range(ysize):

					chance = random.uniform(0, 1)
					if(chance < noise):
						val = random.uniform(0, 255)
						pixels[x, y] = int(val)

			image.save(dest+file)









