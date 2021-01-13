# challenge from hackerrank https://www.hackerrank.com/challenges/breaking-best-and-worst-records

def int_list(item):
    return int(item)


scores = map(int_list, input('Enter scores each score separated with ",": ').split(', '))
scores = list(scores)

betterScore = 0
worseScore = 0
bestScore = scores[0]
worstScore = scores[0]

for val in scores:
    if val > bestScore:
        betterScore += 1
        bestScore = val
    if val < worstScore:
        worseScore += 1
        worstScore = val

    lastScore = val

print(betterScore, worseScore)
