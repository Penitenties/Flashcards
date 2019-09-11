class Set():
	def __init__(self, f, c):
		self.flashcards = f
		self.challenges = c

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

