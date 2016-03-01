#!/usr/bin/python
import time

def main():
	input = raw_input("What's the shape? ")

	if input == 'triangle':
		triangle()
	if input == 'circle':
		circle()
	if input == 'square':
		square()
	if input == 'rectangle':
		rectangle()
	if input == 'trapezoid':
		trapezoid()

def triangle():
	pedestal = input("Pedestal: ")
	height = input("Height: ")

	result = pedestal * height / 2
	print "Result:", result
	exit()

def circle():
	radiant = input("Radiant: ")

	result = radiant * 2 / 3.14
	print "Result:", result
	exit()

def square():
	pedestal = input("Pedestal: ")
	height = input("Height: ")

	result = pedestal * height
	print "Result:", result
	exit()

def rectangle():
	pedestal = input("Pedestal: ")
	height = input("Height: ")

	result = pedestal * height
	print "Result:", result
	exit()

def trapezoid():
	width_1 = input("First width: ")
	width_2 = input("Second width: ")
	width = width_1 + width_2
	height = input("Vertical width: ")

	result = width / 0.5 * height
	print "Result: ", result

def exit():
	exit = raw_input("Again? [y]Yes or [n]No: ")
	if exit == 'y':
		main()
	if exit == 'n':
		time.sleep(0.1)


if __name__ == '__main__':
	main()
