import readWrite


class data():
	def __init__():
		flashcards = None
		challenges = None

	def initialize(self, savefile):
		self.flashcards = readWrite.load(savefile)[0]
		self.challenges = readWrite.load(savefile)[1]

	def getf(self):
		return self.flashcards
	
	def getc(self):
		return self.challenges

	def addf(self, cards):
		if type(cards) is dict:
			self.flashcards.append(cards)
		else:
			for x in cards:
				self.flashcards.append(x)

	def addc(self, chal):
		if type(chal) is dict:
			self.challenges.append(cards)
		else:
			for x in chal:
				self.challenges.append(x)

