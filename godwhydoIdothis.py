'''
Author: Luke Weiksner
Date: 5/12/2024
Description: I created a bunch of functions that are used to make the code more efficient. We also used our previous functions in our new ones
Bugs: No bugs
Challenges: Takes a string and reverses it, takes a string and checks whether it is a palindrome, takes a name and returns the initials
Sources: Ms. Marciano and TA(Eli Murphy)
'''
import random  #bringing the random library

def chorus (): #defining the function that I named chorus
    print("You are my sunshine")
    print("My only sunshine")
    print("You make me happy")
    print("When skies are gray")
    print("You'll never know, dear")
    print("How much I love you")
    print("Please don't take")
    print("My sunshine away")
def solo(): #defining the function solo that is full of print statements 
    print("The other night, dear")
    print("As I lay sleeping")
    print("I dreamed I held you")
    print("In my arms")
    print("When I awoke, dear")
    print("I was mistaken")
    print("So I hung my head and cried")

def add(num1,num2): #making a function that adds number 1 and number 2 together
    print(num1 + num2) #prints the sum of both numbers

def print_elements(my_list): #making a function with a list that I creae as the perameters.
    for element in my_list: #Starts a check that scans for an individual element in the list that I create called my_list
        print(element) #printing the individual element that it is scanning for
def contains_element(my_list,element): #Making a function with the previous function and element
    if element in my_list: #if the individual element is in the list
        return True #The computer will return True to the user
    else: #otherwise
        return False #the computer will False to the user
def is_int(string): #Making that a function that checks if the number the user enters is an integer
    if "-" in string: #if the user uses a - in the string
        string = string[1:]#making the number a whole because sometimes it would come out as a weird decimal
    if string.isnumeric(): #if the the input the user enters is a number
        return True #the computer will return true
    else: #otherwise
        return False #the computer will return False to the user
def get_random(): #creating a function that finds a number between two numbers entered by the user
    while True: #infinite or forever loop
        firstnum = input("What is your first number?") #creating an input that asks the user what their first number is
        secondnum = input("What is your second number?") #creating an input for the second number for the user to enter.

        if is_int(firstnum) and is_int(secondnum):  #checking if both numbers entered are numbers using the is_int function
            print(random.randint(int(firstnum), int(secondnum)))  #printing a random number in between the users two entered numbers.
            break #breaking the code
        else: #otherwise
            print("Please enter a number") #Printing code that asks the user to enter a number
def replace_str(string, old_char, new_char): #creating a function that replaces certain letters with new letters in the string
    new_string = "" #creating a place to hold the new string
    for s in string:  #for each letter in the entered string
        if s == old_char: #if letter is in the previous string
            new_string += new_char #replace that letter and enter the new character in the new string
        else: #otherwise
            new_string += s #if there is nothing to replace it just leave the letter
    return new_string #return the new and modified string
def reverse(string): #creating a function that reverses the string
    return string[::-1] #reversing the string that the user enters
def initials(name): #creating a function that gets the intials of the name that the user enters
    name = name.split(" ") #it splits the string into individual letters
    initials = "" #creating something to store the the name entered by the user
    for n in name: #for each letter in the entered name
        initials += n[0] #grabbing the first letter of the names
    return initials #returning the final product of the intials

def palindrome(string): #creating a function that makes a palindrome
    return string == reverse(string) #returning if the string is the same when the string is reversed used the reverse function.

def main(): #creating the main functions that run the other functions
    chorus()
    solo()
    chorus()
    add(2,7)
    my_list = ["Luke Weiksner", "Nick Triplett", "Seneca Greenwood"]
    print_elements(my_list)
    print(contains_element(my_list, "Seneca Greenwood")) 
    string = input("Enter your number to check if it is an integer: ")
    print(is_int(string))
    get_random()
    print(replace_str("hello world","l","a"))
    string = reverse(input("Enter a word and I'll repeat it backwards"))
    print(string)
    print(palindrome(input("Enter a word and I'll check if it is a palindrome")))
    name = input("Enter you full name ")
    print(initials(name))



main()#calling the main function
