# creating a test file
# 1) import unittest
# 2) import module that contains functions or classes you want to test
# 3) create a class that inherits from unittest.TestCase.
# Inside that class, define your test functions, using whatever assertions are appropriate.
# 4) Finally, add a main function that runs "unittest.main()"

import unittest
import mult3

class Test(unittest.TestCase):
    """Contains unit tests for the mult3 function."""
    def test_NotAlmostEqual(self):
        """tests to see if a and b are equal to n decimal places"""

    def test_NotEqual(self):
        """tests to see if a and b are not equal"""

    def test_NotIn(self):
        """tests to see if a is not in b"""


    def test_False(self):
        """tests to see if p is not true"""


if __name__ == '__main__':
    unittest.main()

# import unittest
# from listfuncs import list_max
#
#
# class TestListMax(unittest.TestCase):  # The class name can be whatever you want
#     """
#     Contains unit tests for the listMax function
#     """
#
#     def test_1(self):  # The function names also can be whatever you want
#         a_list = [6, 43, 18, 100, 9, 85]
#         result = list_max(a_list)
#         self.assertEqual(result, 100)
#
#     def test_2(self):
#         a_list = [-7, -1, -38, -2, -99]
#         result = list_max(a_list)
#         self.assertEqual(result, -1)
#
#     def test_3(self):
#         a_list = [-3, 7, 96, -102, 58, 14, -8]
#         result = list_max(a_list)
#         self.assertEqual(result, 96)
#
#     def test_4(self):
#         a_list = [9]
#         result = list_max(a_list)
#         self.assertEqual(result, 9)
#
#
# if __name__ == '__main__':
#     unittest.main()