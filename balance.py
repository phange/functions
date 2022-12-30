# name: Gerald Phan
# date: April 15, 2020
# assignment 2 part 3

# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import sys

# Yes, you should iterate over the string and push all opening brackets to the stack. When you encounter a closing bracket, you should pop from the stack and compare the popped bracket with the closing bracket to see if the pair is matched. This will determine if you should keep iterating over the string to check that all pairs are matched or if the string is unbalanced.

# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False


def is_balanced(input_string):
    """Checks whether the input string is balanced.  Returns True if string is balanced, otherwise returns False."""
    # initialize an empty list as the stack
    stack = []

    # iterate over each character in the string
    for i in input_string:
        # if stack is empty and if it starts with a closing bracket, it is unbalanced
        if not stack:
            if i == "}":
                return False
            if i == "]":
                return False
            if i == ")":
                return False

        if i == "{":
            stack.append("{")
        if i == "(":
            stack.append("(")
        if i == "[":
            stack.append("[")
        if i == "]":
            popped = stack.pop()
            if popped is not "[":
                return False
        if i == ")":
            popped = stack.pop()
            if popped is not "(":
                return False
        if i == "}":
            popped = stack.pop()
            if popped is not "{":
                return False

    # if the stack is not empty, then there is {, { or ( inside it, and is unbalanced
    if stack:
        return False

    return True


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))