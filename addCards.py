import json
import Set
import sys
from datetime import datetime

#add enter !quit to quit at any point

#takes in the cards object and returns a card dict
def makeCard(cardset):
	flashcards = cardset.getf()
	#get data from user
	temp = flashcards[-1][0]
	idz = int(temp) + 1
	typez = "flashcard"
	front = input("Enter the text for the front of the card: ")
	back = input("Enter the text for the back of the card: ")
	lastserved = datetime.now()
	percentwrong = 0.0
	tags = input("Enter any tags you want asociated with this card: ")
	#input verification
	scrap = "hi"
	while (scrap.lower() != "y") and (scrap.lower() != "n"):
		scrap = input("Add this card to the card set? (y/n) ")
	if scrap.lower() == "n":
		return None
	#build card
	body = {"type":typez,"front":front,"back":back,"lastserved":lastserved,"percentwrong":percentwrong,"tags":tags}
	card = {idz : body}
	return card

#takes a card set object and returns an cardset object with the added cards
def addCards(cardset):
	goOn = "hi"
	while (goOn.lower() != "y") and (goOn.lower() != "n"):
		toAdd = makeCard(cardset)
		if toAdd is not None:
			cardset.addf(toAdd)
		goOn = input("Make another card? (y/n) ")
	return cardset

#takes in a file formated, front,back,tags\nfront,back,tags and adds the cards to a card set, or creates a new setreturns a Set
def bulkAddf(path, cardset=None):
	
	cards = []
	idz = 0
	isnew = False
	
	if cardset is not None:
		idz = int(cardset.getf()[-1]["id"])
		isnew = True
	
	f = open("path", "r")
	for x in f:
		x.split(",")
		typez = "flashcard"
		front = x[0]
		back = x[1]
		lastserved = datetime.now()
		percentwront = 0.0
		tags = x[2]
		body = {"type":typez,"front":front,"back":back,"lastserved":lastserved,"percentwrong":percentwrong,"tags":tags}
		card = {idz : body}
		cards.append(card)
	f.close()
	
	if isnew:
		temp = Set(cards, None)






	
