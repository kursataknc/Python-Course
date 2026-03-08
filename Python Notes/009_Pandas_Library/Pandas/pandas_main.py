import pandas
data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)


print(sum(temp_list) / len(temp_list))


#   Get Data in Columns
print(data["condition"])
print(data.condition)
data["temp"].max()

#   Get Data in Row
#   sunday = data[data.temp == data["temp"].max()] # The row that where the temperature is maximum.

print(sunday.condition)

#   Create a dataframe from scratch

data_dict = {
		"students": ["Amy", "James", "Angela"],
		"scores": [76, 56, 65]
			}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



