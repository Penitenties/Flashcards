#!/usr/bin/python3
import readWrite



if __name__== "__main__":
	readWrite.repopSave()
	temp = readWrite.load("testData.txt")
	flashcards = temp[0]
	challenges = temp[1]
	print(flashcards, challenges)
	readWrite.write("testData.txt",flashcards, challenges)

