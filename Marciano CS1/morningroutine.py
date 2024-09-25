'''
Author: Luke Weiksner
Date: 11/1/2023
Description: Interactive walkthrough of my morning routine,
which allows uers to select the options in which I select to get ready for the day.
Bugs: No Bugs
Challenges: ?
Sources:
https://docs.google.com/presentation/d/1mM7m2PD4g8YggPutlbCtHnnT__fi_F7TzTlDVNozjNo/edit#slide=id.g24c455fdac6_0_13 
'''


import time #documentation

    
print("Alarm!") #displays to the user that the alarm is going off

while True: #Infinite or forever loop (acts as an alarm clock and if the user would like go back to sleep or wake up) - while condition True is true
    snooze = str.lower(input("Snooze?")) #prompts user to respond whether they want to snooze or not, converts that response to lowercase, and stores that response in the variable snooze
               
    if snooze == "yes": #if the user wants to snooze  
        print("Go back to sleep for 10 more minutes") #then it print go back to sleep and go to the beginning of the loop
        time.sleep(2) #telling program to not show any code for 2 seconds
    elif snooze == "no": #if the user wants wake up 
        print("Get up") #then it will print to get up
        break #breaking the loop
    else: #if the user does not answer with yes or no 
        print("Invalid") #then it will print that it was an Invalid Response.
    
while True: #Infinite or forever loop (asks the user if they showered and will tell them to go shower or brush teeth)
    shower = input("Did you shower after sports?") #prompts user to respond whether they showered or not also stores response in the variable shower
    time.sleep(3) #telling code to not show for 3 seconds
    if shower == "yes": #if the user showered after sports 
        print("go brush your teeth") #then it will answer with go brush your teeth and exit the loop
        break #breaking the loop if the user answered yes
    elif shower == "no": #if the user answers with no the user 
        print("Go Shower!")#then it will be responded with go shower and will leave the loop
        break #breaking the loop if the user answered yes
    else: #if the user does not answer with yes or no 
        print("Invalid") #then it will print that it was an Invalid
    
while True: #Infinite or Forever loop (asks the user whether it sunny and what they should wear)
    weather = input("is it sunny today?") #prompts user to respond whether it is sunny or not and also stores response in the variable weather
    time.sleep(1) #tells to code to not show code for 1 second
    if weather == "yes": #if it sunny outside
        print("put on shorts and a t-shirt") #Then it will tell the user to put on shorts and a t-shirt on
        break #breaking the loop if the user answered yes
    elif weather == "no": #if it is not sunny and the user responds with no
        print("put on a hoodie and sweatpants") #it will respond by saying to put on a pair of sweatpants and a hoodie
        break #breaking the loop once the user answers no
    else:#if the user does not answer with yes or no
        print("Invalid")#then it will print Invalid
    
while True: #Infinite or Forever loop (is asking the user whether they have school today or not)
    school = input("do you have school today?") #prompts user to respond whether they have school or not and stores response in the variable school
    time.sleep(1) #tells to code to not show code for 1 second
    if school == "yes": #if they have school today
        print("make sure you have completed your homework") #then it will answer with make sure you have completed homework and computer
        bag_packed = input("did you pack your homework and computer?")#prompts user to respond whether they have pack there stuff and stores response in the variable bag
        if bag_packed == "yes": #if they have packed their bag
            print("enjoy your day at school!") #Then it will respond with enjoy your day at school
        elif bag_packed == "no": #if the user did not pack their bag
                print("Make sure to pack everything before school") #Then the program will respond with make sure to pack everything before school
        break #once all is answered the user will then leave the loop
    elif school == "no": #if the user does not have school
        print("enjoy your day with your friends") #then it will print enjoy your day with your friends
        break #then the user will exit the loop
    else:
        print("Invalid")#if the answer is not yes or no

    
        
        

    





