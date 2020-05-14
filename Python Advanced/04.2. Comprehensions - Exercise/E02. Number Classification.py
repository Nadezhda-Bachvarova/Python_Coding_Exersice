numbers = [int(x) for x in input().split(', ')]

positive = [str(x) for x in numbers if x >= 0]
negative = [str(x) for x in numbers if x < 0]
even = [str(x) for x in numbers if x % 2 == 0]
odd = [str(x) for x in numbers if x % 2 != 0]

print(f'Positive: {", ".join(positive)}\nNegative: {", ".join(negative)}\nEven: {", ".join(even)}\nOdd: {", ".join(odd)}')