#!/usr/bin/python3
import readWrite
from Set import Set
import addCards


if __name__== "__main__":
	readWrite.repopSave()
	temp = readWrite.load("testData.txt")
	f = temp[0]
	c = temp[1]	
	data = Set(f , c)
	addCards.addCards(data)
	readWrite.write("testData.txt", data.getf(), data.getc())
