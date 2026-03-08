def logof():
	global logo
	logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
	print(logo)
from replit import clear
end = False
contwsnb = False
def add(n1, n2):
	return n1 + n2
def subtract(n1, n2):
	return n1 - n2
def multiply(n1, n2):
	return n1 * n2
def divide(n1, n2):
	return n1 / n2
def power(n1, n2):
	return n1 ** n2
operations = {
			  "+": add, 
			  "-": subtract,
			  "*": multiply,
			  "/": divide,
			  "**": power
			 }
def function(n1, n2):
	if op == add:
		add(n1, n2)
		return add(n1,n2)
	if op == subtract:
		subtract(n1, n2)
		return subtract(n1, n2)
	if op == multiply:
		multiply(n1, n2)
		return multiply(n1, n2)
	if op == divide:
		divide(n1, n2)
		return divide(n1, n2)
	if op == power:
		power(n1, n2)
		return power(n1, n2)
def calculate1():
	global num1, n1
	num1 = float(input("What is the first number? "))
	n1 = num1
def calculate2():
	global answer, operation, num2, n2, op
	for key in operations:
		print(key)
	operation = input("Pick an operation.")
	num2 = float(input("What is the next number? "))
	n2 = num2
	op = operations[operation]
	answer = function(n1,n2)
	print(f"Result is: {n1} {operation} {n2} = {round(answer, 2)}")
	contwsnf()
def contwsnf():
	global contwsn, end, answer, n1
	contwsn = input("Do you want to continue with this result? 'y' or 'n'. Type 'finish' if you want to leave now ")
	if contwsn == "y":
		n1 = answer
		calculate2()
	elif contwsn == "n":
		contwsnb = True
		cont()
	elif contwsn == "finish":
		end = True
		print(("yine bekleriz anam!").title())
def cont():
	global cont, end
	cont = input("Do you want to continue? 'yes' or 'no'.")
	if cont == "yes":
		clear()
		print(logo)
	elif cont == "no":
		end = True
		print(("yine bekleriz anam!").title())
while not end:
	logof()
	calculate1()
	calculate2()
	