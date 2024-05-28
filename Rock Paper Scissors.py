'''
Author: Luke Weiksner
Date: 12/02/2023
Description: The game of Rock, Paper, Scissors. In my game there is a count of the score, which there is a user score and bot score. Once a
user or the bot gets 4 points the game is over.
Bugs: No Bugs
Challenges: The game keeps score over multiple games, Multiple different user errors are addressed, Introduce a score limit
Sources: Ms Marciano, Eli Murphy aka TA

'''
import random #bringing in random library

rps = ["rock","paper","scissors"]#the possible responses for the game being played.
bot_score = 0 #score of the bot
user_score = 0 #score of the user 
errors = ["no me gusta","invalid answer","That is not an answer","please use rock, paper, scissors","I cannot understand"] #list of invalid answers

while True: #infinite or forever loop that will continue to run unless it is broken
    print("bot score is",bot_score) #printing a string that contains the string bot score and is the bot score variable value
    print("user score is",user_score) #printing a string that contains the string user score and is the user score variable value
    if user_score == 4: #if the user reaches four points then the code will break
        print("user win") #will print user win
        break #then the code will break due to the user reaching 4 points
    if bot_score == 4: #if bot_score is 4 then the code will break
        print("user win") #will print user win
        break #will break the code if bot score is 4
    question = input("Do you want to play rock, paper scissors? ")#asking if the user would like to play rock paper scissors
    if question == "no": #if user answers no
        break #then code will break
    if question == "yes": #if user answer with yes
        user_rps = str.lower(input("please select rock, paper, or scissors "))#then will ask user to select rock paper or scissors
        if user_rps not in rps: #if the user does not use rock paper or scissors
            print(random.choice(errors)) #then it will print a random response in the list errors
        else: 
            bot_rps = random.choice(rps) #the bot choice of rock paper scissors 
            print(bot_rps) #printing the bots choice of Rock, Paper, Scissors

            if user_rps == bot_rps: #if the user and bot choose the same choice
                print("tie") #then print the word tie
            elif user_rps == "rock" and bot_rps == "paper": #if user chooses rock and bot chooses paper from rps
                print("bot wins") #then print bot wins
                bot_score += 1 #adds 1 to bot_score
            elif user_rps == "scissors" and bot_rps == "paper": #if user chooses scissors and bot chooses paper from rps
                print("user wins") #print user wins
                user_score += 1 #then adds 1 to user_score
            elif user_rps == "scissors" and bot_rps == "rock": #if user chooses scissors and bot chooses rock from rps
                print("bot wins") #print bot wins
                bot_score += 1 #then adding a point to bot score
            elif user_rps == "paper" and bot_rps == "rock": #is user chooses paper and bot chooses rock from rps list
                print("user wins") #print user wins
                user_score += 1 #then adding a point to user_score
            elif user_rps == "paper" and bot_rps == "scissors": #if user chooses paper and bot selects scissors from rps list
                print("bot wins") #printing bot wins
                bot_score += 1 #adding a point to bot_score
            elif user_rps == "rock" and bot_rps == "scissors": #if user selects rock and bot selects scissors
                print("user wins") #then it will print user wins
                user_score += 1 #then it will add a point to user_score
