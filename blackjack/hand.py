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
        self.sum = None

    def __str__(self):
        """
        TODO: convert this into string for method to return
        """
        hand_array = np.array(len(self.hand))
        [hand_array[pos] = val for val in self.hand]
        print(DISPLAY_HAND_MESSAGE)
        for val in hand_array[cn.FIRST_CARD:]:
            print(convert(val) + '\n')
        printf(DISPLAY_HAND_SUM, hand_array[cn.SUM])

    def hit(self):
        hand.add(self.deck[self.start])
        hand[sum]


    def deal(self):
        """
        TODO: fix syntax to be compliable with numpy list data structure.
        """
        hand = np.list(cn.INITIAL_DEAL_SIZE)
        [hand[card + 1] = self.deck[self.start + card] for card in 
            range(cn.INITIAL_DEAL_SIZE)]
        hand[0] = sum(hand[1:])
        self.start += cn.INITIAL_DEAL_SIZE
        return hand

