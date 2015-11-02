#!/usr/bin/python

import rasterizer
import network
import sys


if __name__=="__main__":

	image = sys.argv[1]
	raster = rasterizer.Raster()

	raster.openImage(image)
	raster.binarize()
	raster.show()

	network = network.MyNet()
	network.constructNet(144,10,4)
	network.setup()

	network.saveToFile()


