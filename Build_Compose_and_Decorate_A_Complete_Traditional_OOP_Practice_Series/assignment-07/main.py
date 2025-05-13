# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and documen

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          
        self._salary = salary       
        self.__ssn = ssn           

emp1 = Employee("Moiz", 15000, 123456789)

print("Public (name):", emp1.name)            
print("Protected (_salary):", emp1._salary)
print("Private (__ssn):", emp1._Employee__ssn) 
