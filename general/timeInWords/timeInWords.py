# challenge from hackerrank https://www.hackerrank.com/challenges/the-time-in-words

def to_string(*args):
    word = ''
    for i in args:
        word = word + ' ' + str(i)

    return word.strip()


h = int(input('Enter the hour of the day: '))
m = int(input('Enter the minutes after the hour: '))

numbersInWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

if m == 0:
    print(to_string(numbersInWords[h], "o' clock"))

elif m == 1:
    print(to_string("one minute past", numbersInWords[h]))

elif m == 59:
    print(to_string("one minute to", numbersInWords[(h % 12) + 1]))

elif m == 15:
    print(to_string("quarter past", numbersInWords[h]))

elif m == 30:
    print(to_string("half past", numbersInWords[h]))

elif m == 45:
    print(to_string("quarter to", (numbersInWords[(h % 12) + 1])))

elif m <= 30:
    print(to_string(numbersInWords[m], "minutes past", numbersInWords[h]))

elif m > 30:
    print(to_string(numbersInWords[60 - m], "minutes to", numbersInWords[(h % 12) + 1]))
