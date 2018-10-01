"""
Custom class to define data structure for a Black Jack hand.
"""

import constants as cn
from num_to_card_converter import convert, value


class Hand(object):
    """
    Class containing all relevant methods for a BlackJack Hand.
    """
    def __init__(self, deal_size, deck):
        """
        Constructor for Hand.
        Input: initial deal size, deck being used
        """
        self.deal_size = deal_size
        self.deck = deck
        self.hand_sum = 0
        self.hand = self.deal()


    def __str__(self):
        """
        To String method for Hand Class.
        Output: String representation of Hand Class.
        """
        return cn.DISPLAY_HAND_MESSAGE + \
            [convert(card) + '\n' for card in self.hand] + \
            cn.DISPLAY_HAND_SUM + self.hand_sum + '\n'


    def _calculate_sum_of_cards(self):
        """
        Internal method for calculating the sum of cards in a deck.
        Assigns new sum of hand to instance variable hand_sum.
        """
        self.hand_sum += value(self.hand[-1])


    def _check_choice(self, ace_val):
        """
        Internal method for checking if user input is valid for assigning
        value of ace to 1 or 11.
        Input: user input (string)
        Output: valid response (int)
        """
        if ace_val == str(cn.ACE_ONE):
            return cn.ACE_ONE
        elif ace_val == str(cn.ACE_ELEVEN):
            return cn.ACE_ELEVEN
        return self._check_choice(input(cn.INVALID_ACE_VAL))


    def handle_ace(self):
        """
        Internal method for handling case an ace is drawn. Prompt user to
        select a value for ace, either 1 or 11. By default, the system values
        an ace as 11, so if the user specifies 1, then 10 is subtracted from
        the hand sum.
        """
        if value(self.hand[-1]) == cn.ACE_ELEVEN:
            ace_val = input(cn.VALUE_OF_ACE)
            ace_val = self._check_choice(ace_val)
            if ace_val == cn.ACE_ONE:
                self.hand_sum -= cn.TEN_NUM


    def hit(self):
        """
        Public-facing hit method. Pops card from deck and adds it to hand.
        """
        self.hand.append(self.deck.pop())
        self._calculate_sum_of_cards()


    def deal(self):
        """
        Public-facing deal method. Pops initial two cards from deck and adds
        them to hand. Calculates initial sum of cards in hand.
        Output: hand
        """
        self.hand = []
        [self.hand.append(self.deck.pop()) for card in
         range(cn.INITIAL_DEAL_SIZE)]
        for val in self.hand:
            self.hand_sum += value(val)
        return self.hand
