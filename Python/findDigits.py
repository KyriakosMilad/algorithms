# challenge from hackerrank https://www.hackerrank.com/challenges/find-digits

n = input('Enter the number: ')
n_integer = int(n)

total = 0

for i in n:
    if int(i) != 0 and n_integer % int(i) == 0:
        total += 1

print(total)
