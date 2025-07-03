age = int(input("Enter age: "))
if age >= 18:
    nationality = input("Are you Indian? (yes/no): ")
    if nationality.lower() == "yes":
        print("You can vote!")
    else:
        print("You must be an Indian citizen to vote.")
else:
    print("You are too young to vote.")
