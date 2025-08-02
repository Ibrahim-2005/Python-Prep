# With return value

def greeting(name):        # Here the name is known as parameter
    greet="Good Morning "+name
    return greet

name="Ibrahim"
print(greeting(name))       # Here the "name" is known as argument



# Without return value

def greeting(name):
    greet="Good Morning "+name
    print(greet)

name="Ibrahim"
greeting(name)



# We can give as many parameters and arguments

def greeting(first_name,last_name):
    greet="Good Afternoon "+first_name+" "+last_name
    print(greet)

first_name="Mohamed"
last_name="Ibrahim"
greeting(first_name,last_name)



# Parameters as key value pair

def greeting(first_name,last_name):
    greet="Good Evening "+first_name+" "+last_name
    print(greet)

greeting(first_name="Mohamed",last_name="Ibrahim")



# We can give default parameters too

def greeting(first_name="Afza",last_name="Fateheen"):
    greet="Good Night "+first_name+" "+last_name
    print(greet)

first_name="Mohamed"
last_name="Ibrahim"
greeting()



# Default parameters won't work when wepass arguments to the function

def greeting(first_name="Afza",last_name="Fateheen"):
    greet="Good Night "+first_name+" "+last_name
    print(greet)

first_name="Mohamed"
last_name="Ibrahim"
greeting(first_name,last_name)