x=6     #it is a global scope

def local_scope():
    x=9
    print(x)

local_scope()

# Local variable is a variable that can be accessed only in the function in which it is declared