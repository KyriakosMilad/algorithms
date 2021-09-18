# challenge from hackerrank https://www.hackerrank.com/challenges/mars-exploration/

message = input('Enter SOS message received: ')
changed_letters = 0

for i in range(0, len(message), 3):
    if message[i] != 'S':
        changed_letters += 1
    if message[i + 1] != 'O':
        changed_letters += 1
    if message[i + 2] != 'S':
        changed_letters += 1

print(changed_letters)
