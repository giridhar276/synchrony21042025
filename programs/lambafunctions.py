#Disadvantage: this program has many jumps
### function body
# fixed arguments
def display(a , b):
    c = a + b
    return c

total = display(10,20) #calling function
print(total)


# lambda function
# lambda is replacement of single liner function only
#syntax:   functioname = lambda variables : expression
display = lambda a,b : a + b

total = display(10,20) #calling function
print(total)

#
display = lambda num : "even" if num %2==0 else "odd"
total = display(10) #calling function
print(total)

# Everytthing that runs on OS is called process
# Every process contains system calls




#method1
alist = ["unix","python","c","oracle"]
#[4,6,1,6]
blist = []
for item in alist:
    blist.append(len(item))
print(blist)

#method2
#map(function,iterable)   # function can be builtin or userdefined
alist = ["unix","python","c","oracle"]
def getlen(x):
    return len(x)
print(list(map(getlen,alist)))  #[4,6,1,6]


#method3
getlen = lambda x : len(x)
print(list(map(getlen,alist)))

#metho4

print(list(map(lambda x : len(x),alist)))


alist = ['1','2','3','4']
[1,2,3,4]
print(list(map(int,alist)))

data = ["python","unix","java"]  
#["python programming","unix programming","java programming"]
print(list(map(lambda x: x + " programming",data)))




#############
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 1, 'b': 2, 'c': 3}

#output:  {'a': 11, 'b': 22, 'c': 33}

#map(function, iterable)
finaloutput =  dict(map(lambda k: (k, dict1[k] + dict2[k]),dict1))   

print(finaloutput)





names = ['alice', 'bob', 'charlie']
capitalized = list(map(str.capitalize, names))
print(capitalized)

###################
raw_data = ['  apple  ', '  banana ', 'cherry  ']
clean_data = list(map(str.strip, raw_data))
print(clean_data) 

#####################
emails = ['user1@gmail.com', 'user2@yahoo.com', 'user3@outlook.com']
domains = list(map(lambda email: email.split('@')[1], emails))
print(domains)


#######################
prices = {
    'Shirt': 1500,
    'Jeans': 2500,
    'Jacket': 4000
}
# Apply 10% discount
discounted = dict(map(lambda item: (item[0], round(item[1] * 0.9)), prices.items()))
print(discounted)
# {'Shirt': 1350, 'Jeans': 2250, 'Jacket': 3600}



