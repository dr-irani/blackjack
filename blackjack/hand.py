"""
Custom class to define data structure for a Black Jack hand.
"""

import numpy as np
import constants as cn
from num_to_card_converter import convert


class Hand:
    def __init__(self, deal_size, deck, start):
        self.deal_size = deal_size
        self.deck = deck
        self.start = start
        self.hand = self.deal()
        self.sum = 0


    def __str__(self):
        return DISPLAY_HAND_MESSAGE +
            [print(convert(val) + '\n') for val in self.hand] +
            DISPLAY_HAND_SUM + self.sum


    def _calculate_sum_of_cards(self):
        [self.sum += val for val in self.hand]
        if self.sum > cn.MAX_HAND_SUM:
            self.sum = cn.BUST


    def hit(self):
        hand.add(self.deck[self.start])
        self._calculate_sum_of_cards()


    def deal(self):
        """
        TODO: fix syntax to be compliable with numpy list data structure.
        """
        hand = np.list(cn.INITIAL_DEAL_SIZE)
        [hand[card + 1] = self.deck[self.start + card] for card in 
            range(cn.INITIAL_DEAL_SIZE)]
        self._calculate_sum_of_cards()
        self.start += cn.INITIAL_DEAL_SIZE
        return hand

