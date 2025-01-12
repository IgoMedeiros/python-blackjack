from game_exit import game_exit
from hit import hit
import stand
import dealcards


def player_input(player_hand, dealer_hand, playing, chips, result, deck, bet):
    plin = input().lower()

    if plin == "h":
        hit(player_hand, dealer_hand, playing, chips, result, deck, bet)
    elif plin == "s":
        stand.stand(player_hand, dealer_hand, playing, chips, result, deck, bet)
    elif plin == "q":
        game_exit()
    elif plin == "d":
        dealcards.deal_cards()
    else:
        print("Invalid input. Please try again. Enter h, s, q or d")
        player_input(player_hand, dealer_hand, playing, chips, result, deck, bet)