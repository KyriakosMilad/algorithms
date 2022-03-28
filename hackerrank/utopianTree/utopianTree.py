# challenge from hackerrank https://www.hackerrank.com/challenges/utopian-tree

n = int(input('Enter periods:'))

height = 1

for i in range(n):
    if i % 2 == 0:
        height *= 2
    else:
        height += 1

    print(height)

print(height)
