

#write a program to display all the file and directories from the current directory line by line


import os
try:
    files = os.listdir()
    #print(files)
    for file in files:
        print(file)
except Exception as err:
    print(err)

