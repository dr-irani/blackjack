"""
Primary blackjack module.

Instructions to use:
"""

import numpy as np
import constants as cn

def shuffle_deck():
    deck = np.arange(cn.DECK_SIZE)
    np.random.shuffle(deck)
    return deck

def deal_hand(int start):

def play_game(int num_players):
    int cards_drawn_counter = 0
    hands = np.array(num_players)
    for player in num_players:
        hand = deal_hand(cards_drawn_counter)
    print(cn.ANOTHER_ROUND_MESSAGE)



def main():
    print(cn.HOW_MANY_PLAYERS_MESSAGE)
    int num_players = 1
    play_game(num_players)
    print(cn.THANKS_FOR_PLAYING_MESSAGE)
    


if __name__ == "__main__":
    main()