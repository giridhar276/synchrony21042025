

#write a program to display .csv files only 


import os
try:
    files = os.listdir()
    #print(files)
    for file in files:
        if os.path.isfile(file)  and file.endswith(".csv") :
            print(file)
except Exception as err:
    print(err)
