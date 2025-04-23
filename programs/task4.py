'''
write a program to display the below output
192.168.0.1
192.168.0.2
192.168.0.3
..
..
..
192.168.0.100
'''


# 1st method
ip = "192.168.0.{}"
for val in range(1,101):
    print(ip.format(val))




#2nd method
ip = "192.168.0."
for val in range(1,101):
    finalip = ip + str(val)
    print(finalip)


######################## for your understanding
print(3 + 4)
print("hello" + "python")
print([10,20] + [30,40])
print((10,20) + (40,50))

