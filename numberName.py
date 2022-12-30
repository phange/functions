# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions."""
    pass


class OutOfRangeError(Exception):
    """Define a new error (non built in) that inherits from Exception"""
    pass

def numberName():

    # Try block includes code that might raise an exception
    try:
        user_integer = input("Please input an integer including and between 1 and 3:")
        if user_integer == 1:
            print("one")
        if user_integer == 2:
            print("two")
        if user_integer == 3:
            print("three")
        else:
            raise OutOfRangeError
    except OutOfRangeError:
        print("That's not one of the allowed values!")
        print()

    return user_integer

test = numberName()
print(test)