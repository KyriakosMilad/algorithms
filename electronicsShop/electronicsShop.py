# challenge from hackerrank https://www.hackerrank.com/challenges/electronics-shop

def int_list(item):
    return int(item)


keyboards = map(int_list, input('Enter keyboards each keyboard type separated with ",": ').split(','))
keyboards = list(keyboards)
drives = map(int_list, input('Enter drives each drive type separated with ",": ').split(','))
drives = list(drives)
budget = int(input('Enter total budget: '))

can_buy = []

for k in keyboards:
    for d in drives:
        if d + k <= budget:
            can_buy.append(d+k)


if len(can_buy) > 0:
    print(max(can_buy))
else:
    print(-1)
