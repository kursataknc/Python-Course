# TODO: 4- Inheritance - Creating Subclasses

# Inheritance allows us to inherit attributes and methods from a parent class.
# With inheritance, we can create subclasses and get all the functionality of our parent class.
# We can also override or add completely new functionality without affecting the parent class.

# Say that we wanted to create developers and managers.
# Both will have names, pay, and email
# Instead of copying all this code, we can reuse that code by inheriting from Employee.
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee): # This is the child class.
    # We inherited all the attributes and methods from the parent class.
    pass

dev_1 = Developer('Kursat', 'Sipahi', 50000)
dev_2 = Developer('Aziz', 'Nesin', 60000)

# Python first checked the init method in Developer class,
# and it didn't find anything, so it checked the Employee class.

print(dev_1.email)
print(dev_2.email)

print(help(Developer)) # This will print the help for the Developer class.
# This shows the method resolution order.

print(dev_1.pay) # This will print 50000.
dev_1.apply_raise() # This will apply the raise_amt to the pay.
print(dev_1.pay) # This will print 52000.
# --------------------------------------------------------------------------------------
# Sometimes we want to initiate our subclasses with more information than our parent class
# can handle. Let's say we want to create programming language as an attribute but currently
# our Employee class only accepts first-last-pay.

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee): # This is the child class.
    raise_amt = 1.10 # This will override the raise_amt in the parent class.
    def __init__(self, first, last, pay, prog_lang):
    # instead of copy and paste the whole code, we instead use the knit method.
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        # Employee.__init__(self, first, last, pay) works
        # the same. but we use the super() method to call the parent class.

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer('Kursat', 'Sipahi', 50000, 'Python')
dev_2 = Developer('Aziz', 'Nesin', 60000, 'Java')

mgr_1 = Manager('Sultan', 'Sipahi', 90000, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager)) # This will print True.
print(issubclass(Developer, Employee)) # This will print True.

# print(dev_2.prog_lang)
# print(dev_1.email)

# --------------------------------------------------------------------------------------
# Full code:


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
