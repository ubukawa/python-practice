# For reading CSV
import csv

with open('data.csv', newline='') as f: #open csv
    reader = csv.reader(f) # define reader as CSB object
    data = [row for row in reader] # Extract CSV data as an object 
    #print(data[0]) 

i = 0 #record counter
ii = 0  #for counting support
j = 1 #admin1 num
k = 1 #admin2 num

for record in data:
    ### ADM1
    ii = i - 1
    if i < 2:  # I assume that the first record is title.
        j = 1
    elif data[i][1] != data[ii][1]: #If country changes, j will be 1
        j = 1
    elif data[i][2] != data[ii][2]: #if adm1 name is different from the previous one, add 1 to j
        j += 1
    else:
        pass 
    adm1 = str(j)
    if len(adm1) == 1:
        adm1 = "00" + adm1
    elif len(adm1) == 2:
        adm1 = "0" + adm1
    else:
        pass
    adm1 = record[1] + adm1
    if i != 0:
        record[4] = adm1
    else:
        pass

    ### ADM2
    if i == 0:
        k = 1
    elif data[i][1] != data[ii][1] or data[i][2] != data[ii][2]: #When country or ADM1 changes, k will be 1
        k = 1
    elif data[i][3] != data[ii][3]: #If ADM2 changes, add 1 to K
        k += 1
    else:
        pass
    adm2 = str(k)
    if len(adm2) == 1:
        adm2 = "00" + adm2
    elif len(adm2) == 2:
        adm2 = "0" + adm2
    else:
        pass
    adm2 = adm1 + adm2
    if i != 0:
        record[5] = adm2
    else:
        pass

    print(record)
    i += 1




#    i = 0
#    m = 1
#    cd1 = 0
#    for row in reader:
#        i += 1 #record number
#        j = i-1 
#        if row[2] != row[2]: #This needs to be edited. I failed to use row[2] != reader[j][2]
#            cd1 += 1
#        else:
#            pass      
#        num1 = str(cd1)
#        if len(num1) == 1:
#            num1 = "00" + num1
#        elif len(num1) == 2:
#            num1 = "0" + num1
#        else:
#            pass
#        code1 = row[1] + num1
#
#        row[4] = code1
#        print(row)
    
    #l = [row for row in reader]
    #print(l[1][1])

