# TODO: 1- Classes and Instances
# Classes are blueprints for objects.
# Instances are objects created from a class.
# Instance variables and class variables are different things.

class Employee:
    pass # In this statement, Python will know that you just want to skip that for now.

emp_1 = Employee()
emp_2 = Employee()

print(emp_1) # This will print the memory address of the object.
print(emp_2) # This will print the memory address of the object.
# These are employee objects and they are both unique.
# --------------------------------------------------------------------------------------
# Instance variables contain data that is unique to each instance.
# Now we could manually create instance variables for each employee by doing this:
emp_1.first = "Corey"
emp_1.last = "Taylor"
emp_1.email = "corey.taylor@kursat.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "kursat.aknc@corey.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
# You can see it's a lot of code and it's also prone to mistakes.
# --------------------------------------------------------------------------------------
# This is where class variables come in.
# To make these set up automatically, we can use the __init__() method.

class Employee:
    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = first + "." + last + "@kursat.com"

emp_1 = Employee("Dave", "Grohl", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.email) # This prints the email of the first employee.
print(emp_2.email) # This prints the email of the second employee.

print("{} {}".format(emp_1.firstname, emp_1.lastname))

print(emp_1.firstname) # This prints the first name of the first employee.
# This is an alternate way to show the names but it's not the best way.

# --------------------------------------------------------------------------------------
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@kursat.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)
# Each method within a class, automatically takes the instance as the first argument.
# This is known as self.

emp_1 = Employee("Corey", "Taylor", 50000)

print(emp_1.fullname())
# Notice that we need parentheses there because this is a method instead of an attribute.
# If we delete the parentheses, we get:
# <bound method Employee.fullname of <__main__.Employee object at 0x00000260573AFEE0>>
# You can see that it prints the method instead of the attribute.

# --------------------------------------------------------------------------------------
# Final code:

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
