# challenge from hackerrank https://www.hackerrank.com/challenges/kangaroo


first_kangaroo_position = int(input('Enter first kangaroo position: '))
first_kangaroo_velocity = int(input('Enter first kangaroo velocity '))
second_kangaroo_position = int(input('Enter second kangaroo position: '))
second_kangaroo_velocity = int(input('Enter second kangaroo velocity '))

result = 'NO'

if first_kangaroo_position == second_kangaroo_position and first_kangaroo_velocity != second_kangaroo_velocity:
    print(result)
else:
    for i in range(0, 10000):
        if first_kangaroo_position == second_kangaroo_position:
            print('YES')

        first_kangaroo_position += first_kangaroo_velocity
        second_kangaroo_position += second_kangaroo_velocity

print(result)

