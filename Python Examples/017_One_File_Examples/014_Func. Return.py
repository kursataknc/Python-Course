def is_leap(year):
	leap = True
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				leap = True
			else:
				# print("Not leap year.")
				leap = False
		else:
			leap = True
	else:
		leap = False
	return leap


def days_in_month(year, month):
	if month > 12 or month < 1:
		return "Invalid Month!"
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if is_leap(year):
		day = month_days[month - 1]
		if month == 2:
			day = 29
	else:
		day = month_days[month - 1]
	return day


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
