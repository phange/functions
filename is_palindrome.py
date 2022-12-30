# Name: Gerald Phan
# Date: 2/7/20
# Due: 2/12/20
# Description: Project 6c


def is_palindrome(string):
    """Recursive function that checks if a string argument is a palindrome."""
    if string[0] == string[len(string)-1] and len(string) == 2 or len(string) == 1:
        return True
    else:
        if string[0] == string[len(string)-1]:
            return is_palindrome(string[1:-1])  # trim 1st and last character
        else:
            return False


def main():
    print(is_palindrome("string"))
    print(is_palindrome("tacocat"))
    print(is_palindrome("hannah"))
    print(is_palindrome("hannaH"))


if __name__ == '__main__':
    """Runs if the file is run as a script, but not if the file is imported."""
    main()
