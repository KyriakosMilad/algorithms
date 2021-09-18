# given array, sort this array in selection sort way

def selection_sort(a):
    for i in range(len(a)):
        lowest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[lowest]:
                lowest = j
        if lowest != i:
            temp = a[i]
            a[i] = a[lowest]
            a[lowest] = temp
    print(a)


selection_sort([0, 2, 34, 22, 10, 19, 17])
