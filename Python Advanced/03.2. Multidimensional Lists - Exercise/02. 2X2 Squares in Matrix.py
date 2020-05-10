rows_count, cols_count = [int(x) for x in input().split()]
matrix = []
counter = 0

for _ in range(rows_count):
    matrix.append(input().split())

for row in range(rows_count - 1):
    for col in range(cols_count - 1):
        left_up = matrix[row][col]
        right_up = matrix[row][col + 1]
        left_down = matrix[row + 1][col]
        right_down = matrix[row + 1][col + 1]
        if left_up == right_up == left_down == right_down:
            counter += 1

print(counter)