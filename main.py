# Ahthesham Ali Syed

import random  # Import the random library for generating random numbers

# Define constants that will not change throughout the game
MAX_LINES = 3  # The maximum number of lines a user can bet on
MAX_BET = 100  # The maximum amount of money a user can bet
MIN_BET = 1  # The minimum amount of money a user can bet

# The number of rows and columns on the slot machine
ROWS = 3
COLS = 3

# Define a dictionary that holds the count of each symbol that can appear on the slot machine
symbol_count = {
    "A": 2,  # Symbol 'A' will appear twice
    "B": 4,  # Symbol 'B' will appear four times
    "C": 6,  # Symbol 'C' will appear six times
    "D": 8  # Symbol 'D' will appear eight times
}

# Define a dictionary that holds the value of each symbol when it appears on a line
symbol_value = {
    "A": 5,  # Symbol 'A' has a value of 5
    "B": 4,  # Symbol 'B' has a value of 4
    "C": 3,  # Symbol 'C' has a value of 3
    "D": 2  # Symbol 'D' has a value of 2
}


# Function to check the winnings based on the symbols aligned on each line
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Initialize winnings to zero
    winning_lines = []  # List to keep track of winning lines
    # Loop over the number of lines the player has bet on
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol on the current line of the first column
        # Check if this symbol is consistent across all columns
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  # If not, break and check the next line
        else:
            # If the symbol is consistent across all columns, the user wins on this line
            winnings += values[symbol] * bet  # Add the winnings from this line to the total winnings
            winning_lines.append(line + 1)  # Add the line number to the winning lines list

    return winnings, winning_lines  # Return the total winnings and the winning lines


# Function to generate a random spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # List to store all possible symbols based on their count
    # Populate the all_symbols list with symbols according to their count
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)  # Add the symbol to the list symbol_count times

    columns = []  # List to store the result of the spin (a list of columns)
    # Generate each column for the spin
    for _ in range(cols):
        column = []  # List to represent a single column
        current_symbols = all_symbols[:]  # Create a copy of all_symbols to manipulate
        # Randomly select a symbol for each row in the column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # Remove the chosen symbol from current_symbols
            column.append(value)  # Add the chosen symbol to the column

        columns.append(column)  # Add the completed column to the columns list

    return columns  # Return the result of the spin as a list of columns


# Function to print the slot machine's columns and rows after a spin
def print_slot_machine(columns):
    # Loop through each row index
    for row in range(len(columns[0])):
        # Loop through each column in the slot machine
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print the symbol with a separator if it's not the last column
            else:
                print(column[row], end="")  # Print the symbol without a separator if it is the last column

        print()  # Print a newline at the end of each row


# Function for a user to deposit money into their slot machine balance
def deposit():
    while True:  # Loop until a valid deposit is made
        amount = input("What would you like to deposit ? $")
        # Check if the input is a number
        if amount.isdigit():
            amount = int(amount)  # Convert the input to an integer
            if amount > 0:
                break  # Exit the loop if the amount is greater than zero
            else:
                print("Amount must be greater than 0.")  # Error message for non-positive amounts
        else:
            print("Please enter a number.")  # Error message for non-numeric inputs

    return amount  # Return the valid deposit amount


# Function to get the number of lines the user wants to bet on
def get_number_of_lines():
    while True:  # Loop until a valid number of lines is entered
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # Check if the input is a number
        if lines.isdigit():
            lines = int(lines)  # Convert the input to an integer
            # Check if the number of lines is within the allowed range
            if 1 <= lines <= MAX_LINES:
                break  # Exit the loop if the number of lines is valid
            else:
                print("Enter a valid number of lines.")  # Error message for invalid number of lines
        else:
            print("Please enter a number.")  # Error message for non-numeric inputs

    return lines  # Return the valid number of lines


# Function to get the bet amount per line from the user
def get_bet():
    while True:  # Loop until a valid bet amount is entered
        amount = input("What would you like to bet on each line? $")
        # Check if the input is a number
        if amount.isdigit():
            amount = int(amount)  # Convert the input to an integer
            # Check if the bet amount is within the allowed range
            if MIN_BET <= amount <= MAX_BET:
                break  # Exit the loop if the bet amount is valid
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")  # Error message for invalid bet amount
        else:
            print("Please enter a number.")  # Error message for non-numeric inputs

    return amount  # Return the valid bet amount


# Function to handle the user's spin on the slot machine
def spin(balance):
    lines = get_number_of_lines()  # Get the number of lines to bet on
    while True:  # Loop until a valid total bet amount is entered
        bet = get_bet()  # Get the bet amount per line
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


# The main function where the game starts.
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


# Call the main function to run the game.
main()
