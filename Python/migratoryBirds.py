# challenge from hackerrank https://www.hackerrank.com/challenges/migratory-birds

def int_list(item):
    return int(item)


birds = map(int_list, input('Enter birds each bird type separated with ",": ').split(','))
birds = list(birds)

each_bird_seen_times = {}
biggest_birds_types = []

for i in birds:
    if i in each_bird_seen_times:
        each_bird_seen_times[i] += 1
    else:
        each_bird_seen_times[i] = 1

counter = 0
for i in each_bird_seen_times:
    print(counter, i, each_bird_seen_times[i])
    if each_bird_seen_times[i] >= counter:
        counter = each_bird_seen_times[i]

for i in each_bird_seen_times:
    print(counter, i, each_bird_seen_times[i])
    if each_bird_seen_times[i] >= counter:
        counter = each_bird_seen_times[i]
        biggest_birds_types.append(i)


most_sighted_bird = max(biggest_birds_types)
for i in biggest_birds_types:
    if i < most_sighted_bird:
        most_sighted_bird = i

print(most_sighted_bird)
