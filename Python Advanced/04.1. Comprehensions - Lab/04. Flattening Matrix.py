row_count = int(input())

matrix = [map(int, input().split(', ')) for _ in range(row_count)]

flattened = [num for sublist in matrix for num in sublist]

print(flattened)

#OR (other solution to the same task:


def parse_row(string):
    return map(int, string.split(', '))


row_count = int(input())
matrix = [parse_row(input()) for _ in range(row_count)]
flattened = [num for sublist in matrix for num in sublist]
print(flattened)

