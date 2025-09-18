tuple1=[0,1,2,3,4,5,6]

# Indexing always starts with zero

#   [0,1,2,3,4,5,6]     for easy understanding, here the values are indexes

print(tuple1[0])         # This is how a list can be accessed
print(tuple1[2])
print(tuple1[5])

# We can access the list is reverse order and it starts with -1

print(tuple1[-1])
print(tuple1[-5])


# Slicing
# It is similar to string slicing   [start : stop-1 : step]
# start-start index, stop-stop index, step-jumping value, and it's default value is 1

print(tuple1[0:5])
print(tuple1[2:6])
print(tuple1[0:7:2])

# We can use negative values for slicing too

print(tuple1[-3:-1])
print(tuple1[-7:-1:2])

