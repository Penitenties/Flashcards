#!/usr/bin/python3
#tabstop = 4 : python 3.6.5
import json
import sys

#loads a json file from the path savefile  and turns puts it into the global arrays.
def load(savefile):
	try:
		f = open(savefile, "r")
	except FileNotFoundError:
		makeSave(savefile)
		f = open(savefile, "r")
	contents = f.read()
	f.close()
	return initializefc(contents)

#takes a json formated string and returns an array containing the flashcards and challenges dicts
def initializefc(jsonString):
	flashcards  = []
	challenges = []
	data = json.loads(jsonString)
	for x in data.items():
		if x[1]["type"] == "flashcard":
			flashcards.append(x)
		elif x[1]["type"] == "challenge":
			challenges.append(x)
		else:
			print("unexpected type \""+x["type"]+"\"in initializefc")
	result = [flashcards, challenges]
	return result

#creates a savefile if it does not exist
def makeSave(savefile):
	uin = "hi"
	while (uin.lower() != "y") and (uin.lower() != "n"):
		uin = input("You do not have a save file, create one? (y/n)")
	if uin.lower is "n":
		print("okay . . .")
		sys.exit()
	if uin.lower is "y":
		f = open(savefile, "a")
		f.close()	

#writes the flashcard and challenges global arrays into the save file	
def write(savefile, flashcards, challenges):
	towrite = ""
	if flashcards is not None:
		towrite += json.dumps(flashcards)
	if challenges is not None:
		towrite += json.dumps(challenges)		
	f = open(savefile, "w+")
	f.write(towrite)
	f.close()

#repopulates the save with test data whenever I mess up and wipe or corrupt it
def repopSave():
	towrite = temp = {"type" : "flashcard", "front" : "hello" , "back" : "world" , "lastserved" : "time" , "percetwrong" : .5 , "tags" : "test"}
	towrite = {0 : temp}	
	towrite = json.dumps(towrite)	
	f = open("testData.txt", "w")
	f.write(towrite)
	f.close()
