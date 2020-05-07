def solve(values):
    occurrences = {}
    for value in values:
        if value not in occurrences:
            occurrences[value] = 0
        occurrences[value] += 1
    for number, count in occurrences.items():
        print(f'{number} - {count} times')


values_strings = input().split(' ') #test code: -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
values = [float(x) for x in values_strings]
solve(values)