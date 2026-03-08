# TODO: 2- Class Variables

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@kursat.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

'''
 Instead of 1.04, you can write to the top raise_amount = 1.04. and write
 self.raise_amount.
'''
emp_1 = Employee("Corey", "Taylor", 50000)
emp_2 = Employee("Test", "User", 60000)

# emp_1.apply_raise()
# print(emp_1.pay) # This will print 52000.

# print(Employee.raise_amount) # This will print 1.04.
# print(emp_1.raise_amount) # This will print 1.04.
# print(emp_2.raise_amount) # This will print 1.04.

print(emp_1.__dict__) # This will print the dictionary of the instance.
# There is no raise_amount key in the dictionary.
print(Employee.__dict__) # This will print the dictionary of the class.
# There is raise_amount attribute, we can access that from our instances.

Employee.raise_amount = 1.05 # This will change the raise_amount for all instances.
emp_1.raise_amount = 1.06 # This will change the raise_amount for only emp_1.
# The important thing is that self.raise_amount lets us change the raise_amount for a single instance.

# --------------------------------------------------------------------------------------
class Employee:

    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@kursat.com"
        Employee.number_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.number_of_employees) # This will print 0.
emp_1 = Employee("Corey", "Taylor", 50000)
emp_2 = Employee("Test", "User", 60000)
print(Employee.number_of_employees) # This will print 2.

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
