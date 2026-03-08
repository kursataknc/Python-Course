# Arithmetic operations
# Addition:        3 + 2 = 5
# Subtraction:     3 - 2 = 1
# Multiplication:  3 * 2 = 6
# Division:        3 / 2 = 1.5
# Floor Division:  3 // 2 = 1
# Modulus:         3 % 2 = 1
# Exponent:        3 ** 2 = 9

num = 1
num += 5
print(num)  # 6

num = 1
num *= 5
print(num)  # 5

print(abs(-5))  # Absolute value of -5 is 5
print(round(3.7))  # Round 3.7 to 4.0
print(round(3.75, 1))  # Round 3.75 to 3.8

# Comparison operators
# Equal:           3 == 2
# Not Equal:       3 != 2
# Greater Than:    3 > 2
# Less Than:       3 < 2
# Greater Than or Equal: 3 >= 2
# Less Than or Equal:    3 <= 2

num_1 = 3
num_2 = 2
print(num_1 == num_2)  # False

num_1 = 3
num_2 = 2
print(num_1 != num_2)  # True

num_1 = 3
num_2 = 2
print(num_1 > num_2)  # True

num_1 = 3
num_2 = 2
print(num_1 <= num_2)  # False

num_1 = "123"
num_2 = "123"
print(num_1 + num_2)  # "123123"

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)  # 246
