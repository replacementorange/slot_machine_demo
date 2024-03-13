import random

# Console - Slot machine - Demo

# Const values
MAX_LINES = 3   # Lines
MAX_BET = 100   # Bet's maximum amount
MIN_BET = 1     # Bet's minimal amount

ROWS = 3        # Rows in slot machine
COLS = 3        # Columns in slot machine


# Dictionary for symbols and their appearence count
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


# Dictionary for symbol's value
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# Logic for winning
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):                           # Line check
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


# Emulate slot machine's one spin
def get_slot_machine_spin(row, cols, symbols):
    # Creates list of all possible symbols
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):                           # Creates list of colums
        column = []
        current_symbols = all_symbols[:]            # Copy of all_symbols list
        for _ in range(row):
            value = random.choice(current_symbols)  # Picks random value from list
            current_symbols.remove(value)           # Removes value from symbols
            column.append(value)                    # Adds value to column
        
        columns.append(column)                      # Adds column to columns

    return columns


# Print slot machine's output to the player
def print_slot_machine(columns):
    # Transposing (rows -> columns)
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()                                     # Moves to new line


# Collect user deposit input
def deposit():
    while True:
        amount = input("What would you like to deposit? (€) ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please, enter a number.")
        
    return amount


# Get amount of lines to bet on from user input
def get_numbers_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please, enter a number.")
        
    return lines


# Get bet amount from user input
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? (€) ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between €{MIN_BET} - €{MAX_BET}")
        else:
            print("Please, enter a number.")
        
    return amount


# Spin loop logic
def spin(balance):
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is {balance}€")
        else:
            break

    print(f"You are betting {bet}€ on {lines} lines. Total bet is equal to: {total_bet}€")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}€.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


# Game loop logic
def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}€")
        anwser = input("Press enter to play (q to quit). ")
        if anwser == "q":
            break
        else:
            balance += spin(balance)
            if balance == 0: # Ends game if balance is 0
                break

    print(f"You left with {balance}€")


main()