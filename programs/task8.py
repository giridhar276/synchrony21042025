
import csv
with open("employeeinfo.csv","r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print("Workclass:", line[1])
        print("Educaiton:", line[3])
        print("----------------")