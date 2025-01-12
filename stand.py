import game_step


def stand(player_hand, dealer_hand, playing, chips, result, deck, bet):

    if playing == False:
        if player_hand.get_value() > 0:
            result = "Sorry, you cannot stand!"

    else:
        print("You have chosen to stand.")
        playing = True
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())

        if dealer_hand.get_value() > 21:
            result = "Dealer busts! You win your bet. Press 'd' to suffle again or press 'q' to leave."
            chips += bet * 2
            playing = False
        elif dealer_hand.get_value() > player_hand.get_value():
            result = "Dealer wins! Press 'd' to suffle again or press 'q' to leave."
            chips -= bet
            playing = False
        elif dealer_hand.get_value() < player_hand.get_value():
            result = "You win! Press 'd' to suffle again or press 'q' to leave."
            chips += bet * 2
            playing = False
        else:
            result = "It's a tie! Press 'd' to suffle again or press 'q' to leave."
            playing = False
    
    game_step.game_step(player_hand, dealer_hand, playing, chips, result, deck, bet)