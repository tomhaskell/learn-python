# main function - In Python, we frequently use the main() function to define the starting point of
# our program. Including the main() function allows us to import and run this program in another
# script.
def main():
    # get user input
    name = input("Who're you? ")
    # print output - auto adds spaces
    print('Hello', name, '!')
    # print using string literals - start the argument with an `f` & use {} to insert an expression
    print(f'Hello, {name.upper()}!')

    # declaring vars
    value = 32.1
    # cast to a string
    temperature = str(value)
    # print var type
    print(type(temperature))  # prints str

    # Data structures
    data = {'a': 3,
            'b': 27,
            'c': 4}

    myBool = True  # bools are capitalised

    # Maths
    x = 4
    y = 3

    x + y  # returns 7
    x - y  # returns 1
    x * y  # returns 12
    x ** y  # exponent - returns 64
    x / y  # returns 1.333
    x // y  # floor divide - returns 1
    x % y  # returns 1

    # logical operators - 'and', 'or', 'not'
    print(x > 2 and not y < 1)  # True

    # if, elif, else
    if x + y < 4:
        print('less than 4')
    elif x + y < 10:
        print('less than 10')
    else:
        print('wooo, big number!')

    # for loops
    for i in range(5):  # 0-4
        print('we can loop', i)

    for name in ['Tom', 'Dick', 'Harry']:
        print('in different ways, ', name)

    # while
    i = 1
    while i < 6:
        print('and in a while', i)
        i += 1

    # error handling
    nums = ['a', 'b', 'c']

    try:
        print(sum(nums))
    except:
        print('Error during sum')
    finally:  # optional
        print('Better luck next time!')

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # input list
    nums_plus_1 = list(  # create a list from...
        map(  # for each item in input list
            lambda x: x+1,  # lambda func - add 1
            nums
        )
    )
    print(nums_plus_1)


# This basically checks whether the program is being run independently as the primary module or as a
# library in another script.
if __name__ == '__main__':
    main()
