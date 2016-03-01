#!/usr/bin/python
import os

def main():
	input = raw_input("What's the shape? ")

	if input == 'triangle':		
		triangle()

def triangle():
	pedestal = input("Insert triangle pedestal ")
	height = input("Insert triangle height ")

	result = pedestal * height / 2
	print "Result:", result

if __name__ == '__main__':
	main()
