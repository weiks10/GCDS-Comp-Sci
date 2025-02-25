import random
prefix = ('Dr.','Mr.','Ms.','Mrs.','Miss.','Dr','Mr','Ms','Mrs','Miss')
functions = ('Print your Firstname', 'Middlename(s)', 'Lastname', 'Reverse your name/word', 'Count a certain amount of letters in your name/word', 'Find the consonant frequency in your name/word', 'Convert your name/word into lowercase', 'Convert your name/word into uppercase', 'Shuffle the letters in your name/word', 'Find if there is a hyphen in your name or word', 'Find if your firstname or word is a palindrome', 'Print your initials', 'Find if your name has a title/distinction')

def reverse(name):
    reverse_name = name[::-1]
    print(reverse_name)
def vowels(full_name):
    count = 0
    vowels = 'aAeEiIoOuU'
    for char in full_name:
        if char in vowels:
            count += 1
    return count
def letter_counter(what_letter, full_name):
        counter = 0
        for i in full_name:
            if i is what_letter:
                counter += 1
        return counter
        return
def first_name(name):
    return(name[0])
def reverse(full_name):
    reverse_name = full_name[::-1]
    return reverse_name
def middle_name(name, length):
    if length > 2:
        return' '.join(name[1:length-1])
    else:
         return "You don't have a middle name"
def last_name(name, length):
    if length >= 1:
        return(name[length-1])
    else:
        return
def consonant_frequency(full_name):
    counter = 0
    consonant = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWYZ")
    for letter in full_name:
        if letter in consonant:
            counter += 1
    amount = len(full_name)
    freq = (counter/amount)
    rounding = round(freq, 2)*100
    return rounding
def lowercase(full_name):
    lower = ""
    for letter in full_name:
        letter_number = ord(letter)
        if 65 <= letter_number <= 90:
            letter_number += 32
        lower = lower + chr(letter_number)
    return lower
def uppercase(full_name):
    upper = ""
    for letter in full_name:
        letter_number = ord(letter)
        if 97 <= letter_number <= 122:
            letter_number -= 32
        upper = upper + chr(letter_number)
    return upper
def hyphen(name):
    hyp = '-'
    lastname = name[-1]
    for letter in lastname:
        if letter == hyp:
            return True
    return False
def shuffle_name(full_name):
  character_list = list(full_name)
  random.shuffle(character_list)
  return ''.join(character_list)
def palindrome(full_name):
    if (full_name == full_name[::-1]):
        return True
    else:
        return False
def find_initials(name):
    initials = []
    for word in name:
        initials += [word[0]]
    return "".join(initials)
def find_prefix(name):
    if  name[0] in prefix:
        return True
    else:
        return False    
def bonus(character_list):
    number_letter = len(character_list)
    for i in range(number_letter - 1, 0, -1):
        space = random.randint(0, i)
        character_list[i], character_list[space] = character_list[space], character_list[i]
    return ''.join(character_list)


                
def main():
    run = "yes"
    while run == "yes":
        full_name = input("Please enter your full name without special or weird characters: ")
        counter = 0
        extracharacter = ("!@#$%^&*()~_=+[|\:',<.>/?]")
        for char in full_name:
            if char in extracharacter:
                counter = counter =+ 1
        if counter > 0:
            print("Invalid, you used a special or weird character")
        else:
            run = "no"
    name = full_name.split()
    character_list = list(full_name)
    length = len(name)
    while True:
        for i in range(len(functions)):
            v = functions[i]
            print(f"{i} {''.join(v)}")
            print("-----------------------------------------------------")
        choice = input("what option would you like to select?")
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
        else:
            print("Please enter a valid number(0-12)")

main()
