

# traditional way
#opening the file
fobj = open("languages.txt","w") # will be current working directly
# write operation
fobj.write("python\n")
fobj.write("sas\n")
fobj.write("unix\n")

# closing the file
fobj.close()

# pythonic way
# context manager
# if any line starts with keyword 'with' ... it is called context manager
# Other areas where context manager is used: 
#  database connections,network connections , server connections, socket connections
# Advantage:  file will be closed automatically
with open("languages1.txt","w") as fobj:
    fobj.write("python\n")
    fobj.write("unix\n")
    fobj.writelines(["unix\n","java\n"])
