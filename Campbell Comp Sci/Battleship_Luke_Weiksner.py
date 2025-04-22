import random
import time
'''
Name: Luke Weiksner
Description: A battleship game between a user and a computer with random guesses on a 5x5 board
Bugs: None
Features: None
Sources: Stack Overflow, w3 schools, python, geeksforgeeks, Mr. Campbell
Log: 1.0 initial release
'''
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
    boats = 1
    try:
        while boats <= 5:  
            row = int(input(f"\nPlace Ship #{boats} on row (1-5): ")) - 1
            col = int(input(f"Place Ship #{boats} on column (1-5): ")) - 1
            board[row][col] = "\033[32mS\033[0m"
            boats += 1
        return board
    except ValueError:
        print("Invalid Entry. Please use 1,5")

def user_guess(bot_board, guesses):
    try:
        row = int(input(f"Guess row (1-5): ")) - 1
        col = int(input(f"Guess column (1-5): ")) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            if bot_board[row][col] == "\033[32mS\033[0m":
                guesses[row][col] = '\033[31mH\033[0m'
                print_board(guesses)
            elif bot_board[row][col] != "\033[32mS\033[0m":
                guesses[row][col] = "\033[34mM\033[0m"
                print("bot board with user guess:")
                print_board(guesses)
        else:
            print("Invalid coordinates. Try again.")
            user_guess(bot_board, guesses)
    except ValueError:
        print("Invalid input. Enter numbers only.")
        user_guess(bot_board, guesses)
    
def bot_guess():
    try:
        row = random.randint(1,5) - 1
        col = random.randint(1,5) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            if player_board[row][col] == "\033[32mS\033[0m" or player_board[row][col] == 0:
                if player_board[row][col] == "\033[32mS\033[0m":
                    player_board[row][col] = '\033[31mH\033[0m'
                elif player_board[row][col] != "\033[32mS\033[0m":
                    player_board[row][col] = "\033[34mM\033[0m"
            elif player_board[row][col] == "\033[31mH\033[0m" or player_board[row][col] == "\033[34mM\033[0m":
                print("yay")
                bot_guess()
        else:
            print("Invalid coordinates. Try again.")
    except ValueError:
        print("Invalid input. Enter numbers only.")
    
def generate_bot_board(board):
    boats = 0
    while boats <= 4:      
        random_row = random.randint(1,5) - 1
        random_col = random.randint(1,5) - 1
        if board[random_row][random_col] == "\033[32mS\033[0m":
            random_row = random.randint(1,5) - 1
            random_col = random.randint(1,5) - 1
        elif board[random_row][random_col] != "\033[32mS\033[0m":
            board[random_row][random_col] = "\033[32mS\033[0m"
            boats += 1
    return board
    
def main():
    player_guesses = 10
    generate_bot_board(bot_board)
    place_ships(player_board)
    print(f"here is your board with the placed ships")
    print_board(player_board)
    print("---------")
    print_board(guesses)
    while True:
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
            while True:
                bot_guess()
                print("---------")
                print("player board with bot guess:")
                print_board(player_board)
                break
        elif player_guesses == 0:
            exit()




main()