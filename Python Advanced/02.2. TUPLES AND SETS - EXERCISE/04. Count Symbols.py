text = input()
occurrences = {}

for element in text:
    if element in occurrences:
        occurrences[element] += 1
    else:
        occurrences[element] = 1

for (key, value) in sorted(occurrences.items()):  #sort by key!!!
    print(f'{key}: {value} time/s')