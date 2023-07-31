import emoji # Import emoji module to allow the use of emojis
import random # Import random module to allow generating random numbers

MAX_NUM_OF_LINES = 3
MAX_BET = 500
MIN_BET = 100

ROWS = 3 
COLS = 3 

symbol_count = {
    "A": 2, 
    "B": 4,
    "C": 6, 
    "D": 8 
}

def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate slot machine spins and return a 2D list representing the result.

    The method generates random spins for a slot machine with the given number of rows and columns.
    The symbols to be used in the slot machine are defined in the 'symbols' dictionary, where the keys represent symbols,
    and the values represent the count of each symbol in the slot machine.

    Args:
        rows (int): The number of rows in the slot machine.
        cols (int): The number of columns in the slot machine.
        symbols (dict): A dictionary containing the symbols and their respective counts in the slot machine.
                        Example: {'A': 2, 'B': 4, 'C': 6, 'D': 8}

    Returns:
        list: A 2D list representing the slot machine spins, where each inner list represents a column,
              and each element in the column list represents a symbol from the 'symbols' dictionary.

    Example:
        get_slot_machine_spin(3, 3, {'A': 2, 'B': 4, 'C': 6, 'D': 8})
        Output: [['B', 'C', 'D'], ['C', 'D', 'D'], ['B', 'B', 'C']]
    """

    all_symbols = []
    
    # Generate a list of all symbols based on their counts in the 'symbols' dictionary
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # Choose a random symbol from the available symbols and remove it from the list to avoid duplicates
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    """
    Print the slot machine spins in a user-friendly format.

    The method takes a 2D list representing the slot machine spins, where each inner list represents a column,
    and each element in the column list corresponds to a symbol from the slot machine spins.

    The function prints the spins in a user-friendly format, displaying each column as vertical symbols in the slot machine.

    Args:
        columns (list): A 2D list containing the slot machine spins. Each inner list represents a column in the slot machine.
                        Example: [['B', 'C', 'D'], ['C', 'D', 'D'], ['B', 'B', 'C']]

    Returns:
        None

    Example:
        print_slot_machine([['B', 'C', 'D'], ['C', 'D', 'D'], ['B', 'B', 'C']])
        Output:
        B | C | B
        C | D | B
        D | D | C

    Note:
    The function assumes that the number of rows in each column is the same, and the input 'columns' list contains valid slot machine spins.
    """

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                # Print the symbol followed by a "|" to separate columns (except for the last column)
                print(column[row], end=" | ")
            else:
                # Print the symbol without "|" for the last column
                print(column[row], end="")
                
        print()

            
def deposit():
    """
    Prompt the user to enter a valid deposit amount and return said valid deposit.

    The method repeatedly asks the user to input a valid deposit amount in dollars as a string. 
    It validates the input to ensure it consists of digits and handles negative numbers. 
    If a valid positive amount is entered, the loop breaks, and the method concludes.
    If the input is invalid or not a positive number, appropriate error messages are displayed.

    Args:
        None

    Returns:
        int: User's deposit amount
    """
    
    while True: # Prompt the user to enter a valid deposit amount
        deposit = input(emoji.emojize('Please enter your deposit. :heavy_dollar_sign:'))  # User input: amount in dollars as a String
        
        if deposit.lstrip('-').isdigit():
             deposit = int(deposit) # User deposit is a digit; deposit variable is now of type int
             if deposit > 0:
                 break
             else: 
                 print('Your deposit must be greater than 0', emoji.emojize(':red_exclamation_mark:'), sep = '')
        else: 
            print('Your deposit must be a positive digit', emoji.emojize(':red_exclamation_mark:'), sep = '')
    
    return deposit 

def get_number_of_lines():
    """
    Prompt the user to enter a valid number of lines to bet on and return said valid number.

    The method repeatedly asks the user to input the number of lines they want to bet on.
    It validates the input to ensure it consists of digits and handles negative numbers.
    If a valid positive amount is entered, the loop breaks, and the method concludes.
    The maximum number of lines allowed is determined by the constant MAX_NUM_OF_LINES.

    Args:
        None

    Returns:
        int: The number of lines the user wants to bet on, within the range of 1 to MAX_NUM_OF_LINES.
    """
    
    while True: # Prompt the user to enter a valid number of lines to bet on 
        lines = input(emoji.emojize('Please enter the number of lines to bet on (1-' + str(MAX_NUM_OF_LINES) + '). :money_bag: '))  # User input: number of lines to bet on
        
        if lines.lstrip('-').isdigit():
             lines = int(lines) # User input is a digit; lines variable is now of type int
             if 1 <= lines <= MAX_NUM_OF_LINES:
                 break
             else: 
                 print('Your lines input is not within the range of 1-' + str(MAX_NUM_OF_LINES), emoji.emojize(':red_exclamation_mark:'), sep = '')
        else: 
            print('Your lines input must be a positive digit within the range of 1-' + str(MAX_NUM_OF_LINES), emoji.emojize(':red_exclamation_mark:'), sep = '')
    
    return lines
    
def get_bet(): 
    """
    Prompt the user to enter a valid bet amount for each line and return said valid bet.

    The method repeatedly asks the user to input the bet amount they want to place on each line.
    It validates the input to ensure it consists of digits and handles negative numbers.
    If a valid positive amount is entered, the loop breaks, and the method concludes.
    The minimum and maximum bet amounts are determined by the constants MIN_BET and MAX_BET.

    Args:
        None

    Returns:
        int: The bet amount the user wants to place on each line, within the range of MIN_BET to MAX_BET.
    """
    
    while True: # Prompt the user to enter a valid bet 
        bet_amount = input(emoji.emojize('Please enter your bet amount for each line. :heavy_dollar_sign:'))  # User input: bet amount
        
        if bet_amount.lstrip('-').isdigit():
             bet_amount = int(bet_amount) # User input is a digit; bet_amount variable is now of type int
             if MIN_BET <= bet_amount <= MAX_BET:
                 break
             else: 
                 print('Your bet is not within the range of ' + str(MIN_BET + '-' + MAX_BET), emoji.emojize(':red_exclamation_mark:'), sep = '')
        else: 
            print('Your lines input must be a positive digit within the range of ' + str(MIN_BET + '-' + MAX_BET), emoji.emojize(':red_exclamation_mark:'), sep = '')
    
    return bet_amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True: 
        bet_amount = get_bet()
        total_bet = bet_amount * lines
        
        if total_bet > balance: 
            print(f'You do not have enough to bet that amount, your current balance is {balance}')
        else: 
            break
    
    print(f'You are betting ${bet_amount} on {lines} line(s). Total bet is equal to ${total_bet}.')
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
main()