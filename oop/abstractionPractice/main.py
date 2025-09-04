import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        pass

    def create_deck(self):
        pass

    def shuffle_deck(self):
        pass

    def deal_card(self):
        pass

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
