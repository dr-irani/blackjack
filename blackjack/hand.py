"""
Custom class to define data structure for a Black Jack hand.
"""

import numpy as np
import constants as cn
from num_to_card_converter import convert, value


class Hand(object):
    def __init__(self, deal_size, deck):
        self.deal_size = deal_size
        self.deck = deck
        self.hand_sum = 0
        self.hand = self.deal()


    def __str__(self):
        return cn.DISPLAY_HAND_MESSAGE + \
            [convert(val) + '\n' for val in self.hand] + \
            cn.DISPLAY_HAND_SUM + self.hand_sum + '\n'


    def _calculate_sum_of_cards(self):
        """
        TODO: handle case that ace can be 1 or 11.
        """
        self.hand_sum = 0
        for val in self.hand:
            self.hand_sum += value(val)
        print(self.hand_sum)
        if self.hand_sum > cn.MAX_HAND_SUM:
            self.hand_sum = cn.BUST


    def hit(self):
        self.hand.append(self.deck.pop())
        self._calculate_sum_of_cards()


    def deal(self):
        """
        TODO: fix syntax to be compliable with numpy list data structure.
        """
        self.hand = []
        [self.hand.append(self.deck.pop()) for card in 
            range(cn.INITIAL_DEAL_SIZE)]
        self._calculate_sum_of_cards()
        return self.hand

