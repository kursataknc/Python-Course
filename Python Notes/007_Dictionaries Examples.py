student = {'name': 'John', 'age': '21', 'course': 'Python'}
print(student['name'])  # Prints John

student = {1: 'John', 2: '21', 3: 'Python'}
print(student[2])  # Prints 21

student = {'name': 'John', 'age': '21', 'course': 'Python'}
print(student.get('name'))  # Prints John
print(student.get('name2', 'Not found'))  # Prints out for the keys doesnt exist: Not found

student = {'name': 'John', 'age': '21', 'course': 'Python'}
student['phone'] = '555-555-5555'  # Adds a new key-value pair
student['name'] = 'Jane'  # Updates the value for the existing key
# If you print this, you'll see that the value for the 'name' key has changed and phone added

student = {'name': 'John', 'age': '21', 'course': 'Python'}
student.update({'name': 'Jane', 'phone': '555-555-5555'})  # Updates the value for the existing key

student = {'name': 'John', 'age': '21', 'courses': ['Python', 'Java']}
del student['age']  # Deletes the key-value pair

student = {'name': 'John', 'age': '21', 'course': 'Python'}
age = student.pop('age')  # Removes the key-value pair and returns the value
print(student)  # Prints {'name': 'John', 'course': 'Python'}
print(age)  # Prints 21

student = {'name': 'John', 'age': '21', 'course': 'Python'}
print(len(student))  # Prints 3
print(student.keys())  # Prints out all the keys: ['name', 'age', 'course']
print(student.values())  # Prints out all the values: ['John', '21', 'Python']
print(student.items())  # Prints out all the key-value pairs: [('name', 'John'), ('age', '21'), ('course', 'Python')]

student = {'name': 'John', 'age': '21', 'course': 'Python'}
for key in student:
	print(key)  # Prints out all the keys: name, age, course

student = {'name': 'John', 'age': '21', 'course': 'Python'}
for key, value in student.items():
	print(key, value)  # Prints out all the key-value pairs: name John, age 21, course Python
