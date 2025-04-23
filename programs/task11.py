



# read operation
with open("employeeinfo.csv","r") as fr:
    # write operation
    with open("empbackup.csv","w") as fw:
        header = fr.readline()  # this line is just to read first line
        for line in fr: # reading line by line
            newline = line.replace("United-States","USA") # using str.replace()
            fw.write(newline)

