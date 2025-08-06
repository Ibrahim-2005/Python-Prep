# A tuple is a collection of different data types which is ordered and unchangeable. 
# Tuples are written with round brackets, (). 


tup=tuple()          # creates an empty tuple into the variable "tup"
print(tup)

print(len(tup))      # len gives the len of the tup

# A tuple can contain items of any datatypes.


tuple1=(1,2,3,4,5)
tuple2=("Apple","Orange","Banana","Grapes")
tuple3=(1,"Apple",2,"Orange",3,"Grapes")

print(tuple1,"\t",tuple2,"\t",tuple3)          # All the lists are printed with a tab space between them

print(len(tuple1),"\t",len(tuple2),"\t",len(tuple3))  