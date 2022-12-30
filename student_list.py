# name: Gerald Phan
# date: April 15, 2020

# student_list.py
# ===================================================
# Reimplementation of Pythons List
# ===================================================

import numpy as np


# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])

# You may want an internal function that handles resizing the array.
# Dont modify get_list or get_capacity, they are for testing

    def get_list(self):
        """Returns StudentList."""
        return self._list[:self._size]

    def get_capacity(self):
        """Returns StudentList capacity."""
        return self._capacity

    def get_size(self):
        """Returns StudentList size."""
        return self._size

    def get_array(self):
        """Returns the underlying Numpy array."""
        return self._list[:self._size]

    def double_size(self):
        """Makes a new array twice as big as the current, and copies over the data from the current to the new array, sets new array as the current array."""
        # make new array of twice the size as the current
        new_array = np.empty([self._capacity*2], np.int16)
        # copy over the data from the current to the new array
        for data in range(0, self._size-1):
            new_array[data] = self._list[data]

        # sets new array as the current array
        self._list = new_array

        # update current array capacity
        self._capacity = self._capacity * 2

        # update current array size  ## do this outside of this function
        # new_list[self._size] # do this in other functions; this is only to expand the size
        return

    def append(self, val):
        """Appends val at the end of the StudentList."""
        # increase size by 1
        self._size += 1

        # if current capacity is full, call double size function
        if self._size > self._capacity:
            self.double_size()

        # add val at the end of the array
        self._list[self._size-1] = val
        return

    def pop(self):
        """Removes item at the end of the StudentList and returns it."""
        # assign item at end of list to new variable
        last_item = self._list[self._size-1]

        # do not need to remove item explicitly from array, updating size will take care of that.

        # update size
        self._size = self._size - 1

        return last_item

    def insert(self, index, val):
        """Inserts val at the specified index, shifting downward the remaining items by 1 unit, keeping order the same."""

        # if current capacity is full, call double size function
        if self._size == self._capacity:
            self.double_size()

        # shift all data from index downward from by one unit; this one is reversed so new temp list not needed
        for x in range(self._size-1, index-1, -1):
            self._list[x+1] = self._list[x]

        # insert new val at index
        self._list[index] = val

        # increase size by 1
        self._size += 1

        return

    def remove(self, val):
        """Removes the first item from the list whose value is equal to val.  Does not Raise ValueError if there is no such item."""
        # no need to check for resize because the array is getting smaller
        # search for the index where the val exists in the array
        for x in range(0, self._size):
            if self._list[x] == val:
                index = x
                # shift all values to the left
                for i in range(index, self._size-1):
                    self._list[i] = self._list[i+1]
                self._size = self._size - 1
                return

    def clear(self):
        """Removes all items from the list.  Equivalent to del a[:]."""
        for x in range(0, self._size):
            self.pop()

        # self._size = 0
        return

    def count(self, val):
        """Return the number of times val appears in the list."""
        count = 0
        for x in range(0, self._size):
            if self._list[x] == val:
                count = count + 1
        return count

    def get(self, index):
        """Returns value of the list at the specified index."""
        return self._list[index]


def main():
    test_list = StudentList()
    test_list.append(5)
    test_list.append(10)
    test_list.append(3)
    test_list.append(42)
    test_list.append(9)
    print(test_list.get_list())
    test_list.insert(4, 5)  # index, val
    print(test_list.get_list())
    # test_list.remove(9)
    # print(test_list.get_list())
    # test_list.remove(2)
    # print(test_list.get_list())
    # test_list.clear()
    # print(test_list.get_size())
    # print(test_list.get_list())


if __name__ == '__main__':
    """Runs if the file is run as a script, but not if the file is imported."""
    main()
