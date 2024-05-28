'''
Author: Luke Weiksner
Date: 5/15/2024
Description: I created a password keeper that has multiple options. Examples of some of my options were to generate a secure password, print everything, print specific websites, usernames, and passwords, and change the username and password for the website.
Bugs: No bugs
Challenges: Allow the user to retroactively add more usernames and passwords, allow the user to change usernames and passwords, generate a secure password for the user, and check how complex/secure the passwords are
Sources: Ms. Marciano and TA(Eli Murphy)
'''

import random #importing the random library

def specific_return(websites, usernames, passwords, i):
    '''Prints the website at a given index in the websites list along with its corresponding password and username

    Args:
        websites (list): websites entered by the user
        usernames (list): Usernames entered by the user
        passwords (list): Passwords entered by the user
        i (int): The numbers in place for where items in a list are
    Prints:
        Prints websites, usernames, and passwords at a given index.
'''
    print(f'''website: {websites[i]} username: {usernames[i]} password: {passwords[i]}''')
def add_more(websites, usernames, passwords):
    '''Prompts the User to enter a website, username and password and then adds them to the corresponding lists

    Args:
        websites (list): websites entered by the user
        usernames (list): Usernames entered by the user
        passwords (list): Passwords entered by the user
'''
    websites.append(input("What would you like to store your website to be named?"))#adding the user answer of the name of the websites to the list websites
    usernames.append(input("What would you like to store your username as?"))#adding the name of the user input of name of the username and adding it to the username list
    passwords.append(input("What would you like you password to be?"))#adding the answer of the name of the password to the password list
def secure_password():
    '''Generates a secure password for the user using the lietters and digits
    Prints:
        Using the numbers, upper case and lower case letters, it joins them into password horizontally
'''
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    digits = list("1234567890")
    pwd = []

    for i in range(6):
        pwd.append(random.choice(digits)) #choosing 6 random digits from the digits list
        pwd.append(random.choice(list(letters.upper()))) #choosing 6 random uppercase letters from the letters list
        pwd.append(random.choice(list(letters.lower()))) #choosing 6 random lowercase letters from the letter list
    random.shuffle(pwd) #shuffle all of the random digits together
    pwd = ''.join(pwd) #joining the code on the same line horizontally.
    return(pwd)
def has_digits(string):
    '''has_digits finds if there is a digit or number in the thing that the user enters
    Args:
        String: The password that is entered by the user
'''

    return any(char.isdigit() for char in string)
def special_char(string):
    '''Finds if the user has entered a special character inside of the list called special
    Args:
        String: The password entered by the user
'''


    return any(char in list("!@#$%^&*()_+{}:<>?|") for char in string)
def check_password(has_digits, special_char):
    '''Checks if the users entered password is safe which needs to have 6 characters, 1 number, and 1 special character
    Args:
        has_digits (function): Checks if there digits in the password entered
        special_char (function): Checks if there are special characters in the the password entered
    Prints:
        It will print you have a safe password once you fulfill all the requirements for a safe password.
'''

    while True:
        pwd = input("Enter your password") 

        if has_digits(pwd) and len(pwd) > 6 and special_char(pwd): #the requirements that I created for a safe password
            print("you have yourself a safe password") #printing that you have a safe password if you pass the requirements.
            break #breaking the code
        elif not has_digits(pwd): #if the code does not have any numbers or digits
            print("enter more numbers, you need atleast 1") #printing that the user needs to enter more numbers
        elif len(pwd) < 6: #if the user has less than 6 characters
            print("enter more characters, you need 6 or more total") #printing that the user needs to enter more characters
        elif not special_char(pwd): #if there is no special character enter
            print("enter a special character, you need at least one") #printing that the user needs to enter at least one special character

        

def main():
    websites = []
    usernames = []
    passwords = []
    
    while True: #infinite or forevers loop
        add_more(websites, usernames, passwords)#using the function add_more asking them to enter more websites, passwords, and usernames if yes_or_no is yes 
        yes_or_no = input("Would you like to enter more usernames, websites, or passwords?") #asking the user if they want to add more

        if yes_or_no == "no": #if they respond with no the code will stop
            break #breaking the code

    while True:
        mode = input(f'''What would you like to do?
    1. Print all of your websites, usernames, and passwords
    2. Print the usernames and passwords for the website
    3. End
    4. Add more
    5. Generate random password
    6.check if password if secure
    7. Change Usernames and Passwords''') #depending on which mode the user the selects it will do the following
        if mode == "1":
            for i in range(len(websites)): #finding all of the websites
                specific_return(websites, usernames, passwords, i) #printing out all of the websites, usernames, and passwords that are corresponding
        elif mode == "2":
            name = input("Enter a website for the username and password: ")

            if name in websites: #if the entered website is correct
                specific_return(websites, usernames, passwords, websites.index(name)) #returning only the website, username, and password for that specific website
            else:
                print("Please enter a valid website")
        elif mode == "3":
            break #breaking the code
        elif mode == "4":
            add_more(websites, usernames, passwords) #calling the add more function
        elif mode == "5":
            print(secure_password()) #printing the secure password function
        elif mode == "6":
            check_password(has_digits, special_char) #calling the check_password function
        elif mode == "7":
            web = input("Enter a website")
                        
            if web in websites: #finds the index of the website that the user entered
                i = websites.index(web) #it returns the first occurence of the value of the website they entered.
                usernames[i] = input("Enter a new username") #giving the user an option to change the username for the specific website that they entered
                passwords[i] = input("Enter a new password") #giving the user an option to change the password for the specific website that they entered
            elif web not in websites: #if web is not in the websites 
                print("enter a valid website")
        else:
            print("Please enter a number 1-7")
            continue #restartung the while True loop
main() #calling the main function
            





