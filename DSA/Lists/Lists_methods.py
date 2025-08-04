"""
append()	Adds an element at the end of the list
extend()	Add the elements of a list to the end of the current list
insert()	Adds an element at the specified position
index()	    Returns the index of the first element with the specified value
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
sort()	    Sorts the list
reverse()	Reverses the order of the list
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
clear()	    Removes all the elements from the list

"""

list1=["Apple","Orange","Banana"]
print(list1)
list1.append("Grapes")
print(list1)
list1.append("Mango")
print(list1)
list1.extend(["Papaya","Mosambi","Apple"])
print(list1)
list1.insert(0,"Pomogranate")
print(list1)
print(list1.index("Apple"))
list2=list1.copy()                      # list2 is a new list object with new address and with the copy of elements of list1
print(id(list1),id(list2))
print(list1.count("Apple"))
list1.sort()
print(list1)
list1.reverse()
print(list1)
list1.pop()
print(list1)
list1.remove("Mosambi")
print(list1)
list1.clear()
print(list1)
