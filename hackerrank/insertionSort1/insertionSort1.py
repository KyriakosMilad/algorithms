# challenge from hackerrank https://www.hackerrank.com/challenges/insertionsort1

def insertion_sort1(arr_size, arr):
    current_value = arr[arr_size - 1]
    for j in range(arr_size - 2, -1, -1):
        # print(j, arr[j], arr[j+1])
        if current_value < arr[j]:
            arr[j + 1] = arr[j]
            print(*arr)
            if j == 0:
                arr[0] = current_value
                print(*arr)
        elif current_value >= arr[j]:
            arr[j + 1] = current_value
            print(*arr)
            break
