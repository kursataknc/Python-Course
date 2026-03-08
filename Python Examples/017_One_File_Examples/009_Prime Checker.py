import math


def prime_checker(number):
	prime = True
	for x in range(3, int(math.sqrt(number)) + 1, 2):
		if number % x == 0:
			prime = False
			print(x)
			break
	if number % 2 == 0 and number != 2:
		prime = False
	if prime:
		print("It's a prime number.")
	else:
		print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
