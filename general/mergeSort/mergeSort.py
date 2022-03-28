# given array, sort this array in merge sort way

def merge_sorted_arrays(arr1, arr2):
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    return merge_sorted_arrays(left, right)


print(merge_sort([4, 100, 3]))
