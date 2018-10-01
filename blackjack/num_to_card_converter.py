"""
This utility converts a number and outputs what card it is.
"""

import constants as cn

def convert(card_number):
    """
    Method that determines value and suit of card based on modular arithmetic.
    Input: card_number (int)
    Output: representation of card in CARD of SUIT format (String)
    """
    card_type = {cn.TWO_NUM: cn.TWO,
                 cn.THREE_NUM: cn.THREE,
                 cn.FOUR_NUM: cn.FOUR,
                 cn.FIVE_NUM: cn.FIVE,
                 cn.SIX_NUM: cn.SIX,
                 cn.SEVEN_NUM: cn.SEVEN,
                 cn.EIGHT_NUM: cn.EIGHT,
                 cn.NINE_NUM: cn.NINE,
                 cn.TEN_NUM: cn.TEN,
                 cn.JACK_NUM: cn.JACK,
                 cn.QUEEN_NUM: cn.QUEEN,
                 cn.KING_NUM: cn.KING,
                 cn.ACE_ONE: cn.ACE}[card_number % cn.NUM_TYPES]

    suit = {cn.CLUBS_NUM: cn.CLUBS,
            cn.SPADES_NUM: cn.SPADES,
            cn.DIAMONDS_NUM: cn.DIAMONDS,
            cn.HEARTS_NUM: cn.HEARTS}[card_number % cn.NUM_SUITS]

    return "{0} of {1}".format(card_type, suit)


def value(card_number):
    """
    Method for calculating integer value of a card.
    Input: card_number (int)
    Output: value (int)
    """
    val = card_number % cn.NUM_TYPES
    if val > cn.FACE_CARD_VALUE or val == cn.KING_NUM:
        return cn.FACE_CARD_VALUE
    elif val == cn.ACE_ONE:
        return cn.ACE_ELEVEN
    return val
