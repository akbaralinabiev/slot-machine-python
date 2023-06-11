# Slot Machine Game

This is a simple text-based slot machine game implemented in Python. The game allows the player to deposit a certain amount of money and place bets on multiple lines. The slot machine will generate random symbols, and the player can win based on the matching symbols on the lines they bet on.

## How to Play

1. Run the Python script `source.py`.
2. Enter the amount you want to deposit.
3. Enter the number of lines you want to bet on (between 1 and 3).
4. Enter the bet amount for each line (between $1 and $ ... ).
5. The slot machine will generate random symbols for each line.
6. If you win, your winnings will be displayed along with the winning lines.
7. You can choose to continue playing or exit the game.
8. The game will keep track of your balance and display it after each round.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the `source.py` file.
2. Make sure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory containing the `slot_machine.py` file.
4. Run the script using the command: `python source.py`.

## Customization

- You can modify the `MAX_LINES`, `MAX_BET`, and `MIN_BET` constants to change the game rules.
- The `symbols_count` dictionary defines the symbols and their occurrence count on the slot machine.
- The `symbols_values` dictionary defines the symbols and their corresponding values for calculating winnings.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and enhance the game according to your needs. Contributions and suggestions are welcome.

Enjoy the game!
