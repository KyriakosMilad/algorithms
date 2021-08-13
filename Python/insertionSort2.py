# challenge from hackerrank https://www.hackerrank.com/challenges/insertionsort2

def insertion_sort2(arr_size, arr):
    for i in range(1, arr_size):
        current_value = arr[i]
        for j in range(i - 1, -1, -1):
            if current_value < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = current_value
        print(*arr)


insertion_sort2(7, [3, 4, 7, 5, 6, 2, 1])

# [3 4 7 5 6 2 1]
#    ^ ^
