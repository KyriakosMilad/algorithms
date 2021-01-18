# challenge from hackerrank https://www.hackerrank.com/challenges/angry-professor

def int_list(item):
    return int(item)


a = map(int_list, input('Enter the arrival times of the students each student separated with ",": ').split(', '))
a = list(a)
k = int(input('Enter the threshold number of students: '))

counter = 0
for i in a:
    if i <= 0:
        counter += 1
        print(k, counter)
        if counter == k:
            print('NO')
            break

print('YES')
