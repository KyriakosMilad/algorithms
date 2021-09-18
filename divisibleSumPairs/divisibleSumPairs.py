# challenge from hackerrank https://www.hackerrank.com/challenges/divisible-sum-pairs

def int_list(item):
    return int(item)


ar = map(int_list, input('Enter elements each element separated with ",": ').split(','))
ar = list(ar)
k = int(input('Enter divisible number: '))

total_pairs = 0

for i in range(len(ar)):
    for j in range(i + 1, len(ar)):
        if (ar[i] + ar[j]) % k == 0:
            total_pairs += 1

print(total_pairs)
