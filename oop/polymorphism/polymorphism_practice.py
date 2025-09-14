SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        s = False
        if self.rank_index == other.rank_index:
            s = True
        r = False
        if self.suit_index == other.suit_index:
            r = True

        return s and r

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
