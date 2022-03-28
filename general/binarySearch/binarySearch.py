# given sorted array and value
# if value exists in the array return it's index if not return -1

def binary_search(array, value):
    l_pointer = 0
    r_pointer = len(array)
    if value < array[0] or value > array[-1]:
        return -1

    while (r_pointer - l_pointer) >= 1:
        index = int((l_pointer + r_pointer) / 2)
        if array[index] == value:
            return index
        elif value < array[index]:
            r_pointer = index - 1
        else:
            l_pointer = index + 1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
