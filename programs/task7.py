


import csv
with open("employeeinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)