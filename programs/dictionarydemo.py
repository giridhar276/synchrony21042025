
book = {"chap1":10 , "chap2":20,"chap3":30 ,"chap4":40}
print(book)
# display individual values
print(book['chap1'])
print(book['chap2'])

# create new key:value pairs
book["chap5"] = 50
book["chap6"] = 60
print(book)

# display keys
print(book.keys())

# display values
print(book.values())

# display key-value items
print(book.items())

newbook = {"chap7":70 ,"chap8":80}
# method1
finalbook = {**book, **newbook} # we are creatting new object named finalbook
print(finalbook)
# method2
book.update(newbook)  # book is getting updated
print(book)


#print(book["chap11"])
#method1
if "chap11" in book:
    print(book["chap11"])
else:
    print("key doesnt exist")

# method2
print(book.get("chap11"))  # if key is found... it returns the value
                           # if key is not found... it returns None


book = {"chap1":10 , "chap2":20,"chap3":30 ,"chap4":40}
# display keys
for key in book.keys():
    print(key)


# display values
for val in book.values():
    print(val)

# dsiplay key-value pair
for k,v in book.items():  #[('chap1', 10), ('chap2', 20), ('chap3', 30), ('chap4', 40), ('chap5', 50), ('chap6', 60)]
    print(k,v)

for item in book.items():
    print(item)