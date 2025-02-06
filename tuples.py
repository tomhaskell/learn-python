# Tuples are like immutable lists, making them more efficient

tpl = ('abc', 123, 'def', 456)

# Tuples _can_ hold 1 item, if followed  by a comma
tpl_single = ('ghi',)

# Can be accessed in the same way as lists
print(tpl[0])  # abc
print(tpl[1:3])  # (123,'def)

print(len(tpl))  # 4

# Min/Max - find lowest/highest value. Only works if tuple is all same type. For strings, returns
# first/last element if sorted alphabetically
my_tuple = (65, 2, 88, 101, 25)
print(max(my_tuple))  # returns 101

my_tuple = ('orange', 'blue', 'red', 'green')
print(min(my_tuple))  # returns "blue"

try:
    my_tuple = ('abc', 234, 567, 'def')
    max(my_tuple)  # throws an error!
except:
    print("can't use min/max on mixed tuple!")


tpl = ('abc', 123, 'def', 'abc', 456, 456)
# Index - find the (first) index of
print(tpl.index('abc'))  # 0
print(tpl.count(456))  # 2
