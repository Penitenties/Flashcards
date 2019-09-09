import json
import Set
import sys
from datetime import datetime

#add enter !quit to quit at any point

#takes in the cards object and returns a card dict
def makeCard(cardset):
	flashcards = cardset.getf()
	#get data from user
	idz = flashcards[-1]+1
	typez = "flashcard"
	front = input("Enter the text for the front of the card")
	back = input("Enter the text for the back of the card")
	lastserved = datetime.now()
	percentwrong = 0.0
	tags = input("Enter any tags you want asociated with this card")
	#input verification
	scrap = "hi"
	while scrap.lower() != "y" and (scrap.lower() != "n":
		scrap = input("Add this card to the card set? (y/n)")
	if scrap.lower() == "n":
		return None
	#build card
	body = {"type":typez,"front":front,"back",back,"lastserved":lastserved,"percentwrong":percentwrong,"tags":tagsd	}
	card = {idz : body}
	return card

#takes a card set object and returns an cardset object with the added cards
def addCards(cardset):
	goOn = "hi"
	while goOn.lower() != "y" and (goOn.lower() != "n":
		toAdd = makeCard(cardset)
		if toAdd is not None:
			cardset.addf(toAdd)
		goOn = input("Make another card? (y/n)")
	return cardset
