import random

value = random.random()  # This prints out a random float number between 0 and 1
value1 = random.uniform(1, 10)  # This prints out a random float number between 1 and 10
value2 = random.randint(1,10)  # This prints out a random integer number between 1 and 10 (both included in the numbers)

greetings = ["Hello", "Hi", "Greetings", "Good morning", "Good afternoon", "Good evening"]
value3 = random.choice(greetings)  # This prints out a random element from the list

colors = ["red", "green", "blue", "yellow", "orange", "purple", "cyan", "magenta"]
value4 = random.choices(colors, k=3)  # This prints out 3 random elements from the list

colors2 = ["red", "green", "blue", "yellow", "orange", "purple", "cyan", "magenta"]
value5 = random.choices(colors, weights=[1, 2, 3, 3, 4, 6, 5, 3],
                        k=3)  # This prints out 3 random elements from the list and
# the probability of each element is defined by the weights list.

deck = list(range(1, 53))  # This creates a list with the numbers from 1 to 52
random.shuffle(deck)  # This shuffles the list "deck"
# This method won't work with the choices method. Instead of that, we can use the sample method.

hand = random.sample(deck, k=5)  # This prints out 5 random elements from the list "deck"
# This method won't give you the same elements, each time it will be unique cards.

first_names = ["John", "Jane", "Mary", "Bob", "Tom", "Jack", "Jill"]
last_names = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller", "Wilson"]
street_names = ["Main", "Second", "Third", "Fourth", "Fifth"]
fake_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"]
states = ["California", "Texas", "New York", "Florida", "Illinois"]
for num in range(100):
	first = random.choice(first_names)
	last = random.choice(last_names)
	phone = f'{random.randint(100, 999)}-555-{random.randint(1000, 9999)}'
	street_num = random.randint(100, 999)
	street = random.choice(street_names)
	city = random.choice(fake_cities)
	state = random.choice(states)
	zip_code = random.randint(10000, 99999)
	address = f'{street_num} {street} St., {city} {state} {zip_code}'
	email = first.lower() + '.' + last.lower() + '@gmail.com'
	print(f'{first} {last} - {phone} - {address} - {email}')

print(hand)
