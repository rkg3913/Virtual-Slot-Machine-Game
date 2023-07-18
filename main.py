import emoji # Import emoji module to allow the use of emojis

def deposit():
    """
    Prompt the user to enter a valid deposit amount.

    The method repeatedly asks the user to input a valid deposit amount in dollars as a string. 
    It validates the input to ensure it consists of digits and handles negative numbers. 
    If a valid positive amount is entered, the loop breaks, and the method concludes.
    If the input is invalid or not a positive number, appropriate error messages are displayed.

    Args:
        None

    Returns:
        None
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
            print('Your deposit must be a positive digit.', emoji.emojize(':red_exclamation_mark:'), sep = '')
            
deposit()