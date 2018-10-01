"""
This is a test file for hand.py
"""


import unittest
import numpy as np
import constants as cn
from hand import Hand
from num_to_card_converter import convert, value


class HandTest(unittest.TestCase):
    def setUp(self):
        deck = np.arange(cn.DECK_SIZE).tolist()
        self.hand = Hand(cn.INITIAL_DEAL_SIZE, deck)


    def test_deal(self):
        self.hand.hand_sum = 0
        self.hand.deal()
        hand = self.hand.hand
        self.assertEqual(10, value(hand[0]))
        self.assertEqual(9, value(hand[1]))
        self.assertEqual(19, self.hand.hand_sum)



    def test_hit(self):
        self.hand.hand_sum = 0
        self.hand.deal()
        self.hand.hit()
        hand = self.hand.hand
        self.assertEqual(8, value(hand[2]))
        self.assertEqual(27, self.hand.hand_sum)


suite = unittest.TestLoader().loadTestsFromTestCase(HandTest)
_ = unittest.TextTestRunner().run(suite)