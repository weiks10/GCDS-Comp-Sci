'''
Name: Luke Weiksner
Description: Reads a student data text file and puts it into a csv file 
Bugs: None
Features: N/A
Sources: Mr. Campbell
Log: 1.0 initial release

'''


def main():
    fhand = open('student_data_cs2.txt')                                              #opening the text file
    with open ('fixed_length_conversion_Luke_Weiksner.csv', 'w') as csvfile:          #opening the file in write as a csv file
        for line in fhand:                                                            #scans each line in file entered                 
            csvfile.write(line[0:4].rstrip() + "," + line[5:19].rstrip() + "," + line[21:35].rstrip() + "," + line[36:42].rstrip() + "," + line[42:46].rstrip() + "," + line[47:58].rstrip() + "," + line[59:66].rstrip() + "," + line[67:73].rstrip() + "," + line[76:86].rstrip() + "," + line[86:87].rstrip() + "," + line[93:102].rstrip() + "," + line[102:112].rstrip() + "\n")
                                                                                      #writes in the csv file with the information split by the bytes and commas.
main()