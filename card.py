class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        suits = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Clubs': '\u2663',
            'Spades': '\u2660'
        }
        ranks = {
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '10': '10',
            'Jack': 'J',
            'Queen': 'Q',
            'King': 'K',
            'Ace': 'A'
        }
        return f"{ranks[self.rank]}{suits[self.suit]}"
    
    def grab_suit(self):
        return self.suit
    
    def grab_rank(self):
        return self.rank
    
    def draw(self):
        print(self.rank + self.suit)