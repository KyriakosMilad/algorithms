# get the longest word in the text

txt = input('enter ur text: ')

longest = 0
longestWord = ''
txtWords = txt.split(' ')

for word in txtWords:
    wordLetters = list(word)
    if len(wordLetters) > longest:
        longest = len(wordLetters)
        longestWord = word

print(longestWord)
