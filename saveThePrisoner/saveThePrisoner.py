# challenge from hackerrank https://www.hackerrank.com/challenges/save-the-prisoner

n = int(input('Enter the number of prisoners: '))
m = int(input('Enter the number of sweets: '))
s = int(input('Enter the chair number to begin passing out sweets from: '))

counter = 0
chair = s

for i in range(1, m):
    if chair == n:
        chair = 1
    else:
        chair += 1

print(chair)

# better solution
print(((s + m - 2) % n) + 1)
