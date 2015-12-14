#!/usr/bin/python

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer, SigmoidLayer, TanhLayer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

class MyNet:

	def __init__(self, file='config.xml'):
		self.net = FeedForwardNetwork()
		self.file = file


	def constructNet(self, input, hidden, output): 
		inputLayer = LinearLayer(input)
		hiddenLayer = TanhLayer(hidden)
		outputLayer = LinearLayer(output)

		self.net.addInputModule(inputLayer)
		self.net.addModule(hiddenLayer)
		self.net.addOutputModule(outputLayer)

		conn1 = FullConnection(inputLayer, hiddenLayer)
		conn2 = FullConnection(hiddenLayer, outputLayer)

		self.net.addConnection(conn1)
		self.net.addConnection(conn2)

	
	def setup(self):
		self.net.sortModules()

	
	def saveToFile(self,file='config.xml'):
		NetworkWriter.writeToFile(self.net, file)


	def loadFromFile(self, file='config.xml'):
		self.net = NetworkReader.readFrom(file)


if __name__ == "__main__":

	network = MyNet()
	network.constructNet(144,10,4)
	network.setup()

	network.saveToFile()

	
