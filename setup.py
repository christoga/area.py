#!/usr/bin/python
import os

def main():		
	input = raw_input("What's the shape? ")

	if input == 'triangle':
		os.system("area/triangle.py")

if __name__ == '__main__':
	main()