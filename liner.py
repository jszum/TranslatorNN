#!/usr/bin/python

import sys
import os
import Image
import random

if __name__=="__main__":

	try:
		folder	  = sys.argv[1]
		lines = int(sys.argv[2])
		dest  = sys.argv[3] 
	except IndexError:
		print "Not enough arguments img-noise-dest"


	for file in os.listdir(folder):
		print "Im in "+folder
		if file.endswith(".png"):
			image = Image.open(folder+file).convert('L')

			xsize = image.size[0]
			ysize = image.size[1]

			pixels = image.load()

			for iter in range(lines):
				line = int(random.uniform(0,ysize))
		
				for x in range(xsize):
					pixels[x, line] = 200;

			image.save(dest+file);
