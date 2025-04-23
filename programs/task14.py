'''
write a script to perform the below operations :

1. display current working directory
2. display login name
3. display all environment variables
4. display today's date ( timestamp )
5. display April months calendar
6. display all .py files and its size in bytes
7. display the modified time of employees.csv file
8. display current process id
9. set an environment variables. ( Eg.    TEST_PATH = "C:/Users/Admin/")

'''

import os
import datetime
import calendar
import time

print("current working directory :", os.getcwd())

print("login name :", os.getlogin())

print("****** ENVIRONMENT VARIABLES *******")
#print(os.environ)
for key,value in os.environ.items():
    print(key)
    print(value)
    print("---------")

print(datetime.datetime.now())
print(datetime.date.today())
print(calendar.month(2025,4))
print(calendar.calendar(2025))



for file in os.listdir():
    print(file,os.path.getsize(file),"bytes")


output = os.path.getmtime("task1.py")
print(output)
print(time.localtime(output))
print(datetime.datetime.fromtimestamp(output))
print(os.getpid())