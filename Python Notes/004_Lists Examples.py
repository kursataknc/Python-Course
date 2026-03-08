courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Art", "Education", "Engineering", "Law"]

print(len(courses))
# Prints out the length of list

print(courses[0])
# Prints out the first item in the list

print(courses[3])
# Prints out the fourth item in the list

print(courses[-1])  # Prints out the last item in the list

print(courses[0:2])  # Prints out the first two items in the list
# First index is included, second index is not

print(courses[1:3])  # Prints out the second and third items in the list

print(courses[:3])  # Prints out the first three items in the list

print(courses[2:])  # Prints out the third and all remaining items in the list

print(courses[-3:])  # Prints out the last three items in the list

print(courses[:])  # Prints out all items in the list

print(courses[::2])  # Prints out every other item in the list

print(courses[::-1])  # Prints out the list in reverse order

print(courses[::-2])  # Prints out the list in reverse order, every other item

courses.append("Art")  # Adds an item to the end of the list

courses.insert(0, "Art History")  # Adds an item to the list at the specified index
# This won't overwrite the first item in the list

courses.insert(0, courses_2)  # Adds the entire list to the list at the specified index
print(courses[0])  # Prints out the list that was added. If we don't need to print out the entire list,
# we can use the extend method instead.

courses.extend(courses_2)  # Adds the entire list to the end of the list

# If we append the list, we will not be able to access the list that was added.
# It would be a list in a list. That's why we use extend.

courses.remove("Art")  # Removes the first item in the list that matches the specified value

courses.pop()  # Removes the last item in the list

popped = courses.pop(0)  # Removes the item at the specified index
print(popped)  # Prints out the item that was removed

courses.reverse()  # Reverses the order of the list

courses.sort()  # Sorts the list in alphabetical order

nums = [1, 2, 3, 4, 5]
courses.sort()  # Sorts the list in alphabetical order
nums.sort()  # Sorts the list in numerical order
print(courses)  # Prints out the sorted list
print(nums)  # Prints out the sorted list

nums = [1, 2, 3, 4, 5]
courses.sort(reverse=True)  # Sorts the list in reverse alphabetical order
nums.sort(reverse=True)  # Sorts the list in reverse numerical order
print(courses)  # Prints out the sorted list
print(nums)  # Prints out the sorted list

sorted(courses)  # Returns a sorted list without modifying the original list
sorted(nums)  # Returns a sorted list without modifying the original list

sorted_courses = sorted(courses)  # Returns a sorted list without modifying the original list
print(sorted_courses)  # Prints out the sorted list

nums = [1, 2, 3, 4, 5]
print(min(nums))  # Prints out the smallest item in the list
print(max(nums))  # Prints out the largest item in the list
print(sum(nums))  # Prints out the sum of all items in the list

courses = ["History", "Math", "Physics", "CompSci"]
print(courses.index("Math"))  # Prints out the index of the first item in the list that matches the specified value
# If the item is not found, it will throw an error

courses = ["History", "Math", "Physics", "CompSci"]
print("Math" in courses)  # Returns True if the item is found in the list, False if not
# This is a good way to check if an item is in a list

courses = ["History", "Math", "Physics", "CompSci"]
for item in courses:
	print(item)  # Prints out each item in the list on a new line
# Item is not a keyword, it is a variable. We can use any name for it.

courses = ["History", "Math", "Physics", "CompSci"]
for index, course in enumerate(courses):
	print(index, course)  # Prints out the index and item in the list on a new line

courses = ["History", "Math", "Physics", "CompSci"]
for index, course in enumerate(courses, start=1):
	pass
# Prints out the index and item in the list on a new line, starting at 1 instead of 0

courses = ["History", "Math", "Physics", "CompSci"]
course_str = ", ".join(courses)  # Joins the list items into a string with the specified separator
print(course_str)  # Prints out the string

course_str = ", ".join(courses)  # Joins the list items into a string with the specified separator
course_list = course_str.split(", ")  # Splits the string into a list with the specified separator
print(course_list)  # Prints out the list

courses = ["History", "Math", "Physics", "CompSci"]
course_str = ", ".join(courses)  # Joins the list items into a string with the specified separator

courses = ["History", "Math", "Physics", "CompSci"]
course_str = ", ".join(courses)
new_list = course_str.split(", ")  # This turns the string into a list. Basically, it is the opposite of join.

# print()
