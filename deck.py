import random
from card import Card


class Deck:
    def __init__(self):
        self.build_deck()

    def build_deck(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
    
    def get_num_cards(self):
        return len(self.cards)
    
    def draw(self):
        deck_composition = ""
        for card in self.cards:
            deck_composition += f"{card.__str__()} "
        return deck_composition