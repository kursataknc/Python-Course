MENU = {
	"espresso": {
		"ingredients": {
			"water": 50,
			"coffee": 18,
			"milk": 0
		},
		"cost": 1.5,
	},
	"latte": {
		"ingredients": {
			"water": 200,
			"milk": 150,
			"coffee": 24,
		},
		"cost": 2.5,
	},
	"cappuccino": {
		"ingredients": {
			"water": 250,
			"milk": 100,
			"coffee": 24,
		},
		"cost": 3.0,
	}
}

resources = {
	"water": 300,
	"milk": 200,
	"coffee": 100,
}

end_game = False
money_inp = 0
vault = 0


def check_report():
	global resources, money_inp, prompt
	print(f"{resources['water']} ml of water")
	print(f"{resources['milk']} ml of milk")
	print(f"{resources['coffee']} g of coffee")
	print(f" ${vault}")


def insert_coin():
	global quarters, dimes, nickels, pennies, money_inp
	quarters = int(input("How many quarters?"))
	dimes = int(input("How many dimes?"))
	nickels = int(input("How many nickels?"))
	pennies = int(input("How many pennies?"))
	money_inp += (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
	money_inp = round(money_inp, 2)


def check_change():
	global cost, in_change, money_inp, sorry
	if money_inp >= cost:
		return True
	else:
		return False


def check_resources():
	global resources, MENU, prompt, cost, ingredient, end_game, money_inp
	if prompt == "espresso":
		if resources["water"] >= ing_water and resources["coffee"] >= ing_coffee:
			return True
	elif prompt == "latte":
		if resources["water"] >= ing_water and resources["milk"] >= ing_milk and resources["coffee"] >= ing_coffee:
			return True
	elif prompt == "cappuccino":
		if resources["water"] >= ing_water and resources["milk"] >= ing_milk and resources["coffee"] >= ing_coffee:
			return True
	else:
		return False


while not end_game:
	prompt = input("What would you like? 'espresso', 'latte' or 'cappuccino'")
	if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
		ing_water = MENU[prompt]["ingredients"]["water"]
		ing_milk = MENU[prompt]["ingredients"]["milk"]
		ing_coffee = MENU[prompt]["ingredients"]["coffee"]
		res_water = resources["water"]
		res_milk = resources["milk"]
		res_coffee = resources["coffee"]
		cost = MENU[prompt]['cost']
		if check_resources():
			insert_coin()
			check_change()
			in_change = money_inp - cost
			if check_change():
				vault += cost
				print(f"Here is ${round(in_change, 2)} in change.")
				print(f"Here is your {prompt}. Enjoy!")
				resources["water"] -= ing_water
				resources["milk"] -= ing_milk
				resources["coffee"] -= ing_coffee
				money_inp = 0
			elif not check_change():
				money_inp = 0
				print(f"Sorry, you need ${round((-in_change), 2)} more. Money Refunded.")
		else:
			print(f"Sorry there is not enough water.")
	elif prompt == "report":
		check_report()
	elif prompt == "off":
		break
