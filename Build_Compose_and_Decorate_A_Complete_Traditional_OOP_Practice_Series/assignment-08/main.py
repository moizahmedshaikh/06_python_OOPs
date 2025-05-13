# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self,subject, name):
        self.subject = subject
        super().__init__(name)


teacher1 = Teacher("English", "Moiz")
print(teacher1.name, teacher1.subject)
teacher1 = Teacher("Islamiat", "Ahmed")
print(teacher1.name, teacher1.subject)