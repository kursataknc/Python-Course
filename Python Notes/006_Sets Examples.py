# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# Sets are unordered and represent with curly braces.
print(cs_courses)  # If you print the set, it will print in a random order.
# Sets are used to remove duplicates.
# If you add a duplicate, it will not add it.

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Physics', 'CompSci', 'Design'}

print(cs_courses.intersection((art_courses)))  # Intersection of two sets.

print(cs_courses.difference(art_courses))  # Difference of two sets.

print(cs_courses.union(art_courses))  # Union of two sets.

print(cs_courses.issubset(art_courses))  # Is cs_courses a subset of art_courses?

print(cs_courses.issuperset(art_courses))  # Is cs_courses a superset of art_courses?

print(cs_courses.isdisjoint(art_courses))  # Are the sets disjoint?

# Empty sets
empty_set = {}  # This is a dictionary!
empty_set = set()
