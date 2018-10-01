"""
Primary blackjack game class. An instance of the game can be instantiated
in the provided driver function: play_blackjack.py.
"""

import numpy as np
import constants as cn
from hand import Hand
from num_to_card_converter import convert, value


class BlackJackBase(object):
    """
    Base BlackJack class
    """
    def __init__(self, num_players, deal_size=cn.INITIAL_DEAL_SIZE):
        """
        Constructor for BlackJackBase class.
        Input: number of players playing, how many cards are initially dealt.
        """
        self.num_players = num_players
        self.deal_size = deal_size


    def shuffle_deck(self):
        """
        Function that handles instatitation of new deck and shuffling deck.
        Output: deck as a list
        """
        deck = np.arange(cn.DECK_SIZE)
        np.random.shuffle(deck)
        return deck.tolist()


    def _initial_deal(self, deck):
        """
        Internal function for dealing the initial hand.
        Input: deck (list)
        Output: current hand and hand object
        """
        h = Hand(self.deal_size, deck)
        return h.hand, h


    def _display_hand(self, hand):
        """
        Internal function for printing all of the cards in a hand, after a user's
        turn is over.
        Input: hand
        Output: contents of hand to stdout
        """
        print(cn.DISPLAY_HAND_MESSAGE)
        [print(convert(card)) for card in hand]


    def _check_choice(self, choice):
        """
        Internal method for checking if user input is valid for message about
        playing another round.
        Input: user input (string)
        Output: valid response (string)
        """
        choice = choice.lower()
        if choice == cn.NO or choice == cn.NO_SPELLED_OUT:
            return cn.NO
        elif choice == cn.YES or choice == cn.YES_SPELLED_OUT:
            return cn.YES
        return self._check_choice(input(cn.INVALID_CHOICE))


    def _check_move(self, move):
        """
        Internal method for checking if user input is valid for message about
        whether to hit or pass.
        Input: user input (string)
        Output: valid response (string)
        """
        move = move.lower()
        if move == cn.HIT or move == cn.HIT_SPELLED_OUT:
            return cn.HIT
        elif move == cn.PASS or move == cn.PASS_SPELLED_OUT:
            return cn.PASS
        return self._check_move(input(cn.INVALID_MOVE))



    def _next_moves(self, hand, hand_object):
        """
        Internal method that handles user input about hitting or passing.
        Input: hand, hand object
        Output: final hand, hand object
        """
        h = hand_object
        print(cn.DISPLAY_SECOND_CARD, convert(hand[1]))
        h.handle_ace()
        move = input(cn.NEXT_MOVE_MESSAGE)
        move = self._check_move(move)
        while move == cn.HIT:
            h.hit()
            print(convert(hand[-1]))
            h.handle_ace()
            move = input(cn.NEXT_MOVE_MESSAGE)
        return h.hand, h


    def _handle_bust_ace_first_card(self, hand, hand_sum):
        """
        Internal method that handles case that first card is a hidden ace,
        which is what caused a bust. By default, the system values ace as 11,
        but if changing this to 1 prevents a bust, it does so.
        Input: hand, hand sum
        Output: hand sum
        """
        if value(hand[0]) == cn.ACE_ELEVEN:
            hand_sum -= cn.TEN_NUM
        return hand_sum


    def _game_result(self, hand, hand_object):
        """
        Internal method for displaying final result of game.
        Input: hand, hand object
        Output: status (BlackJack, Bust, or sum of cards) to stdout
        """
        h = hand_object
        hand_sum = h.hand_sum
        if hand_sum > cn.BLACKJACK_NUM:
            hand_sum = self._handle_bust_ace_first_card(hand, hand_sum)
        if hand_sum == cn.BLACKJACK_NUM:
            print(cn.BLACKJACK)
            self._display_hand(hand)
        elif hand_sum > cn.BLACKJACK_NUM:
            print(cn.BUST)
            self._display_hand(hand)
        else:
            self._display_hand(hand)
            print(cn.DISPLAY_HAND_SUM, hand_sum, "\n")


    def _game(self, deck):
        """
        Internal method for managing game. Calls all gameplay methods like
        initial deal, next moves, and handles input of whether user wants to
        play anther game.
        """
        hand, h = self._initial_deal(deck)
        hand, h = self._next_moves(hand, h)
        self._game_result(hand, h)
        choice = input(cn.ANOTHER_ROUND_MESSAGE)
        choice = self._check_choice(choice)
        if choice == cn.YES:
            deck = self.shuffle_deck()
            self._game(deck)


    def play_game(self):
        """
        Public-facing method that user calls in BlackJack instantiation that
        obtains a new shuffled deck and begins game.
        """
        deck = self.shuffle_deck()
        self._game(deck)



class BlackJackSolo(BlackJackBase):
    """
    Child class of BlackJack for a single player game.
    """
    def __init__(self, deal_size=cn.INITIAL_DEAL_SIZE):
        """
        Constructor for BlackJackSolo which calls super constructor, with
        number of players set to 1.
        """
        super().__init__(num_players=1, deal_size=deal_size)
