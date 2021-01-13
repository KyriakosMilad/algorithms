# challenge from hackerrank https://www.hackerrank.com/challenges/ctci-making-anagrams

s1 = input('Enter first word: ')
s2 = input('Enter second word: ')

s1_encoded = {}
s2_encoded = {}

characters_deleted = 0

for i in s1:
    if i in s1_encoded:
        s1_encoded[i] += 1
    else:
        s1_encoded[i] = 1

for i in s2:
    if i in s2_encoded:
        s2_encoded[i] += 1
    else:
        s2_encoded[i] = 1

for i in s1_encoded:
    if i not in s2_encoded:
        characters_deleted += s1_encoded[i]

for i in s2_encoded:
    if i not in s1_encoded:
        characters_deleted += s2_encoded[i]
    else:
        characters_deleted += abs(s1_encoded[i] - s2_encoded[i])

print(characters_deleted)
