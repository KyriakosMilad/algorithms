# challenge from hackerrank https://www.hackerrank.com/challenges/cut-the-sticks

def int_list(item):
    return int(item)


arr = map(int_list, input('Enter elements each element separated with ",": ').split(','))
arr = list(arr)

answer = []

while True:
    arr = [value for value in arr if value != 0]

    if len(arr) == 0:
        break

    shortest = min(arr)
    answer.append(len(arr))

    for idx, val in enumerate(arr):
        arr[idx] = val - shortest

print(answer)
