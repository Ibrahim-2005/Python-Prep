def student_info(**details):
    print(details)

student_info(name="Ibrahim", roll=42, course="Python", city="Chennai")


# **kwargs lets your function accept any number of keyword arguments that is, arguments passed as key=value pairs.

# It gathers them all up into a dictionary inside the function.