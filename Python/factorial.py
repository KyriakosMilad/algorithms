# challenge from hackerrank https://www.hackerrank.com/challenges/extra-long-factorials

n = int(input('enter starter number: '))

current_number = n
next_number = n - 1
total = 1

for i in range(n, 1, -1):
    total = current_number * next_number * total
    current_number = current_number - 2
    next_number = next_number - 2
    if next_number == 0 or current_number == 0:
        break

print(total)
