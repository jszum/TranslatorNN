#!/usr/bin/python

import sys
import Image
import random
if __name__=="__main__":

    try:
        img   = sys.argv[1]
        lines = int(sys.argv[2])
        dest  = sys.argv[3] 
    except IndexError:
	print "Not enough arguments img-noise-dest"
   

    image = Image.open(img).convert('L');
    pixels = image.load()
    xsize = image.size[0]
    ysize = image.size[1]

    line = int(random.uniform(0,ysize))
    
    for x in range(xsize):
	pixels[x, line] = 255;

    image.save(dest);
