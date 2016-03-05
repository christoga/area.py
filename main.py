#!/usr/bin/python
import time
import math
__author__ = 'Andre Christoga'

def main():
	'''
	Area of the shape
	'''
	input = raw_input("What's the shape? ")

	if input == 'triangle':
		triangle()
	elif input == 'circle':
		circle()
	elif input == 'square':
		square()
	elif input == 'rectangle':
		square()
	elif input == 'trapezoid':
		trapezoid()
	else:
		print  'Shape is not available'

def init(self):
	pass

def triangle():
	'''
	Area of the triangle
	'''
	pedestal = input("Pedestal: ")
	height = input("Height: ")

	result = pedestal * height / 2
	print "Result:", result
	exit()

def circle():
	'''
	Area of the circle
	'''
	radiant = input("Radiant: ")

	ceil = radiant * 2 / math.pi
	result = math.ceil(ceil)
	print "Result:", result
	exit()

def square():
	'''
	Area of the square
	'''
	pedestal = input("Pedestal: ")
	height = input("Height: ")

	result = pedestal * height
	print "Result:", result
	exit()

def trapezoid():
	'''
	Area of the trapezoid
	'''
	width_1 = input("First width: ")
	width_2 = input("Second width: ")
	width = width_1 + width_2
	height = input("Vertical width: ")

	result = width / 0.5 * height
	print "Result: ", result
	exit()

def exit():
	'''
	Exit program
	'''
	exit = raw_input("Again? [y]Yes or [n]No: ")
	if exit == 'y':
		main()
	if exit == 'n':
		print 'Goodbye! '
		time.sleep(0.1)


if __name__ == '__main__':
	main()
