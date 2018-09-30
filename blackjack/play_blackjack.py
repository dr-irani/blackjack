"""
Driver program to play Black Jack.
"""

from blackjack import BlackJackSolo, BlackJackGroup
import constants as cn


def main():
    print(cn.HOW_MANY_PLAYERS_MESSAGE)
    num_players = 1
    if num_players == 1:
        game = BlackJackSolo()
        game.play_game()
    elif num_players > 1 and num_players <= 4:
        game = BlackJackGroup(num_players)
        winner = game._setup_game_group()
    else:
        print(cn.TOO_MANY_PLAYERS_ERROR)
        return
    
    # printf(cn.WINNER_MESSAGE, winner)
    print(cn.THANKS_FOR_PLAYING_MESSAGE)
        

if __name__ == "__main__":
    main()