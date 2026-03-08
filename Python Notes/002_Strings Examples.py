message = "Hello Python World!"

print(len(message))  # len() function returns the length of a string

print(message[0])  # prints the first character of the string

print(message.upper())  # .upper() function returns the string in upper case

print(message.lower())  # .lower() function returns the string in lower case

print(message.capitalize())  # .capitalize() function returns the string with the first character in upper case

print(message[0:5])  # prints the first 5 characters of the string

print(message.count("o"))  # .count() function returns the number of times a character appears in a string

print(message.find("World!"))  # .find() function returns the index of the first occurrence of a character in a string

print(message.find("Universe"))  # .find() function returns -1 if the character is not found

new_message = message.replace("World!", "Universe")  # .replace() function replaces a string with another string
print(new_message)

greeting = "Hello"
name = "Bruce"
message = greeting + " " + name
message = greeting + ", " + name + ". Welcome!"
print(message)  # concatenation

greeting = "Hello"
name = "Bruce"
message = f"{greeting}, {name}. Welcome!"
print(message)  # f-strings

greeting = "Hello"
name = "Bruce"
print(dir(greeting))  # dir() function returns a list of all the methods available for a given object

print(help(str.upper))  # help() function returns a string containing the documentation for the given object
