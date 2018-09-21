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
    hand = [np.list.insert(shuffle_deck[start + card]) for card in range(cn.INITIAL_DEAL_SIZE)]
    return np.list

def play_game(int start):
    for player in num_players:
        hand = deal_hand(cards_drawn_counter)
        cards_drawn_counter += cn.INITIAL_DEAL_SIZE
    print(cn.ANOTHER_ROUND_MESSAGE)
    choice = True
    if choice:
        play_game(cards_drawn_counter)

def setup_game(num_players):
    int cards_drawn_counter = 0
    hands = np.array(num_players)
    play_game(cards_drawn_counter)


def main():
    print(cn.HOW_MANY_PLAYERS_MESSAGE)
    int num_players = 1
    play_game(num_players)
    print(cn.THANKS_FOR_PLAYING_MESSAGE)
    


if __name__ == "__main__":
    main()