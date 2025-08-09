# A dictionary is a collection of unordered, modifiable paired (key: value) data type.

dic=dict()
print(dic)          # creates an empty dictionary into the variable "dic"

print(len(dic))      # len gives the len of the dic

# A dict can contain items of any datatypes.

dict1={"First_Name":"Mohamed","Last_Name":"Ibrahim","Age":20,"Location":"Chennai"}
dict2={1:1,2:2,3:3,4:4}
dict3={1:"Apple",2:"Orange",3:"Grapes"}


print(dict1,"\t",dict2,"\t",dict3)          # All the dicts are printed with a tab space between them

print(len(dict1),"\t",len(dict2),"\t",len(dict3)) 

# Accessing elements

print(dict1["Last_Name"])
print(dict2[4])
print(dict3[3])


# Adding new elements

dict1["Country"]="India"
print(dict1)

dict2[6]=6
print(dict2)


# Modifying values

dict1["Last_Name"]="Ibbu"
print(dict1)

dict3[2]="Mango"
print(dict3)