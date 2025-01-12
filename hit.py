import game_step

def hit(player_hand, dealer_hand, playing, chips, result, deck, bet):
    """
    Function to handle a hit from the player.
    """
    # Check if the player is playing and has not busted yet.
    # If so, add a card to the player's hand and update the total value.
    # If the player busts, end the game.

    if playing:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())

        if player_hand.get_value() > 21:
            print("Bust! You lose your bet.")
            result = "Press 'd' to suffle again or press 'q' to leave."
            chips -= bet
            playing = False
    else:
        result = "You are not playing. Cannot hit. Press 'd' to suffle again or press 'q' to leave."

    game_step.game_step(player_hand, dealer_hand, playing, chips, result, deck, bet)