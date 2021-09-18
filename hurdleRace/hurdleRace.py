# challenge from hackerrank https://www.hackerrank.com/challenges/the-hurdle-race

def int_list(item):
    return int(item)


hurdles = map(int_list, input('Enter hurdles heights each hurdle separated with ",": ').split(','))
hurdles = list(hurdles)

k = int(input('Enter value player can jump:'))

maximum = 0
for i in hurdles:
    if k < i and (i - k) > maximum:
        maximum = i - k

print(maximum)
