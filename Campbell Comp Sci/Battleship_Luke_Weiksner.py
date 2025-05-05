import random
import time
'''
Name: Luke Weiksner
Description: A battleship game between a user and a computer with random guesses on a 5x5 board
Bugs: None
Features: None
Sources: Stack Overflow, w3 schools, python, geeksforgeeks, Mr. Campbell, NICHOLAS TRIPLETT
Log: 1.0 initial release

'''
wincon = 0
bot_win_con = 0

player_board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

bot_board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

guesses = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]

def print_board(board):
    """
    Makes the board as a 2d array    
    Args:
        none
    Returns:
        Returns the box
    """
    for row in board:                       #for all the rows in the board
        for col in range(len(row)):         #for the columns in the range of the number of the rows
            print(row[col],end = " ")       #printing the row for each column
        print("")

def place_ships(board):
    """
    Description:
        It asks for the user input of where to put five ships on their board   
    Args:
        board - the board of the user
    Returns:
        Returns the modified board with the newly placed ships
    """
    boats = 1
    while boats <= 5:
        try:  
            #asks the user for what row and column to place their ships on 
            row = int(input(f"\nPlace Ship #{boats} on row (1-5): ")) - 1
            col = int(input(f"Place Ship #{boats} on column (1-5): ")) - 1
            if 0 <= row < 5 and 0 <= col < 5:
                #if the board is 0 of where the user wants to place their ship than replace with a green "s".
                if board[row][col] == 0:
                    board[row][col] = "\033[32mS\033[0m"
                    boats += 1
                #if the board already has a ship 
                elif board[row][col] == "\033[32mS\033[0m":
                    print("You already placed a ship there.")
            else:
                print("Invalid boat placement. Try again.")     
        except ValueError:
            print("Invalid Entry. Please use 1,5")
    return board

def user_guess(bot_board, guesses):
    global wincon
    """
    Description:
        finds the user guess by asking for the col and row 
    Args:
        board - the board of the user
        guesses - empty board used to display user guesses
    Returns:
        Returns the user guess on the guess board
    """
    try:
        #asking user for row and column to guess
        row = int(input(f"Guess row (1-5): ")) - 1
        col = int(input(f"Guess column (1-5): ")) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            #if the user guesses the same spot twice
            if guesses[row][col] == '\033[31mH\033[0m' or guesses[row][col] == "\033[34mM\033[0m":
                print("you have already guessed that space, try again.")
                user_guess(bot_board, guesses)
            #if the bot board has a ship
            elif bot_board[row][col] == "\033[32mS\033[0m":
                guesses[row][col] = '\033[31mH\033[0m'      #replace empty board with hit
                print_board(guesses)
                wincon += 1
            elif bot_board[row][col] == 0:                  #if the space is empty on the board
                guesses[row][col] = "\033[34mM\033[0m"      #replace space with blue "m".
                print("bot board with user guess:")
                print_board(guesses)
        else:
            print("Invalid coordinates. Try again.")
            user_guess(bot_board, guesses)
    except ValueError:                                  #if there is a value than re run the function
        print("Invalid input. Enter numbers only.")
        user_guess(bot_board, guesses)

def check_win():
    """
    Description:
        checks for a win if there are no longer any ships on the board
    Args:
        none
    Returns:
        nothing just ends the code if a win is found
    """
    #if wincon is greater than five, print that the user won and exit the code
    if wincon >= 5:
        print_board(guesses)
        print("you win! Game over.")
        exit()
    #if bot wincon is greater than five, print that the bot won and exit the code
    if bot_win_con >= 5:
        print("Bot wins! Game over.")
        exit()
    
def bot_guess():
    global bot_win_con
    """
    Description:
        Finds the bot guess by asking for the random number for the row and column
    Args:
    Returns:
        Returns the your board with new bot guess
    """
    try:
        row = random.randint(1,5) - 1       #finding a random 1 through 5 subtracting 1 because of indices for the row
        col = random.randint(1,5) - 1       #finding a random 1 through 5 subtracting 1 because of indices for the col
   
        if 0 <= row < 5 and 0 <= col < 5:
            #if player board at the bot guess is a ship or empty
            if player_board[row][col] == "\033[32mS\033[0m" or player_board[row][col] == 0:
                #if the bot guess is a ship on player entered board 
                if player_board[row][col] == "\033[32mS\033[0m":
                    player_board[row][col] = '\033[31mH\033[0m'
                    bot_win_con += 1
                #if the bot guess is not a ship 
                elif player_board[row][col] != "\033[32mS\033[0m":
                    player_board[row][col] = "\033[34mM\033[0m"
            #if the bot guess guesses a space that is already guesses
            elif player_board[row][col] == "\033[31mH\033[0m" or player_board[row][col] == "\033[34mM\033[0m":
                bot_guess()
        else:
            print("Invalid coordinates. Try again.")
            print_board(guesses)
            print("Bot wins! Game over.")
    except ValueError:
        print("Invalid input. Enter numbers only.")
    
def generate_bot_board(board):
    """
    Description:
        generates bot board by generating random numbers for the ship placement   
    Args:
        board - the board of the user
    Returns:
        Returns the modified board with the newly placed ships
    """
    boats = 0
    while boats <= 4:
        #finding random numbers for row and column      
        random_row = random.randint(1,5) - 1
        random_col = random.randint(1,5) - 1
        #if the random col and row already have a ship placed on it
        if board[random_row][random_col] == "\033[32mS\033[0m":
            random_row = random.randint(1,5) - 1
            random_col = random.randint(1,5) - 1
        #if there is not a ship on the row and col
        elif board[random_row][random_col] != "\033[32mS\033[0m":
            board[random_row][random_col] = "\033[32mS\033[0m"
            boats += 1
    return board
    
def main():
    player_guesses = 100
    generate_bot_board(bot_board)
    print("Welcome to Battleship, the game will end if you run out of guesses or you or the bot guess all of the ships on the opponent board")
    print_board(bot_board)
    place_ships(player_board)
    print(f"here is your board with the placed ships")
    print_board(player_board)
    print("---------")
    print_board(guesses)
    while True:
        check_win()
        if player_guesses != 0:
            while True:
                try:                                                                        
                    print(f"you have {player_guesses} guesses left")
                    user_guess(bot_board, guesses)
                    player_guesses -= 1
                    time.sleep(2)
                    break
                except ValueError:
                    print("Enter a valid number")
        if player_guesses != 0:
            check_win()
            while True:
                bot_guess()
                print("---------")
                print("player board with bot guess:")
                print_board(player_board)
                break
        elif player_guesses == 0:
            exit()

main()
