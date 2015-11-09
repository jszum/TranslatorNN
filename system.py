#!/usr/bin/python

import rasterizer
import network
import sys


if __name__=="__main__":

	image = sys.argv[1]
	net_file = sys.argv[2]

	raster = rasterizer.Raster()

	raster.openImage(image)
	raster.binarize()
	data = raster.get()

	netw = network.MyNet()
	netw.loadFromFile(net_file)
	result = netw.net.activate(data)

	print result


