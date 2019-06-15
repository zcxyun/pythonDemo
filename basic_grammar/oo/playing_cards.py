# 一副扑克牌 ================================================================
from collections import namedtuple
import random

Card = namedtuple('card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(x) for x in range(2,11)] + list('JQKA')
    suits = ['spades', 'hearts', 'diamonds', 'clubs']

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self._cards[key] = value

deck = FrenchDeck()
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for i in sorted(deck, key=spades_high):
    print(i)

print(random.shuffle(deck))
print(deck[:])
