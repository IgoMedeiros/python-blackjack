# Python Blackjack

A simple command-line Blackjack game implemented in Python. This project aims to simulate a Blackjack game between a player and the dealer, with basic game mechanics such as card dealing, player decisions, and automatic dealer logic.

## Features
- Standard Blackjack game rules
- Player vs dealer gameplay
- Automatic deck shuffling and card dealing
- Hit, Stand, and Bust functionalities
- Simple text-based user interface

## Installation

### Prerequisites
To run the game, you need to have Python 3.x installed on your machine. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### Steps
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/IgoMedeiros/python-blackjack.git
   ```

2. Navigate to the project folder:
   ```bash
   cd python-blackjack
   ```

3. Run the game:
   ```bash
   python blackjack.py
   ```

## Usage

After running the game, follow the on-screen prompts to play the game. You will be given the option to hit (draw another card) or stand (keep your current hand).

### Game Rules

- **The objective**: The goal is to have a hand value as close to 21 as possible without exceeding it.
- **Card Values**:
  - Number cards (2-10) are worth their face value.
  - Face cards (Jack, Queen, King) are worth 10 points.
  - Aces can be worth either 1 or 11 points, whichever benefits the hand the most.
- **Winning**: You win by having a higher hand value than the dealer without busting (going over 21).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Blackjack Rules](https://en.wikipedia.org/wiki/Blackjack)
- Python 3.x for the programming language.
