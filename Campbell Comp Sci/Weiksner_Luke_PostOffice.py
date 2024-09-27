
'''
Name: Luke Weiksner
Description: Program that determines the size of package and the cost based on the the parameters that the user enters.
Bugs: 
Features: (challenges)
Sources:W3 Schools
Log: 1.0 initial release
'''

def main():
    print("Welcome to the GCDS Post Office!")
    while True:
        dimensions = input("give me data for a post office in order of height,length,width,where it is going, and from where it is coming from. ")
        for item in dimensions:                                 #iterates through the list above
            #if an item in the list has a letter re-ask the user to only enter numbers                               
            if item.isalpha():                                  
                dimensions = input("Incorrect format(numbers only), please enter your height,length,and width with the zip code to where it is going and what zip it is coming from")
                continue

        dimensions = dimensions.split(",")   #splitting the dimensions by every comma  

        #if the user enter more or less than 5 groups of numbers than it prompts the user to re-enter the numbers split by commas                 
        if len(dimensions) != 5:                               
            dimensions = input("Incorrect format, please enter your height,length,and width with the zip code to where it is going and what zip it is coming from")
        else:
            try:
                height = float(dimensions[0])                               #saving the 0 index(first thing said by user) as height and turning it into an float
                length = float(dimensions[1])                               #saving the first index as length and saving it as an float
                width = float(dimensions[2])                                #saving the second index from dimensions as float
                to_where = int(dimensions[3])                               #saving to_where as an int and it is the third index
                from_where = int(dimensions[4])                             #saving from_where to an int and it is the fourth index
                from_where > 99999
                to_where > 99999
                distance = abs(get_zone(to_where) - get_zone(from_where))     #distance is equal to the subraction of the two zipcodes
                size = get_mail_type(length,height,width)                     #size is equal to the function of get_mail_type which gets the size of the parcel
                price = cost(size,distance)                                   #price is equal to the function cost 
                price = str(price)
                price = price.lstrip("0")           #removes zero from cost the cost when printed  
                print(f"Your parcel is a {size} and the price is ${price}") #printing the f string which includes the size and price
                break
            except ValueError:
                print("You did not enter the correct information")


 


def get_mail_type(length,height,width):
    '''
    Calculates what the type of mail being sent is and what dimensions fit the different types of packages

    Args:
        length: the first number that the user entered when prompted
        height: the second number that the user entered when prompted
        width:the third number that the user entered when prompted
    Returns:
        returns the package type as a string based on the dimensions given by the user in the args
    '''
    #determining the type of main based on dimensions
    if (3.5 <= length <= 4.25) and (3.5 <= height <= 6) and (.007 <= width <= .016):
        return "REGULAR POST CARD"    
    elif (4.25 <= length <= 6) and (6 <= height <=11) and (.007 <= width <=.015):
        return "LARGE POST CARD"
    elif (3.5 <= length <= 6.125) and (5 <= height <=11.5) and (.016 <= width <=.25):
        return "ENVELOPE"
    elif (6.125 <= length <= 24) and (11 <= height <=18) and (.25 <= width <=.5):
        return "LARGE ENVELOPE"
    elif (length +2*height +2*width<84):
        return "PACKAGE"
    elif (84<length +2*height +2*width<130):
        return "LARGE PACKAGE"
    else:
        return "UNMAILABLE"

def get_zone(zipcode):
    '''
    Calculates the zones of the zipcode being entered by the user.

    Args:
        zipcode: what the user inputted and it will be put into the funtion

    Returns:
        it returns the zone of the number of the zip being thrown into it
    '''
    #finding the zone of the zipcodes entered.
    if 1 <= zipcode <= 6999:
        return 1
    elif 7000<=zipcode<=19999:
        return 2
    elif 20000 <=zipcode<=35999:
        return 3
    elif 36000 <=zipcode<=62999:
        return 4
    elif 63000 <=zipcode<=84999:
        return 5
    elif 85000 <=zipcode<=99999:
        return 6

def cost(size,distance):
    '''
    Calculates the cost of each package with zipcode with the size and the distance.

    Args:
        size: what the package type is(using the get_mail_type function)
        distance: the subtraction of the two zipcodes which turns it into a positive number using absolute value

    Returns:
        it returns the cost of the parcel by using its size multiplied by the zones it goes through.
    '''
    #finding the cost of the package multiplied by the zones crossed
    if size == 'REGULAR POST CARD':
        return .20+.03*distance
    elif size == 'LARGE POST CARD':
        return .37+.03*distance
    elif size == 'ENVELOPE':
        return .37+.04*distance
    elif size == 'LARGE ENVELOPE':
        return .6+.05*distance
    elif size == 'PACKAGE':
        return 2.95+.25*distance
    elif size == 'LARGE PACKAGE':
        return 3.95+.35*distance
    elif size == 'UNMAILABLE':
        return " cannot be generated"


main()
