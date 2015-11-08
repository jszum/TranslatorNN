#!/usr/bin/python

import rasterizer
import sys
import os

morse_codes = {
	"b":[1,0,0,0],
	"c":[1,0,1,0],
	"f":[0,0,1,0],
	"h":[0,0,0,0],
	"j":[0,1,1,1],
	"l":[0,1,0,0],
	"p":[0,1,1,0],
	"q":[1,1,0,1],
	"v":[0,0,0,1],
	"x":[1,0,0,1],
	"y":[1,0,1,1],
	"z":[1,1,0,0]
}

def getImages(folder):
	imag = []
	for file in os.listdir(folder):
		if file.endswith(".png"):
			imag.append(file)

	return imag

def saveCsv(dlist, name):

	csvfile = open(name, 'w+')

	data = '\n'.join(str(e) for e in dlist)

	csvfile.write(data)
	csvfile.close() 

def buildSet(images):
	records = []
	raster = rasterizer.Raster()

	images = sorted(images)	
	print images

	for image in images:
		raster.openImage(directory+"/"+image)
		raster.binarize()
		arr = raster.get()

		data = ','.join(str(x) for x in arr)
		response = morse_codes[image[:-4]]
		record = data + ','+ ','.join(str(e) for e in response)

		records.append(str(record))

	return records

if __name__=="__main__":

	directory = os.path.abspath(sys.argv[1])
	dirname = os.path.basename(directory)
	images = getImages(directory)
	
	records = buildSet(images)

	saveCsv(records, "datasets/"+dirname)
