# challenge from hackerrank https://www.hackerrank.com/challenges/designer-pdf-viewer

def int_list(item):
    return int(item)


word = input('Enter the word:')
heights = map(int_list, input('Enter hurdles heights each hurdle separated with ",": ').split(','))
heights = list(heights)

letters = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
    'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25,
}

maximum = 0
for letter in word:
    letter_height = heights[letters[letter]]

    if letter_height > maximum:
        maximum = letter_height

print(maximum * len(word))
