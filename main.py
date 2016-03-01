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

def exit():
	exit = raw_input("Again? [y]Yes or [n]No: ")
	if exit == 'y':
		main()
	if exit == 'n':
		time.sleep(0.1)


if __name__ == '__main__':
	main()
