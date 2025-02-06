lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]

# indexing and slicing
print(lst[0])  # abc
print(lst[4:6])  # [62, ['g', 'h', 'i']]

# built-in methods
print(len(lst))  # 6

lst.append(99)  # add 99 to end
lst.remove(62)  # remove 62
lst.pop()  # remove last (99)
lst.pop(2)  # remove 'def'
