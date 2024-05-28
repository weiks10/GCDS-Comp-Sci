'''
Author: Luke Weiksner
Date: 3/28/2024
Description: I created a shop which sells Barbeque items and addons/sides the code will ask the user how many items it would like and it gives that many items and sides
Bugs: No bugs
Challenges: Domain change, generating costs associated with items and addons, and ValueError
Sources: Ms. Marciano and TA(Eli Murphy)
'''
import random #importing random library

bbq_items = ["ribs", "brisket", "pulled pork", "whole hog", "burger", "pork belly", "steak", "wings"] #list of the names of the bbq main courses
bbq_addons = ["potatoes", "coleslaw", "corn", "bbq sauce", "french fries", "mac'n'cheese", "tater tots"] #List of the names of the possible sides for the bbq addons
m_costs = [19.99, 39.99, 24.99, 99.99, 14.99, 29.99, 32.99, 17.99] #Prices for the bbq main courses
s_costs = [3.99, 2.99, 1.99, 1.99, 2.99, 3.99, 2.99] #Prices of the bbq addons

while True: #infinite of forever loop
    try: #attempts the following code and doesnt do anything unless there an error
        number_of_bbq_items = int(input("How many items from the BBQ would you like?")) #asking the user how many items from the bbq it would like and than associating number_of_bbq_items with that number
        break #breaking the code
    except ValueError: #if there is an ValueError with the code above it will print "Please enter a a number
        print("Please enter a number!") #  
        
for i in range(number_of_bbq_items): 
    bbq_item = random.choice(bbq_items) #makes bbq_item a random term from the list of bbq_items 
    bbq_addon = random.choice(bbq_addons) #makes bbq_addon a random term from the list of bbq_addons
    
    print(f"{bbq_item} with a side of {bbq_addon}. Total cost is {round(m_costs[bbq_items.index(bbq_item)] + s_costs[bbq_addons.index(bbq_addon)],2)}") #printing what items they brought with addons and what the combined total cost is.


# print(f"{random.choice(bbq_items)} with a side of {random.choice(bbq_addons)}")
       
#   bbq_items.index(bbq_item)
#   bbq_addons.index(bbq_addon)
#    bbq_items = random.choice(m_costs)
#    bbq_addons = random.choice(s_costs)
#    s_costs = len(bbq_addons)
#    m_costs = len(bbq_items)

    
