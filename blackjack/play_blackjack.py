"""
Driver program to play Black Jack.
"""

from blackjack import BlackJackSolo
import constants as cn


def main():
    """
    Main method instatiates instance of single player BlackJackSolo game.
    """
    game = BlackJackSolo()
    game.play_game()
    print(cn.THANKS_FOR_PLAYING_MESSAGE)


if __name__ == "__main__":
    main()
