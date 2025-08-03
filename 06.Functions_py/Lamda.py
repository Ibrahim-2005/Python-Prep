# A lambda function is a small anonymous function
lambda argument : "expression"
# lamda is a keyword    

# 1. Addition
add=lambda a,b:a+b          #Here (a,b) is passed and arguments and (a+b) is returned 
print(add(1,5))

# 2. Reversed
last_char = lambda s: s[::-1]
print(last_char("Python")) 

# 3. Sorting
students = [("Apple", 85), ("Baloon", 95), ("Cat", 90)]
students.sort(key=lambda x: x[1])
print(students)  

