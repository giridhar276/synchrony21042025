alist = [34,2,67,43,4,60,60,60,21,55]
alist.append(100)  # adding one single value
print("After appending :",alist)

getcount = alist.count(55)
print("count test:", getcount)

alist.extend([49,92,3])  # adding multiple values
print("After extending:", alist)

alist.insert (1,150)   #list.insert(index,value)
print("After inserting :",alist)

alist.pop(0)  # elimnate value at index 0
print("After pop operation:",alist)

alist.remove(60)  # remove 60 from the list
print("After remove operation :", alist)

if 79 in alist: 
    alist.remove(79)  # remove 79 from the list
    print("After remove operation :", alist)

alist.reverse()
print("reverse list :", alist)

alist.sort()  # ascending order # smallest to largest
print("Ascending order:",alist)