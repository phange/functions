def mergesort_ascending(array):
    """Returns array using recursion.
    1. Sort left half of array.  Both halves don't have to be equal size.
    2. Sort right half of array.
    3. Merge halves together.
    """

    if len(array) > 1:

        middle = len(array)//2  # find middle
        right = array[:middle]  # set right half
        left = array[middle:]  # set left half

        # recursive call
        mergesort_ascending(left)
        mergesort_ascending(right)
        # set counters for two halves
        i = 0  # for left
        j = 0  # for right
        k = 0  # for main array

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        return array

    else:
        return array