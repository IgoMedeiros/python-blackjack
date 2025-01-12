from player_input import player_input


def game_step(player_hand, dealer_hand, playing, chips, result, deck, bet):

    print("")
    print(f"Player hand is: {player_hand.__str__()}")
    
    print(f"Player hand total is: {str(player_hand.get_value())}")

    print("")
    print(f"Dealer hand is: {dealer_hand.__str__()}")
    print(f"Dealer hand total is: {str(dealer_hand.get_value())}")

    if playing == False:
        print(f"Chip total is: {str(chips)}")

    print(result)

    player_input(player_hand, dealer_hand, playing, chips, result, deck, bet)