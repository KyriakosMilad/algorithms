# challenge from hackerrank https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

def get_the_reverse(integer):
    string = str(integer)

    maximum = len(string)
    new_string = ''

    for digit in range(maximum - 1, -1, -1):
        new_string += string[digit]

    return int(new_string)


i = int(input('Enter the starting day number: '))
j = int(input('Enter the ending day number: '))
k = int(input('Enter the divisor: '))

counter = 0
for day in range(i, j + 1):
    if abs(day - get_the_reverse(day)) % k == 0:
        counter += 1

print(counter)
