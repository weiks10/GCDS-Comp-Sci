'''
Name: Luke Weiksner
Description: Opens a text file and removes all unecessary words, punctuation from it as well as making it all lowercase. It then sorts the words, puts them into a csv, and then into a pie chart.
Bugs: None
Features: matplotlib and sorting the dictionary
Sources:W3 Schools, Geeks for Geeks, Stack Overflow, Jeremy Morgan
Log: 1.0 initial release
'''
#importing libraries to the computer
from matplotlib.pyplot  import pie,axis,show
import pandas as pd
import re
import csv
import matplotlib.pyplot as plt

counts = dict() #making counts a dictionary
unnecessary_words = ['ever','can','every','or','make','more','am','now','and','the','to','of','i','a','in','for','our','we','that','is','he','are','will','who','my','with','us','be','as','she','not','you','on','it','this', 'an','when','have','has','but','would','was','one','their','me','all','know','they','his','about','up','at','because','out','what','so','from','always','let','by','never','going','them','been','your','were','no']

def pie_chart(filename,fhand):
    '''
    Creates a dictionary from a text file and then sorts it, deletes unecessary words, and gives a pie chart. 
    Args:
        filename: is a string and is a csv
        fhand: the file being entered as a string and is put in read mode
    Voids:
        returns nothing
    '''
    for line in fhand:                                  #scans each line in file entered
        line = line.lower()                             #making every line in every line lowercase
        words = line.split()                            #splits the strings into a list of words in a variable called words
        for word in words:                              #for each in the word in the list words
            word = re.sub(r'[^\w\s]', '', word)         #this function substitutes all non-word characters with an empty string under the variable word
            if word not in unnecessary_words:           #if a word in the list words is not in the list unecessary_words
                if word not in counts:                  #if the word in the list word is not the dict counts
                    counts[word] = 1                    #make the value of the word equal to 1
                else:
                    counts[word] += 1                   #add 1 to the value of the word if it has already been used

    sorted_dict = dict(sorted(counts.items(), key=lambda item:item[1], reverse = True))
    new_counts = dict()                                 #making new_counts a dictionary
    count = 0                                           #setting count equal to 0           
    for i in sorted_dict:                               #for the index in sorted_dict
        if count < 10:                                  #if the count of the word is greater than 10
            new_counts[i] = sorted_dict[i]              #new_counts is equal to the amount of times the word is in the sorted_dict
            count += 1                                  #add one to the count
        else:
            break

    with open (filename, 'w', newline = '') as csvfile: #opening the file in write as a csv file
        csvwriter = csv.writer(csvfile)                 #making csvwriter the function of writing to the csv file
        fields = ['word', 'count']                      #the names that will be displayed in the columns in the csv file
        csvwriter.writerow(fields)                      #writing the fields in the csv file
        for word in new_counts:                         #for the word in new_counts
            csvwriter.writerow([word, new_counts[word]]) #writing the word and the the new_counts(the value) of the word

    axis('equal')                                       #function that sets the x, y, and z axis equal to have equal lengths
    explode = (0.05,0.05,0,0,0,0,0,0,0,0)               #seperating 2 slices of the pie chart to emphasize them
    pie(new_counts.values(), labels=new_counts.keys(), explode=explode, autopct='%1.1f%%');     #creating a pie chart using new_counts with keys and values, exploding the two most occuring words and turning it into a percentage
    show()                                              #showing the pie_chart



    #for key,value in counts:
    #sorting by value in ascending order
fhand = open('kamala_new.txt','r')              #opening the kamala text file in the read more
kamala_speech = 'kamala_new.csv'                #making the speech a csvfile
plt.title("Kamala Speech")                      #title of the Kamala Speech
pie_chart(kamala_speech,fhand)                  #entering the kamala_speech and fhand into the pie_chart function
fhand = open('cleaned_trump_speech_transcript.txt','r')     #opening the trump text file 
trump_speech = 'cleaned_trump_speech_transcript.csv'        #making the speech a csv
plt.title("Trump Speech")                                   #making the title trump speech
pie_chart(trump_speech,fhand)                               #entering the paramters into the pie_chart function

                
