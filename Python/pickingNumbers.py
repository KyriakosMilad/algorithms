# challenge from hackerrank https://www.hackerrank.com/challenges/picking-numbers

def int_list(item):
    return int(item)


arr = map(int_list, input('Enter the numbers each number separated with ",": ').split(','))
arr = list(arr)

arr.sort()
elements = {}
longest = 0

for i in arr:
    if i in elements:
        elements[i] += 1
    else:
        elements[i] = 1

last_key = list(elements.keys())[0]

for index, (key, value) in enumerate(elements.items()):
    if index == 0:
        continue
    else:
        if abs(key - last_key) <= 1:
            if longest < (elements[key] + elements[last_key]):
                longest = elements[key] + elements[last_key]

    last_key = key

longest_value = elements[max(elements, key=elements.get)]
if longest == 0 or longest_value > longest:
    longest = longest_value

print(longest)
