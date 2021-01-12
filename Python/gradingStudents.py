# challenge from hackerrank https://www.hackerrank.com/challenges/grading

def int_list(item):
    return int(item)


def next_multiple_of_five(number):
    if number % 5 == 0:
        return number

    for i in range(40, 101, 10):
        if number > i:
            continue
        if i - number > 4:
            return i - 5
        else:
            return i


grades = map(int_list, input('Enter grades each grade separated with ",": ').split(','))
grades = list(grades)

finalGrades = []

for grade in grades:
    if grade >= 38:
        grade_next_multiple_of_five = next_multiple_of_five(grade)

        if (grade_next_multiple_of_five - grade) < 3:
            finalGrades.append(grade_next_multiple_of_five)
        else:
            finalGrades.append(grade)
    else:
        finalGrades.append(grade)

print(finalGrades)
