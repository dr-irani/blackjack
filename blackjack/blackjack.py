"""
Primary blackjack module.

Instructions to use:
"""

import numpy as np
import constants as cn


class BlackJack():

    def __init__(self, num_players)
        self.num_players
        self.winner = None
        self.num_wins = 0

    def _shuffle_deck(self):
        deck = np.arange(cn.DECK_SIZE)
        np.random.shuffle(deck)
        return deck

    def _reshuffle(self, cards_used):
        if (cn.DECK_SIZE - cards_used) < (cn.INITIAL_DEAL_SIZE * self.num_players):
            return True
        return False

    # def deal_hand(self, start, deck):
    #     hand = np.list(cn.INITIAL_DEAL_SIZE)
    #     [hand[card + 1] = deck[start + card] for card in range(cn.INITIAL_DEAL_SIZE)]
    #     hand[0] = sum(hand[1:])
    #     return hand

    def initial_deal(num_players, start, deck, hands):
        for player in num_players:
            if num_players > 0:
                printf(ONE_PLAYER_LOOK_MESSAGE, player)
                print(CONTINUE_MESSAGE)
                # when Y pressed, continue
            hand = deal_hand(cards_drawn_counter, deck)
            cards_drawn_counter += cn.INITIAL_DEAL_SIZE
            printf(DISPLAY_HAND_MESSAGE, hand[cn.FIRST_CARD], hand[cn.SECOND_CARD],
                hand[cn.THIRD_CARD], hand[cn.SUM])
            if num_players > 0:
                print(CONTINUE_MESSAGE)
                # command clear
        return hands

    def hit_or_pass(start, deck, hands):
        if 


    def play_game(num_players, start, deck, hands):
        hands = initial_deal(num_players, start, deck, hands)
        for player in num_players:
        hit_or_pass(start, deck, hands)
        print(cn.ANOTHER_ROUND_MESSAGE)
        choice = True
        if choice:
            if reshuffle():
                deck = shuffle_deck(cards_drawn_counter, num_players)
            play_game(num_players, cards_drawn_counter, deck, hands)
        return #index position for max value in number of wins

    def setup_game(num_players):
        int cards_drawn_counter = 0
        hands = np.array(num_players)
        deck = shuffle_deck()
        play_game(num_players, cards_drawn_counter, deck, hands)

