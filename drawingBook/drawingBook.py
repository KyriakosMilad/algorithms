# challenge from hackerrank https://www.hackerrank.com/challenges/drawing-book

n = int(input('Enter total book pages: '))
p = int(input('Enter wanted page: '))

print(min(p // 2, n // 2 - p // 2))
