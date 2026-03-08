travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
country_name = input("country name: ")
visits_made = input("visits_made: ")
city_names = input("city names: ")


def add_new_country(country_name, visits_made, city_names):
    new_dict = {"country": country_name, "visits": visits_made, "cities": city_names.split(" ")}
    travel_log.append(new_dict)


add_new_country(country_name, visits_made, city_names)
print(travel_log)
