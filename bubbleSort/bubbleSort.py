# challenge from hackerrank https://www.hackerrank.com/challenges/ctci-bubble-sort

def bubble_sort(a):
    count = 0
    for i in a:
        current_count = count
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                count += 1
        # check if the array sorted stop the loop
        if current_count == count:
            break
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
