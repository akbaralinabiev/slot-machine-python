MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def desposit():
    while True:
        lines =input('What would you like to deposit? $')
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                break
            else:
                print("lines must be greater than 0.")
        else:
            print("Please enter a number.")
    return lines


def number_of_lines():
    while True:
        lines =input('Enter the number of lines to bet on (1- ' + str(MAX_LINES) + ")? ")
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
        amount =input('What would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} -$ {MAX_BET}")
        else:
            print("Please enter a number.")
    return amount
    
def main():
    balance = desposit()
    lines = number_of_lines()
   
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print("You don't have enough money to bet ${} on {} lines".format(bet, lines), "It's exceeding your balance.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


main()