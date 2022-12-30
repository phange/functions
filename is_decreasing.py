# Name: Gerald Phan
# Date: 2/7/20
# Due: 2/12/20
# Description: Project 6b


def is_decreasing(list_of_numbers):
    """Recursive function that takes a list of numbers and returns True if the elements of the list are strictly decreasing, but return False otherwise."""
    if len(list_of_numbers) <= 1 or len(list_of_numbers) == 2 and list_of_numbers[0] >= list_of_numbers[1]:
        return True
    else:
        if list_of_numbers[0] > list_of_numbers[1]:
            return is_decreasing(list_of_numbers[1::])  # must return a function call with modified argument
        else:
            return False


def main():
    # list_of_numbers = [1, 3]
    list_of_numbers = [5, 4, 3, 2, 1, ]
    print(is_decreasing(list_of_numbers))


if __name__ == '__main__':
    """Runs if the file is run as a script, but not if the file is imported."""
    main()
