"""
Driver program to play Black Jack.
"""

from blackjack import BlackJack


def main():
    print(cn.HOW_MANY_PLAYERS_MESSAGE)
    int num_players = 1
    winner = play_game(num_players)
    printf(cn.WINNER_MESSAGE, winner)
    print(cn.THANKS_FOR_PLAYING_MESSAGE)
        

if __name__ == "__main__":
    main()