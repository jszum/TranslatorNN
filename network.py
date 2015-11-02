#!/usr/bin/python

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer, SigmoidLayer


if __name__ == "__main__":


	net = FeedForwardNetwork()

	inputLayer = LinearLayer(144)
	hiddenLayer = SigmoidLayer(10)
	outputLayer = LinearLayer(4)

	net.addInputModule(inputLayer)
	net.addModule(hiddenLayer)
	net.addOutputModule(outputLayer)

	conn1 = FullConnection(inputLayer, hiddenLayer)
	conn2 = FullConnection(hiddenLayer, outputLayer)

	net.addConnection(conn1)
	net.addConnection(conn2)

	net.sortModules()
