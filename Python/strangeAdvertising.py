# challenge from hackerrank https://www.hackerrank.com/challenges/strange-advertising

n = int(input('Enter the day number to report: '))

total = 0
people = 5
for i in range(n):
    new_people = people // 2
    total += new_people
    people = new_people * 3

print(total)
