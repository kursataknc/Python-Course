# TODO: 3- classmethods and staticmethods

class Employee:

    nums_of_emps = 0
    raise_amt = 1.09

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.nums_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod # Adding a decorator to the top
    def set_raise_amt(cls, amount):
    # This is altering the functionality of our method to where now we receive
    # the class as our first argument instead of the instance.
    # There's a common convention for class variables "cls" (instead of self)
    # You cannot write "class" because that has a different meaning.
        cls.raise_amt = amount

emp_a = Employee("Jay", "Weinberg", 99999)
emp_b = Employee("Ray", "Luzier", 99999)

# If we want to change that raise amount, we can simply:
Employee.set_raise_amt(1.1)
print(Employee.raise_amt) # This prints 1.1
print(emp_a.raise_amt)  # This prints 1.1
print(emp_b.raise_amt)  # This prints 1.1

# There is something you should be careful:
emp_a.set_raise_amt(1.4)
print(Employee.raise_amt) # This prints 1.4
print(emp_a.raise_amt)  # This prints 1.4
print(emp_b.raise_amt)  # This prints 1.4

# --------------------------------------------------------------------------------------
class Employee:

    nums_of_emps = 0
    raise_amt = 1.09

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = first + "." + last + "@kursat.com"

        Employee.nums_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod # Adding a decorator to the top
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

emp_1 = Employee("Corey", "Taylor", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email) # This will print John.Doe@kursat.com
print(new_emp_1.pay)   # This will print 70000
# --------------------------------------------------------------------------------------
# regularmethods: automatically pass the instance as the first argument and we call that "self".

# classmethods: automatically pass the class as the first argument and we call that "cls"

# staticmethods: don't pass anything automatically, they don't pass the instances or the class.

# Lets say that we wanted a simple function that would take in a date and return whether it is a workday or not.
# We can use a staticmethod to do this.

class Employee:

    nums_of_emps = 0
    raise_amt = 1.09

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = first + "." + last + "@kursat.com"

        Employee.nums_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod # Adding a decorator to the top
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):
    # Python have these weekday methods where Monday is 0 and Sunday is 6 and between.
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Static method should be used if you don't access the instance or the class anywhere
# within the function.

# Say that we have this class method in line 259, we can see that I'm using class variable
# there (cls) but if I wasn't using it anywhere within that method, then it probably
# doesn't need to be a class method and the same with the regular methods.

emp_q = Employee("Corey", "Taylor", 50000)
emp_w = Employee("Test", "User", 60000)

import datetime
my_date = datetime.date(2022, 8, 18) # Thursday is a weekday

print(Employee.is_work_day(my_date))
# --------------------------------------------------------------------------------------
# Final code:
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
