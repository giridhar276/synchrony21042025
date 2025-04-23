


import csv

with open("employeeinfo.csv","r") as fobj:
    workset = set()
    header = fobj.readline()  # this line is just to read first line
    reader = csv.reader(fobj)
    for line in reader:
        workclass = line[1]
        workset.add(workclass)
    ## displaying output
    for wclass in workset:
        print(wclass)