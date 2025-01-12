def make_bet():
    chips = 100
    bet = 0

    print("What amount of chips you like to bet? (Enter whole integer please):")

    while bet == 0:
        bet_input = int(input(f"Enter your bet (1-chips): "))
        if bet_input >= 1 and bet_input <= chips:
            bet = bet_input
        else:
            print("Invalid bet. Please try again.")
    print(f"You have placed a bet of {bet} chips.")

    return tuple((chips, bet))
