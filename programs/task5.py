

#pythonic way
ip = "192.168.{}.{}"
for val in range(0,2):
    for ival in range(1,101):
        finalip = ip.format(val,ival)
        print(finalip)



# 2nd method
ip = "192.168."
for val in range(0,2):
    ipaddress = ip + str(val)
    for ival in range(1,101):
        finalip = ipaddress + "." + str(ival)
        print(finalip)
