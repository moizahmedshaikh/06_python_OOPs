# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello how are you {self.name}")

class Department:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def show_detailes(self):
        self.name.show()
        print(f"department: {self.department}")

emp1 = Employee("Moiz Ahmed")
dep1 = Department(emp1, "IT")
dep1.show_detailes()