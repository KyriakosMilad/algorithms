# challenge from hackerrank https://www.hackerrank.com/challenges/sock-merchant

def int_list(item):
    return int(item)


socks = map(int_list, input('Enter socks each sock separated with ",": ').split(','))
socks = list(socks)

colors_pairs = {}
total_pairs = 0

for i in socks:
    if i in colors_pairs:
        colors_pairs[i] += 1
    else:
        colors_pairs[i] = 1

print(colors_pairs)

for i in colors_pairs:
    if colors_pairs[i] % 2 == 0:
        total_pairs += colors_pairs[i] / 2
    else:
        total_pairs += (colors_pairs[i] - 1) / 2
    print(i, total_pairs)
print(int(total_pairs))

