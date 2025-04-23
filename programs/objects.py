
# differerence between list and tuple

alist = [10,20,30]  # 10 is accessbile using alist[0] 20 with alist[1]
print(alist[0])
alist[0] = 100
print(alist) # [100,20,30]

# tuple is immutable
atup = (10,20,30)
#atup[0] = 100  # error
print("tuple elements", atup)

atup = (10,20,30)

alist = list(atup)  # converting tuple to list
alist.append(40)
atup = tuple(alist) # converting back to tuple
print(atup)


print(dir(__builtins__))

print(4 + "hello")