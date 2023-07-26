import emoji # Import emoji module to allow the use of emojis
import random 

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
    all_symbols = []
    
    for symbol, symbol_count in symbols.items(): 
        for _ in range(symbol_count): 
            all_symbols.append(symbol)
    
    columns = [[], [], []]
    for col in range(cols): 
        column = []
        for row in range(rows):        

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
    
main()