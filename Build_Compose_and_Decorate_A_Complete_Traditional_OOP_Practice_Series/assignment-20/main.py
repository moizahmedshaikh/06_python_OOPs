# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older to proceed.")
    else:
        print("Access Granted")

try:
    check_age(17)
except InvalidAgeError as e:
    print("Caught an exception:", e)

