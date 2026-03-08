# Mutable
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1
print(list_1)
print(list_2)
# This will print the same list

list_1[0] = "Art"
print(list_1)
print(list_2)  # This will print the same list except the "History" will be "Art".

# Immutable
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# This will print the same tuple

tuple_1[0] = "Art"
print(tuple_1)
print(tuple_2)  # This will throw an error because tuples are immutable.
