'''
Name: Luke Weiksner
Description: Asks the user for a name and than provides a menu of different for the user to run.
Bugs: None
Features: Menu
Sources: Mr. Campbell
Log: 1.0 initial release

'''
import random
prefix = ('Dr.','Mr.','Ms.','Mrs.','Miss.','Dr','Mr','Ms','Mrs','Miss')
functions = ('Print your Firstname', 'Middlename(s)', 'Lastname', 'Reverse your name/word', 'Count a certain amount of letters in your name/word', 'Find the consonant frequency in your name/word', 'Convert your name/word into lowercase', 'Convert your name/word into uppercase', 'Shuffle the letters in your name/word', 'Find if there is a hyphen in your name or word', 'Find if your firstname or word is a palindrome', 'Print your initials', 'Find if your name has a title/distinction', 'bonus')

def reverse(name):
    '''
    Description: Reverses the name entered by the user 

    Args:
        name - the name of the user that they entered
    Returns:
        returns their name backwards
    '''
    reverse_name = name[::-1]           #set reverse_name as the name backwards 
    print(reverse_name)
def vowels(full_name):
    '''
    Description: finds the 
    
    Args:
        name - the name of the user that they entered
    Returns:
        returns their name backwards
    '''
    count = 0
    vowels = 'aAeEiIoOuU'
    for char in full_name:     #for every character in the name
        if char in vowels:     #if the character is in the vowels list
            count += 1
    return count
def letter_counter(what_letter, full_name):
    '''
    Description: finds the amount of times a letter occurs in a person's name 
    
    Args:
        what_letter - the specific letter that the user wants to find how many times it occurs
        full_name - the full name not split that was entered by the user
    Returns:
        returns the counter of the amount of times the letter occcurs
    '''
    counter = 0
    for i in full_name:             #for every letter in full_name
        if i is what_letter:        #if that letter is equal to the letter entered by the user
            counter += 1            #add one
    return counter
def first_name(name):    
    '''
    Description: Finds the first name of the user 
    
    Args:
        name - the name of the user(split) that they entered
    Returns:
        returns their first name or name at the index 0
    '''
    return(name[0])         #giving back the first name as the first thing in the name
def middle_name(name, length):
    '''
    Description: Finds the middle name of the user 
    
    Args:
        name - the name of the user that they entered
        length - the amount of words in their name
    Returns:
        returns their middle name
    '''
    if length > 2:
        return' '.join(name[1:length-1])        #printing all the names in between the first and the last
    else:
         return "You don't have a middle name"
def last_name(name, length):
    '''
    Description: Reverses the name entered by the user 
    
    Args:
        name - the name of the user that they entered
    Returns:
        returns their name backwards
    '''
    if length > 1:
        return(name[length-1])          #returning the last name
    else:
        return("you did not enter a last name")
def consonant_frequency(full_name):
    counter = 0
    consonant = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWYZ")
    for letter in full_name:            #for every letter in the user entered name
        if letter in consonant:         #if the letter in the consonant letter
            counter += 1                #add one to counter
    amount = len(full_name)
    freq = (counter/amount)
    rounding = round(freq, 2)*100       #rounding the freq and multiplying it by 100 to make it a percentage
    return rounding
def lowercase(full_name):
    lower = ""
    for letter in full_name:                    #for every letter in the user entered
        letter_number = ord(letter)             #letter_number is equal to the ordinal of letter
        if 65 <= letter_number <= 90:           #if the number is in between 65 and 90 in ascii table
            letter_number += 32                 #add 32 which on the ascii table is the same letter lowercase
        lower = lower + chr(letter_number)      #turning letters into lowercase
    return lower
def uppercase(full_name):
    upper = ""
    for letter in full_name:                #for every letter in full name
        letter_number = ord(letter)         #turning the letter into the corresponding number on ascii table       
        if 97 <= letter_number <= 122:      #if the corresponding number is between 97 and 122  
            letter_number -= 32             #subtracting 32 which on ascii table is the same letter but lowercase
        upper = upper + chr(letter_number)
    return upper
def hyphen(name):
    hyp = '-'
    lastname = name[-1]
    for letter in lastname:         #for every letter in lastname
        if letter == hyp:           #if any letter is a hyphen
            return True             
    return False
def shuffle_name(full_name):
  character_list = list(full_name)      #turning full name into a list of characters
  random.shuffle(character_list)        #shuffling the character list randomly
  return ''.join(character_list)
def palindrome(full_name):
    if (full_name == full_name[::-1]):      #if full name is the same backwards
        return True
    else:
        return False
def find_initials(name):
    initials = []
    for word in name:               #for every word in the user entered name
        initials += [word[0]]       #making initials the first letter of every letter
    return "".join(initials)        #joining the initials of the name together
def find_prefix(name):
    if  name[0] in prefix:          #if the first word in the name is in the prefix list
        return True
    else:
        return False    
def bonus(character_list):
    number_letter = len(character_list)                                                         #finding the number of character in the list
    for i in range(number_letter - 1, 0, -1):                                                   #
        space = random.randint(0, i)                                                            #making the space variable between 0 and the number of characters     
        character_list[i], character_list[space] = character_list[space], character_list[i]
    return ''.join(character_list)


                
def main():
    run = "yes"
    while run == "yes":
        full_name = input("Please enter your full name without special or weird characters: ")
        counter = 0
        extracharacter = ("!@#$%^&*()~_=+[|\:',<.>/?]1234567890")
        #checking if the name has no weird or extra character
        for char in full_name:
            if char in extracharacter:
                counter = counter =+ 1
        if counter > 0:
            print("Invalid, you used a special or weird character")
        else:
            run = "no"
    character_list = list(full_name)    
    name = full_name.split()
    length = len(name)
    while True:
        for i in range(len(functions)):                                         #for every function in the list
            v = functions[i]
            print(f"{i} {''.join(v)}")                                          #adds the number to the dedicated function
        choice = input("what option would you like to select?")
        #using the user choice and then printing the function they choose
        if choice == "0":    
            print(f"First name: {first_name(name)}")
        elif choice == "1":
            print(f"middle name: {middle_name(name, length)}")
        elif choice == "2":
            print(f"last name: {last_name(name, length)}")
        elif choice == "3":
            print(f" your reverse name is {reverse(full_name)}")
        elif choice == "4":
            what_letter = input("what letter would like to know?")
            print(f"the {what_letter} appears {letter_counter(what_letter, full_name)} times in your name")
        elif choice == "5":    
            print(F"The consonant frequency is {consonant_frequency(full_name)}%")
        elif choice == "6":
            print(f"your lowercase name is {lowercase(full_name)}")
        elif choice == "7":
            print(f"your uppercase name is {uppercase(full_name)}")
        elif choice == "8":
            print(f"your name shuffled is {shuffle_name(full_name)}")
        elif choice == "9":
            print(hyphen(name))
        elif choice == "10":
            print(palindrome(full_name))
        elif choice == "11":
            print(f"your initials are {find_initials(name)}")
        elif choice == "12":
            print(find_prefix(name))
            if find_prefix(name) == True:
                name.pop(0)
                length = len(name)
        elif choice == "13":
            print(bonus(character_list))
        else:
            print("Please enter a valid number(0-12)")

main()
