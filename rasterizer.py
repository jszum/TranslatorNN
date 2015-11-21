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
		self.image = Image.open(file).convert('L')
		self.xsize = self.image.size[0]
		self.ysize = self.image.size[1]

	def showimage(self):
		print self.image.getpixel((1,2))

	def binarize(self):
		self.array = []
		for y in range(self.ysize):
			for x in range(self.xsize):
				gray_value = self.image.getpixel((x,y))	

				if(gray_value < 150):			
					self.array.append(1)
				else:
					self.array.append(0)

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








