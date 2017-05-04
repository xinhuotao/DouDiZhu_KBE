import random
from Card import Card, Suit, Rank

CONST_SUIT_BEGIN = Suit.Hei.value
CONST_SUIT_END = Suit.Fang.value + 1

CONST_RANK_BEGIN = Rank.Rank_2.value
CONST_RANK_END = Rank.Rank_A.value + 1

class CardLogic:
	def __init__(self):
		# 初始化牌下标
		self.cardIndex = []
		for x in range(0, 54):
			self.cardIndex.append(x)
		# print(self.cardIndex)
		
		# 初始化牌
		self.cards = [None] * 54
		index = 0
		for x in range(CONST_RANK_BEGIN, CONST_RANK_END) :
			for y in range(CONST_SUIT_BEGIN, CONST_SUIT_END):
				self.cards[index] = Card(index, y, x)
				index += 1
		self.cards[index] = Card(index, Suit.Hei.value, Rank.Rank_S.value)
		index += 1
		self.cards[index] = Card(index, Suit.Hong.value, Rank.Rank_B.value)
		# for x in self.cards:
		# 	x.display()

	def shuffle(self):
		random.shuffle(self.cardIndex)
		print(self.cardIndex)

m_cardLogic = CardLogic()
m_cardLogic.shuffle()