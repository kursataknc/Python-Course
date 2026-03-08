def func(*args):
	print(args)
	#You can iterate through the tuple that is given.
	print(args[0])

func(3, 5, 6, 2, 1, 7, 4, 3)

''' As it can be seen in the example above, *args is a method that allows us to give unlimited positional 
arguments to a function as a tuple. '''

''' Likewise, **kwargs is the method that allows us to give arbitrary number of KeyWorded arguments to a function
as a dictionary.'''

def calculate(n, **kwargs):
	print(kwargs)
	for key, value in kwargs.items():
		print(key)
		print(value)
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)

calculate(3, add=3, multiply=4)

class Car:
	def __init__(self, **kw):
		self.make = kw.get("make")
		self.model = kw.get("model")
		self.colour = kw.get("colour")
		self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)

''' As it can be seen in the class example, when we want to give "optional" positional arguments, we can use "get"
module in order not to get a crash in our program as it returns "none" if there is no arguments given into that
keyword.'''


''' Angela's Notes about args and kwargs are below. '''
# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))

# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)


