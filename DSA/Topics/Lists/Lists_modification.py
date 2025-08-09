list1=["Apple","Orange","Banana","Grapes","Guava","Custard Apple","Mosambi"]
print(list1)
list1[0]="Avacado"                  # Changes the 0th element as "Avacado"
print(list1)
list1[-1]="Dragon Fruit"            # changes the last element as "Dragon Fruit"
print(list1)

list2=["Onion","Tomato","Potato"]
list3=list1+list2
print(list3)
del list3
# print(list3)      It throws error cause it is not present now