# challenge from hackerrank https://www.hackerrank.com/challenges/apple-and-orange

def int_list(item):
    return int(item)


s = int(input('Enter the  starting point of Sam\'s house location: '))
t = int(input('Enter the ending location of Sam\'s house location: '))
a = int(input('Enter the location of the Apple tree: '))
b = int(input('Enter the location of the Orange tree: '))
apples = map(int_list, input('Enter the distances at which each apple falls from the tree each apple separated with ",": ').split(','))
oranges = map(int_list, input('Enter the distances at which each orange falls from the tree each orange separated with ",": ').split(','))

answer = [0, 0]

for i in apples:
    if 0 < i <= (t - a) and i >= (s - a):
        answer[0] += 1

for i in oranges:
    if 0 > i >= (s - b) and i <= (t - b):
        answer[1] += 1

print(answer)
