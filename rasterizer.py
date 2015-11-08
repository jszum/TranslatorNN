#!/usr/bin/python
import Image
import sys

class Raster:

	def __init__(self):
		self.filename = ''
		self.image = ''
		self.xsize = 0
		self.ysize = 0
		self.array = []

	def openImage(self, file):
		self.filename = file
		self.image = Image.open(file)
		self.xsize = self.image.size[0]
		self.ysize = self.image.size[1]

	def binarize(self):
		
		for y in range(self.ysize):
			for x in range(self.xsize):
				if self.image.getpixel((x,y)) == (255,255,255):
					self.array.append(0)
				else:
					self.array.append(1)

	def get(self):
		
		return self.array


	def show(self):

		for i in range(self.xsize):
			print self.array[i*self.ysize:(i+1)*self.ysize]

	
if __name__ == "__main__":

	png = sys.argv[1]
	raster = Raster()

	raster.openImage(png)
	raster.binarize()
	raster.show()








