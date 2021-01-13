# challenge from hackerrank https://www.hackerrank.com/challenges/cats-and-a-mouse

a = int(input('first cat position: '))
b = int(input('second cat position: '))
c = int(input('mouse position: '))

if abs(c-b) > abs(c-a):
    print('Cat A')
elif abs(c-a) > abs(c-b):
    print('Cat B')
else:
    print('Mouse C')
