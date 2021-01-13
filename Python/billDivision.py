# challenge from hackerrank https://www.hackerrank.com/challenges/bon-appetit

def int_list(item):
    return int(item)


bill = map(int_list, input('Enter bill items each item separated with ",": ').split(','))
bill = list(bill)
k = int(input('Enter index of element anna does not eat: '))
b = int(input('Enter the amount of money that Anna contributed to the bill: '))

del bill[k]

if (sum(bill) / 2) == b:
    print('Bon Appetit')
else:
    print(int(abs((sum(bill) / 2) - b)))
