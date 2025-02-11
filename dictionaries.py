# Dictionaries contain key-value pairs.
# The values can hold and be a mix of different data types, including lists or even nested dictionaries.
# Keys must be an immutable data type such as strings, numbers or tuples.

groceries = {'fruits': ['mangoes', 'bananas', 'kiwis'],
             'protein': ['beef', 'pork', 'salmon'],
             'carbs': ['rice', 'pasta', 'bread'],
             'veggies': ['lettuce', 'cabbage', 'onions']}

# Accessing values
print(groceries['carbs'])  # ['rice', 'pasta', 'bread']

# .update() dictionary arg used to update the underlying dictionary. New keys are inserted, existing
# ones are overwritten
groceries.update({
    'fruits': ['bananas', 'apples', 'pears'],
    'drinks': ['coffee', 'juice']
})

groceries.keys()
groceries.values()
