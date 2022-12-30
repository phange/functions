def insertsort_ascending(array):
    """
    Insertion sort using recursion.
    :param array:
    :return:
    1. Call first element of the array "sorted"
    2. Repeat until all elements are sorted:
        Look at next unsorted element.  Insert into the "sorted" position by shifting the requisite number of elements.
    """

    for i in range(1, len(array)):

        key = array[i]

        j = i - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

    return array
