from deck import Deck
import game_step
from hand import Hand
from makebet import make_bet

def deal_cards():

    deck = Deck()
    deck.shuffle()

    chips, bet = make_bet()
    player_hand = Hand()
    dealer_hand = Hand()
    
    # Deal initial 2 cards to the player and dealer
    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    result = "Hit or Stand? Press 'h' or 's':"
    
    chips -= bet

    playing = True

    game_step.game_step(player_hand, dealer_hand, playing, chips, result, deck, bet)

    return (player_hand, dealer_hand)