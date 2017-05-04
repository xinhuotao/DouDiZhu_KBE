from enum import Enum

Suit = Enum("Suit", ("Hei", "Hong", "Mei", "Fang"))
Rank = Enum("Rank", ("Rank_2", "Rank_3", "Rank_4", "Rank_5", "Rank_6", "Rank_7", \
                     "Rank_8", "Rank_9", "Rank_10", "Rank_J", "Rank_Q", "Rank_K", "Rank_A", "Rank_S", "Rank_B"))

class Card:
	def __init__(self, index, suit, rank):
		self.index = index
		self.suit = suit
		self.rank = rank
		self.value = rank * 4 + suit

	def display(self):
		print("index: %d, rank: %d, suit: %d, value: %d" % (self.index, self.rank, self.suit, self.value))