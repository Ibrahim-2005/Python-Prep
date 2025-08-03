def args_demo(*numbers):
    for i in numbers:
        print(i,"num")

args_demo(1,2,3,4,5)

# If we do not know the number of arguments we pass to our function, 
# we can create a function which can take arbitrary number of arguments by adding * before the parameter name.