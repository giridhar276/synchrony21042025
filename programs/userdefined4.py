# variable length arguments
# *args is the tuple
def display(*args):
    print(type(args))
    for val in args:
        print(val)
display(10,20,30,40,67,4,3,45,32,67,54,2,56,2,45,32,67,32,42,2,1,6,73,3,4,43,3,34,32,34,4,5,4)


# **kwargs is the dictionary
def displayinfo(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

displayinfo(chap1 = 10 , chap2 = 20)


