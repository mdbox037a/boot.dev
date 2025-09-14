SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        rank_eq = False
        if self.rank_index == other.rank_index:
            rank_eq = True
        suit_eq = False
        if self.suit_index == other.suit_index:
            suit_eq = True

        return suit_eq and rank_eq

    def __lt__(self, other):
        comparison = self.rank_index - other.rank_index
        if comparison == 0:
            comparison = self.suit_index - other.suit_index
            return comparison < 0
        elif comparison < 0:
            return True
        else:
            return False

    def __gt__(self, other):
        comparison = self.rank_index - other.rank_index
        if comparison == 0:
            comparison = self.suit_index - other.suit_index
            return comparison > 0
        elif comparison > 0:
            return True
        else:
            return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
