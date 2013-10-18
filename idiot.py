import random

'''
TODO:
Split classes into modules
'''

class Deck:

	cards = []

	def __init__(self):
		# build Deck
		'''
		11 = Jack
		12 = Queen
		13 = King
		14 = Ace
		'''
		for value in range(2, 15):
			'''
			1 = Spades
			2 = Clubs
			3 = Diamonds
			4 = Hearts
			'''
			suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
			for suit in suits:
				card = Card(value, suit)
				self.cards.append(card)

	def shuffle(self):
		random.seed()
		random.shuffle(self.cards)



	def deal(self, player):
		self.shuffle()
		for card in range(6):
			player.hand.append(self.cards.pop())




	def __str__(self):
		string = ""
		for card in self.cards:
			string += "%s of %s\n" % (card.value, card.suit)
		return string



class Card:

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit



class Pile:

	pile = []

	def __init__(self):
		pass

	def __str__(self):
		string = ""
		
		for card in self.pile:
			string += "%s of %s\n" % (card.value, card.suit)
		return string


class Player:

	hand = []

	def __init__(self):
		pass

	''' TODO: 
	Show player's hand at every turn
	then they can decide whether to play or pickup
	'''
	# If they would like to attack or defend
	def play(self):
		i = int( raw_input("Play: ") )
		if (i > 0 and i <= len(self.hand)):
			played = self.hand[i-1]	# allow for natural number indexing
			print "Played %s of %s" % (played.value, played.suit)
		else:
			print "Play a valid card or pick up"
			self.play()

	# If they would like to pick up
	def pick_up(self, pile):
		print "You picked up: "
		print pile



	def __str__(self):
		string = ""
		for card in self.hand:
			string += "%s of %s\n" % (card.value, card.suit)
		return string




def main():

	'''
	TODO:
	Don't let player pick up when there are no cards in pile
	'''
	def prompt():
		while True:
			prompt = raw_input("> ")
			if (prompt in ("p", "P", "play", "Play")):
				p1.play()
				break
			elif (prompt in ("pu", "PU", "pick up", "Pick Up")):
				p1.pick_up(pile)
				break
			else:
				print "Press 'p' to play a card"
				print "Press 'pu' to pick up the pile"

	deck = Deck()
	p1 = Player()
	pile = Pile()

	deck.shuffle()
	print(deck)
	deck.deal(p1)
	
	while 1:
		prompt()

if __name__ == "__main__":
	main()
