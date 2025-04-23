
print(1,2,3,4)
print("hello","python")
name = "python programming"
print(name)
print("I love", name) 
############ string slicing
#    string[start:stop:step] # step is incremental index
name = "python programming"
print(name[0])
print(name[1])
print(name[2])
print(name[8:12]) # from 8th to 11th index ( excluging 12th)
print(name[0:5])
print(name[0:18])  #python programming
print(name[0:18:1])#python programming
print(name[0:18:2])
print(name[1:18:3])
print(name[:])  #  name[0:18]      # python programming
print(name[::]) #  name[0:18:1]    # python programming
print(name[::1]) # python programming
print(name[::-1])# gnimmargorp nohtyp
# p    y   t   h   o   n      p    r   o   g    r   a    m   m    i   n    g
# 0    1   2   3   4   5   6  7    8   9   10   11  12  13   14   15  16   17
#                                                        -5  -4   -3  -2   -1

# everything is python is object
# every object contains methods

name = "python programming" 
print(name.capitalize())
print(name.title())
print(name.count("p"))
print(name.count("z"))
print(name.endswith("g"))
print(name.startswith("p"))
print(name.startswith("m"))
print(name.isupper())
print(name.islower())
print(name.isalpha())
print(name.replace("python","ruby"))
print(name.split(" "))
print(name.upper())
aname = "python"
print(len(aname))
aname = " python  "
print(len(aname))
print(len(aname.strip()))  # remove whitespaces at both ends
print(len(aname.lstrip())) # left side removval
print(len(aname.rstrip()))


print(name.find("gr"))  # if gr is found.. it returns the index of it

print(name.find("abc")) # if substring is NOT found... it returns -1

bname = "I love {} and {}"      #template
print(bname.format("python","java"))
print(bname.format("sas","tableau"))
print(bname.format(1,2))

#################################### conditional statments #########################
print(name.islower())
################################ simple if ########################
if name.islower() :
    print("string is lower")
    print("inside if")
    print("still inside if")


################################## if-else block #############################
if name.islower() :
    print("string is lower")
    print("inside if")
    print("still inside if")
else:
    print("string is upper")
    print("inside else")
    print("still inside else")


############################ if-elif -elif -elif-else ##########################
# read the input from keyword instead of hardcoding
language = input("Enter any language :")  # spark
if language == "python":
    
    print("you love python")
elif language == "java":
    print("you love java")
elif language == "spark":
    print("you love spark")
else:
    print("you love some other language")


# for loop - display all the numbers from 1 to 10
#for object in str|list|tuple|dict:
#    print(object)

for val in range(1,11):
    print(val)

print("-----")
name = "python"
for char in name[-3:]:
    print(char)


for char in name[::-1]:
    print(char)

alist = [10,20,30]
for val in alist:
    print(val)



# string slicing
# string methods
# conditions
# for loop