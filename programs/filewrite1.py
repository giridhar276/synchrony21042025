
####### If the file has to created in different path 
#fobj = open("C:\\Admin\\Desktop\\languages.txt","w")
#fobj = open("C:/Admin/Desktop/languages.txt","w")
#fobj = open(r"C:\Admin\Desktop\languages.txt","w")  # raw string
# traditional way
#opening the file
fobj = open("languages.txt","w") # will be current working directly
# write operation
fobj.write("python\n")
fobj.write("sas\n")
fobj.write("unix\n")
fobj.writelines(["java\n","oracle\n","\n"])
fobj.write("\n")
for val in range(1,10):
    fobj.write(str(val)  + "\n")
# closing the file
fobj.close()