# challenge from hackerrank https://www.hackerrank.com/challenges/breaking-best-and-worst-records

scores = [12, 24, 10, 24]

betterScore = 0
worseScore = 0
bestScore = scores[0]
worstScore = scores[0]

print(scores)

for val in scores:
    if val > bestScore:
        betterScore += 1
        bestScore = val
    if val < worstScore:
        worseScore += 1
        worstScore = val

    print(betterScore, worseScore, bestScore, worstScore)
    lastScore = val

print(betterScore, worseScore)
