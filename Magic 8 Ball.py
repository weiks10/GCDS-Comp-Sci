'''
Author: Luke Weiksner
Date: 11/14/2023
Description: A magic eight ball that you ask questions that will give you a list of answers
Bugs: No Bugs
Challenges: while True
Sources: ?
'''
import random #bringing in the random library for use of random functions
print("Hi! I am the world famous magic eight ball.")#displays what is inside of the parenthesis
while True: #infinite or forever loop that will ask the user what they want to ask and then will give them an answer from my list and then will restart once finished
    question = input("what do you want to ask the magic eight ball?") #defining the input question and printing my question.
    resp = ["Yes","No","Maybe","ask again later","I do not have an answer","IDK"] # list of possible responses that the magic eight ball has
    print(random.choice(resp)) #printing a random response from the resp list.
