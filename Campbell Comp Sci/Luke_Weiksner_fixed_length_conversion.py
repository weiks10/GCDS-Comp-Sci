'''
Name: Luke Weiksner
Description: Reads a student data text file and puts it into a csv file 
Bugs: None
Features: N/A
Sources: Mr. Campbell
Log: 1.0 initial release

'''


def main():
    fhand = open('student_data_cs2.txt','r')                                              #opening the text file
    with open ('fixed_length_conversion_Luke_Weiksner.csv', 'w') as csvfile:              #opening the file in write as a csv file
        for line in fhand:                                                                #scans each line in file entered                 
            csvfile.write(line[0:4].strip() + "," + line[5:19].strip() + "," + line[21:35].strip() + "," + line[36:42].strip() + "," + line[42:46].strip() + "," + line[47:58].strip() + "," + line[59:66].strip() + "," + line[67:76].strip() + "," + line[76:86].strip() + "," + line[86:87].strip() + "," + line[93:102].strip() + "," + line[102:112].strip() + "\n")
                                                                                          #writes in the csv file with the information split by the bytes and commas.
main()
