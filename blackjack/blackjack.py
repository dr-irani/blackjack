"""
Primary blackjack module.

Instructions to use:
"""

import numpy as np
import constants as cn
from hand import Hand


class BlackJackBase(object):

    def __init__(self, num_players, deal_size=INITIAL_DEAL_SIZE)
        self.num_players = num_players
        self.deal_size = deal_size
        self.start = 0


    def _shuffle_deck(self):
        deck = np.arange(cn.DECK_SIZE)
        np.random.shuffle(deck)
        return deck


    def _reshuffle(self, cards_used):
        if (cn.DECK_SIZE - cards_used) < (self.deal_size * self.num_players):
            return True
        return False


    def _initial_deal(self, deck):
        h = Hand(self.deal_size, deck, self.start)
        self.start = h.start
        return h.hand, h


    def _next_moves(self, deck, hand, hand_object):
        """
        TODO: turn into do while loop
        """
        h = hand_object
        print(hand, NEXT_MOVE_MESSAGE)
        # scan for input
        move = cn.HIT
        while move == cn.HIT:
            h.hit()
            if h.hand_sum == cn.BUST:
                break;
            print(hand, NEXT_MOVE_MESSAGE)
            # scan for input
        return h.hand, h.hand_sum, h


    def play_game(self, deck):
        """
        TODO: Should this live here or in the driver?
        """
        hand, hand_sum, h = _next_moves(self.start, deck, hand, h)
        print(cn.ANOTHER_ROUND_MESSAGE)
        # scan for input
        while choice:
            if self._reshuffle(self.start):
                deck = self._shuffle_deck()
            play_game(deck)



    def _setup_game(self):
        deck = _shuffle_deck()
        self.play_game(cn.start, deck)



class BlackJackSolo(BlackJackBase):

    def __init__(self, num_players, deal_size=INITIAL_DEAL_SIZE):
        pass

    def play_game_solo(self, deck):
        hand, h = self._initial_deal(deck)
        self.play_game(deck)



class BlackJackGroup(BlackJackBase):

    def __init__(self, num_players, deal_size=INITIAL_DEAL_SIZE)
        self.winner = None
        self.num_wins = 0


    def _initial_deal_group(self, start, deck, hands):
        for player in self.num_players:
            printf(ONE_PLAYER_LOOK_MESSAGE, player)
            print(CONTINUE_MESSAGE)
            # when Y pressed, continue

            self._initial_deal(start, deck, hands)
            print(CONTINUE_MESSAGE)
            # command clear
        return hands


    def play_game_group(self, deck, hands):
        for player in self.num_players:
            hands[player], hs[player] = self._initial_deal_group(deck, hands[player])
        hit_or_pass(self.start, deck, hands)
        print(cn.ANOTHER_ROUND_MESSAGE)
        choice = True
        if choice:
            if reshuffle():
                deck = shuffle_deck(cards_drawn_counter, num_players)
            play_game(num_players, cards_drawn_counter, deck, hands)
        return #index position for max value in number of wins


    def _setup_game_group(self):
        self._setup_game()
        hands = np.array(self.num_players)
        self.play_game(deck, hands)