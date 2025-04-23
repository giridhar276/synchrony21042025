# method1 : reading the file line by line
# fobj acts like cursor or handler
with open("companies.csv","r") as fobj:
    for line in fobj:
        print(line.strip())

# method2: fobj.readlines()
with open("companies.csv","r") as fobj:
    print(fobj.readlines()) # reads all the lines in list


# method3: fobj.read() # not suggested for reading bigger files
with open("companies.csv","r") as fobj:
    print(fobj.read())  # read the whole complete file to a string


#method 4: using
import csv # for reading and writing csv files
with open("companies.csv","r") as fobj:
    reader = csv.reader(fobj) # converting file object to csv object
    for line in reader:
        print(line)  # each line is automatically converted to list

# method4 : using pandas library
import pandas as pd
df = pd.read_csv("companies.csv")
print(df)

