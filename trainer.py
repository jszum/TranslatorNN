#!/usr/bin/python

import network
import sys
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer

in_neurons = 900
hid_neurons = 60
out_neurons = 4

def loadSet(dataset, filename):
	f = open(filename, 'r')

	counter = 0	

	for line in f.readlines():
		data = [float(x) for x in line.strip().split(',') if x != '']
		indata =  tuple(data[:in_neurons])
		outdata = tuple(data[in_neurons:])
		
		dataset.addSample(indata, outdata)
		counter = counter +1

def test(n, set):

	print str(n.net.indim) + '|' + str(set.indim)

	if n.net.indim == set.indim:
		print 'OK'
	else: 
		print 'ERROR'

	return n.net.indim == set.indim

if __name__=="__main__":

	data_file = ''
	net_file = ''
	epochs = 1



	netw = network.MyNet()
	ds = ClassificationDataSet(in_neurons,out_neurons)
	

	if len(sys.argv)==3:
		data_file = sys.argv[1]
		loadSet(ds, data_file)
		netw.constructNet(ds.indim,hid_neurons,ds.outdim)
		netw.setup()
		net_file = 'train.xml'
		epch = int(sys.argv[2])
		print "Opt1"
		

	if len(sys.argv)==4:
		data_file = sys.argv[1]
		net_file = sys.argv[3]
		epch = int(sys.argv[2])
		netw.loadFromFile(net_file)
		loadSet(ds, data_file)
		print "Opt2"

	
	t = BackpropTrainer(netw.net,ds,learningrate=0.01,momentum=0.5,verbose=True)

	t.trainEpochs(epochs=epch)

	netw.saveToFile(net_file)



