#!/usr/bin/python
import Image
import sys

def binarize(png):
	xsize = png.size[0]
	ysize = png.size[1]
	array = []
	for y in range(ysize):
		for x in range (xsize):
		
			if png.getpixel((x,y)) == (255,255,255):
				array.append(0)
			else:
				array.append(1)

	return array

def show(array, x, y):
	for i in range(x):
		print binary[i*y:i*y+y]

	
print sys.argv[1]
png = Image.open(sys.argv[1])
xsize = png.size[0]
ysize = png.size[1]

binary = binarize(png)
show(binary, xsize, ysize)
#sys.stdout.write(str(binary))







