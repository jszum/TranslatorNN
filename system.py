#!/usr/bin/python

import rasterizer
import network
import sys
import numpy as np

morse_codes = {
	"1000":"b",
	"1010":"c",
	"0010":"f",
	"0000":"h",
	"0111":"j",
	"0100":"l",
	"0110":"p",
	"1101":"q",
	"0001":"v",
	"1001":"x",
	"1011":"y",
	"1100":"z"
}

def normalize(res):
	normalized = []

	for e in res:
		if e >= 0.7:
			normalized.append(1)
		if e <= 0.3:
			normalized.append(0)

	return normalized

def clasify(n):
	print n
	string = ""
	for e in n:
		string += str(e)

	try:
		print "qualified as letter: " + morse_codes[string]
	except KeyError, e:
		print "Character not recognized"


if __name__=="__main__":

	np.set_printoptions(precision=2, suppress=True)
	image = sys.argv[1]
	net_file = sys.argv[2]

	raster = rasterizer.Raster()

	raster.openImage(image)
	raster.binarize()
	data = raster.get()

	netw = network.MyNet()
	netw.loadFromFile(net_file)
	result = netw.net.activate(data)

	normalized = normalize(result)

	if len(normalized) == 4:
		print result
		clasify(normalized)
	
	else:
		print "Answer not recognized"

