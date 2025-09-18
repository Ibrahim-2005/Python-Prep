# Set is a collection of items which is unordered and does not allow duplicate items. 

st=set()          # creates an empty set into the variable "st"
print(st)

print(len(st))     # len gives the len of the set

# A set can contain items of any datatypes.

set1={1,2,3,4,5}
set2={"Apple","Orange","Banana","Grapes","Apple"}
set3={1,"Apple",2,"Orange",3,"Grapes"}

print(set1,"\t",set2,"\t",set3)          # All the sets are printed with a tab space between them

print(len(set1),"\t",len(set2),"\t",len(set3))  
