from deck import Deck
from intro import intro
from dealcards import deal_cards

intro()

deck = Deck()
deck.shuffle()
deal_cards()

# print(deck.draw())

# print(deck.get_num_cards())

# player_hand = Hand()
# dealer_hand = Hand()

# player_hand.add_card(deck.deal_card())
# player_hand.add_card(deck.deal_card())

# dealer_hand.add_card(deck.deal_card())
# dealer_hand.add_card(deck.deal_card())

# print(deck.get_num_cards())

# print(player_hand.__str__())
# print(dealer_hand.__str__())
# print(deck.draw())