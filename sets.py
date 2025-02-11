# A set is an immutable, unordered collection of unique elements that can consist of integers,
# floats, strings and tuples. However, sets cannot hold mutable elements such as lists, sets or
# dictionaries.
set1 = {'Jenny', 26, 'Parker', 10.5}
print(set1)  # prints {10.5, 26, 'Jenny', 'Parker'}

# Create a set from a list - this will remove duplicates
lst = ['Jenny', 26, 'Parker', 'Parker', 10.5]
set2 = set(lst)
print(set2)  # prints {10.5, 26, 'Jenny', 'Parker'}

# Sets do not have indexes or keys. We can use `in` to check to see if the element exists
print('Parker' in set1)  # True

# Built in methods
set1.add('George')

# Update - takes in any iterable object and adds to an existing set
students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}

students1.update(students2)
# {'Dmitry', 'Amy', 'Bridgette', 'Lily', 'Jane', 'Zhuo', 'Chau', 'Carlos', 'Alice'}
print(students1)

# Union - similar to `update`, but returns the new set rather than modifying
students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}

students3 = students1.union(students2)
print(students1)  # {'Dmitry', 'Amy', 'Bridgette', 'Chau', 'Carlos', 'Jane'}
# {'Dmitry', 'Amy', 'Bridgette', 'Lily', 'Jane', 'Zhuo', 'Chau', 'Carlos', 'Alice'}
print(students3)

# Removing elements
students3.remove('Bridgette')

# for loops
for student in students3:
    print('Hello', student)
