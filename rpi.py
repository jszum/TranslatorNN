#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

PIN = 7

def blink(timer):
	
	GPIO.output(PIN, True) 
	time.sleep(timer)
	GPIO.output(PIN, False) 

def dot():
	print 'dot'
	blink(0.5)
	

def dash():
	print 'dash'
	blink(1.5)
	

def control(arr):
	for e in arr:
		if e == 0:
			dot()
		if e == 1:
			dash()

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(PIN, GPIO.OUT)	
		
def main():
	
	
	code = [1,0,0,0]
	control(code)


main()
