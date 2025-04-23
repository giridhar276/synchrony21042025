


import csv
mcount = 0
fcount = 0
with open("employeeinfo.csv","r") as fobj:
    header = fobj.readline()  # this line is just to read first line
    reader = csv.reader(fobj)
    for line in reader:
        gender = line[9]
        if gender == "Male":
            mcount = mcount +1
        elif gender == "Female":
            fcount = fcount + 1
    
    print("Total male count   :", mcount)
    print("Total female count :", fcount)

