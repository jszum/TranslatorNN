#!/usr/bin/python

import system
import sys
import os

ba = []
ca = []
fa = []
ha = []
ja = []
la = []
pa = []
qa = []
va = []
xa = []
ya = []
za = []

def function():
	img = "sources30px/set1/b.png"
	answer = system.main(img, net)


def verify(expected, answer):

	letter = expected[-5:-4]

	result = 0
	if expected == answer:
		result = 1
		

	if letter == "b":
		ba.append(result)
	if letter == "c":
		ca.append(result)
	if letter == "f":
		fa.append(result)
	if letter == "h":
		ha.append(result)
	if letter == "j":
		ja.append(result)
	if letter == "l":
		la.append(result)
	if letter == "p":
		pa.append(result)
	if letter == "q":
		qa.append(result)
	if letter == "v":
		va.append(result)
	if letter == "x":
		xa.append(result)
	if letter == "y":
		ya.append(result)
	if letter == "z":
		za.append(result)

def count(array):
	summ = 0
	for e in array:
		summ = summ +e

	return sum
	

def stats():

	print "B recognized " + str(sum(ba)/float(len(ba))*100)
	print "C recognized " + str(sum(ca)/float(len(ca))*100)
	print "F recognized " + str(sum(fa)/float(len(fa))*100)
	print "H recognized " + str(sum(ha)/float(len(ha))*100)
	print "J recognized " + str(sum(ja)/float(len(ja))*100)
	print "L recognized " + str(sum(la)/float(len(la))*100)
	print "P recognized " + str(sum(pa)/float(len(pa))*100)
	print "Q recognized " + str(sum(qa)/float(len(qa))*100)
	print "V recognized " + str(sum(va)/float(len(va))*100)
	print "X recognized " + str(sum(xa)/float(len(xa))*100)
	print "Y recognized " + str(sum(ya)/float(len(ya))*100)
	print "Z recognized " + str(sum(za)/float(len(za))*100)


if __name__=="__main__":


	net = "config/extended.xml"

	for (dir, _, files) in os.walk(sys.argv[1]):
		for f in files:
			if f.endswith(".png"):
				path = os.path.join(dir,f)
				filepath = path
				expected =  os.path.basename(path)
				answer = system.main(filepath, net)
		
				verify(expected, answer)

	stats()



	
