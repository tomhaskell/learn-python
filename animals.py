# Delcare a class
class Animal:
    # Constructor - uses the built-in __init__ method. The first param is the current instance
    def __init__(self, kind, likes, dislikes):
        # create instance vars
        self.kind = kind  # members are public by default
        self._likes = likes  # Protected - accessible within class and child classes
        self.__dislikes = dislikes  # Private - only accessible within class

    # Destructor - called when an object is deleted
    def __del__(self):
        print('Bye')

    def print_animal(self):
        print(f'{self.kind}, likes: {self._likes}, dislikes: {self.__dislikes}')


# Create an instance of Animal
salty = Animal('Cat', ['sleeping', 'scratching'], ['dogs'])
salty.print_animal()

# Can't access protected or private members outside of the class
try:
    salty.__dislikes
except:
    print('Can\'t acccess private members')

# This will trigger the destructor method
del salty


# Child classes
class Dog(Animal):
    def __init__(self, breed, likes, dislikes):
        self.breed = breed
        Animal.__init__(self, 'Dog', likes, dislikes)

    def print_dog(self):
        print(f'Dog ({self.breed})')

    def speak(self):
        print('Woof!')


# Create an instance of Dog
pepper = Dog('Labrador', ['walks', 'fetch'], ['cats', 'postman'])
pepper.print_animal()
pepper.print_dog()

# Polymorphism


class Lion(Animal):
    def __init__(self):
        Animal.__init__(self, 'Lion', [], [])

    # class methods can have the same name as another class
    def speak(self):
        print('ROAR!')


simba = Lion()

for pet in (pepper, simba):
    pet.speak()
