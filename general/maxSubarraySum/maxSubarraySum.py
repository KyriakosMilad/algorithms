# get the maximum sum of consecutive elements in array

def int_list(item):
    return int(item)


items = map(int_list, input('Enter elements each element separated with ",": ').split(', '))
list = list(items)
n = int(input('Enter number of consecutive elements you want to make sum of: '))

max = 0
temp = 0

for i in range(0, n):
    max += list[i]

temp = max

for i in range(n, len(list)):
    temp = temp - list[i - n] + list[i]
    if temp > max:
        max = temp

print(max)
