class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_composition = ""

        for card in self.cards:
            hand_composition += f"{card.__str__()} "

        return f"The hand has {hand_composition}"
    
    def add_card(self, card):
        self.cards.append(card)
        self.update_value()

    def update_value(self):
        self.value = 0
        self.ace = False

        for card in self.cards:
            card_rank = card.grab_rank()

            if card_rank == 'Ace' and self.value < 11:
                self.ace = True
                self.value += 11
            elif card_rank == 'Ace' and self.value == 11:
                self.ace = True
                self.value += 10
            elif card_rank == 'Ace' and self.value > 11:
                self.ace = True
                self.value += 1
            elif card_rank.isdigit():
                self.value += int(card_rank)
            else:
                self.value += 10

    def is_busted(self):
        return self.value > 21
    
    def get_value(self):
        return self.value
    
    def draw(self, hidden, playing):
        if hidden and playing:
            starting_card = 1
        else:
            starting_card = 0
        
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()