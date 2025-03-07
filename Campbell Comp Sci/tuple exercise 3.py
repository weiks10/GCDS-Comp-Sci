import string

counts = 0                          
dictionary_counts = dict()
relative_list = list()

fname = input('Enter file name: ')
fhand = open(fname)


for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1

for key, val in list(dictionary_counts.items()):
    relative_list.append((val / counts, key))  

relative_list.sort(reverse=True)        

for key, val in relative_list:
    print(key, val)