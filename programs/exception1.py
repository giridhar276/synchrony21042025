

import csv
try:
    with open("employeeinfo11111.csv","r") as fobj:
        reader = csv.reader(fobj)
        for line in reader:
            print(line)
except FileNotFoundError as e:
    print("File is not found.. pl check")
    print(e)
except TypeError as e:
    print("Invalid operation")
    print(err)
except ValueError as e:
    print("Invalid input")
    print(err)
except ( KeyError,IndexError) as err:
    print("INvalid key or input")
    print(err)
except Exception as err:
    print(err)



import csv
try:
    with open("employeeinfo11111.csv","r") as fobj:
        reader = csv.reader(fobj)
        for line in reader:
            print(line)
except Exception as err:
    print(err)