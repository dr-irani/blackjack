"""
This is a test file for blackjack.py
"""

import unittest
import numpy as np
import constants as cn
from blackjack import BlackJackBase, BlackJackSolo
from num_to_card_converter import convert, value

class BlackJackBaseTest(unittest.TestCase):
    def setUp(self):
        self.game = BlackJackBase(1)


    def test_shuffle_deck(self):
        self.assertEqual(cn.DECK_SIZE, len(self.game.shuffle_deck()))


    def test_initial_deal(self):
        deck = np.arange(cn.DECK_SIZE).tolist()
        hand, h = self.game._initial_deal(deck)
        self.assertEqual(2, len(hand))
        self.assertEqual(10, value(hand[0]))
        self.assertEqual(10, value(hand[1]))


    def test_check_choice(self):
        choice = 'YES'
        self.assertEqual(cn.YES, self.game._check_choice(choice))
        choice = 'NO'
        self.assertEqual(cn.NO, self.game._check_choice(choice))


    def test_check_move(self):
        move = 'H'
        self.assertEqual(cn.HIT, self.game._check_move(move))
        move = 'p'
        self.assertEqual(cn.PASS, self.game._check_move(move))


    def test_handle_bust_ace_first_card(self):
        deck = np.arange(41).tolist()
        hand, h = self.game._initial_deal(deck)
        h.hit()
        self.assertEqual(cn.ACE_ELEVEN, value(hand[0]))
        self.assertEqual(31, h.hand_sum)
        hand_sum = self.game._handle_bust_ace_first_card(h.hand, h.hand_sum)
        self.assertEqual(21, hand_sum)


    def test_game_result(self):
        # print BlackJack!
        deck = np.arange(41).tolist()
        hand, h = self.game._initial_deal(deck)
        h.hit()
        hand_sum = self.game._handle_bust_ace_first_card(hand, h.hand_sum)
        self.assertEqual(cn.BLACKJACK_NUM, hand_sum)
        # print bust!
        deck = np.arange(41).tolist()
        hand, h = self.game._initial_deal(deck)
        h.hit()
        h.hit()
        hand_sum = self.game._handle_bust_ace_first_card(hand, h.hand_sum)
        self.assertTrue(hand_sum > cn.BLACKJACK_NUM)
        # print sum
        deck = np.arange(43).tolist()
        hand, h = self.game._initial_deal(deck)
        hand_sum = self.game._handle_bust_ace_first_card(hand, h.hand_sum)
        self.assertEqual(5, hand_sum)



suite = unittest.TestLoader().loadTestsFromTestCase(BlackJackBaseTest)
_ = unittest.TextTestRunner().run(suite)