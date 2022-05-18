# For reading CSV
import csv
import pprint # maybe used later

with open('data.csv', newline='') as f: #open csv
    reader = csv.reader(f) # define reader (this may correspond to "cur")
    i = 0
    m = 1
    cd1 = 0
    for row in reader:
        i += 1 #record number
        j = i-1 
        if row[2] != row[2]: #This needs to be edited. I failed to use row[2] != reader[j][2]
            cd1 += 1
        else:
            pass      
        num1 = str(cd1)
        if len(num1) == 1:
            num1 = "00" + num1
        elif len(num1) == 2:
            num1 = "0" + num1
        else:
            pass
        code1 = row[1] + num1

        row[4] = code1
        print(row)
    
    #l = [row for row in reader]
    #print(l[1][1])

