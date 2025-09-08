class Company:

    class Employee:
        def __init__(self,name,position,salary):
            self.name=name
            self.position=position
            self.salary=salary

    def __init__(self,name):
        self.name=name
        self.employees=[]
    
    def add_employee(self,name,position,salary):
        employee_details=self.Employee(name,position,salary)
        self.employees.append(employee_details)

    def company_details(self):
        print(f"{self.name} company has {len(self.employees)} employees \n")  

    def employee_list(self):
        for employee in self.employees:
            print(f"{employee.name} is working as {employee.position} and getting a salary of Rs.{employee.salary}")

company1=Company("Juspay")

company1.add_employee("Ibrahim","SDE",27000)
company1.add_employee("Afza Fateheen","Front end Developer",17000)
company1.add_employee("Suhail Ahmed","Java Engineer",70000)
company1.add_employee("Raasheed","JDBC",20000)

company1.company_details()

company1.employee_list()