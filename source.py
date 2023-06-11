import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_values = {
    "A": 5,
    "B": 4,
    "C": 3,~
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
    
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        all_symbols.extend([symbol] * symbols_count)
    columns = []
    for _ in range(cols):
        column = random.choices(all_symbols, k=rows)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1 - {MAX_LINES}): ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines
    
def get_bet():
    while True:
        amount = input(f'What would you like to bet on each line? (${MIN_BET} - ${MAX_BET}): ')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def game(balance):
    lines = number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance or total_bet <= 0:
            print(f"You don't have enough money to bet ${bet} on {lines} lines. It exceeds your balance.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_values)
    print(f"You won ${winnings}")
    print("You won on lines:", *winning_lines)
    
    return winnings - total_bet

def main():
    balance = deposit()
    
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press Enter to play (X to exit): ")
        if answer.lower() == "x":
            break
        balance += game(balance)
    
    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
