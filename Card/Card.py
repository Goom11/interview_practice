#!/usr/bin/python

clubs = 0
spades = 1
hearts = 2
diamonds = 3


class Card:
    def __init__(self, r, s):
        self.m_card = r
        self.m_suit = s

    def value(self):
        return self.m_card

    def suit(self):
        return self.m_suit


class BlackJackCard(Card):
    def value(self):
        if self.m_card == 1:
            return 11
        elif self.m_card < 10:
            return self.m_card
        else:
            return 10

c = Card(5, clubs)
print "c is the", c.value(), "of", c.suit()
j = BlackJackCard(12, hearts)
print "j is the", j.value(), "of", j.suit()
k = BlackJackCard(1, hearts)
print "k is the", k.value(), "of", k.suit()
