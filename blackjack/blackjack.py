"""
Primary blackjack module.

Instructions to use:
"""

import numpy as np
import constants as cn
from hand import Hand
from num_to_card_converter import convert


class BlackJackBase(object):

    def __init__(self, num_players, deal_size=cn.INITIAL_DEAL_SIZE):
        self.num_players = num_players
        self.deal_size = deal_size



    def _shuffle_deck(self):
        deck = np.arange(cn.DECK_SIZE)
        np.random.shuffle(deck)
        return deck.tolist()


    def _reshuffle(self, cards_used):
        if (cn.DECK_SIZE - cards_used) < (self.deal_size * self.num_players):
            return True
        return False


    def _initial_deal(self, deck):
        h = Hand(self.deal_size, deck)
        return h.hand, h

    def _display_hand(self, hand):
        print(cn.DISPLAY_HAND_MESSAGE)
        [print(convert(card)) for card in hand]

    def _next_moves(self, deck, hand, hand_object):
        """
        TODO: turn into do while loop
        """
        h = hand_object
        self._display_hand(hand)
        move = input(cn.NEXT_MOVE_MESSAGE)
        while move.lower() == cn.HIT:
            h.hit()
            self._display_hand(hand)
            if h.hand_sum == cn.BUST:
                print(cn.BUST)
                break;
            self._display_hand(hand)
            move = input(cn.NEXT_MOVE_MESSAGE)
        return h.hand, h.hand_sum, h


    def play_game(self, deck):
        """
        TODO: Should this live here or in the driver?
        """
        hand, h = self._initial_deal(deck)
        hand, hand_sum, h = self._next_moves(deck, hand, h)
        choice = input(cn.ANOTHER_ROUND_MESSAGE)
        while choice.lower() == cn.YES:
            if self._reshuffle(len(deck)):
                deck = self._shuffle_deck()
            self.play_game(deck)



    def _setup_game(self):
        deck = self._shuffle_deck()
        self.play_game(deck)



class BlackJackSolo(BlackJackBase):

    def __init__(self, deal_size=cn.INITIAL_DEAL_SIZE):
        super().__init__(num_players=1, deal_size=deal_size)

    def play_game_solo(self, deck):
        hand, h = self._initial_deal(deck)
        self.play_game(deck)



class BlackJackGroup(BlackJackBase):

    def __init__(self, num_players, deal_size=cn.INITIAL_DEAL_SIZE):
        super().__init__(num_players, deal_size=deal_size)
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
            self.play_game(deck)

        
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
        self.play_game_group(deck, hands)