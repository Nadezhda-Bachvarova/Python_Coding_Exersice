def read_matrix():
    rows_count, columns_count = [int(x) for x in input().split(" ")]
    _matrix = [list(map(int, input().split(" "))) for _ in range(rows_count)]
    return _matrix


def find_best_sub_matrix(best_matrix):
    rows_count = len(best_matrix)
    columns_count = len(best_matrix[0])

    _best_sum = None
    best_start = None

    for row in range(rows_count - 2):
        for col in range(columns_count - 2):
            current_sum = best_matrix[row][col] + \
                          best_matrix[row][col + 1] + best_matrix[row][col + 2] + \
                          best_matrix[row + 1][col] + \
                          best_matrix[row + 1][col + 1] + best_matrix[row + 1][col + 2] + \
                          best_matrix[row + 2][col] + best_matrix[row + 2][col + 1] + best_matrix[row + 2][col + 2]

            if _best_sum:
                if _best_sum < current_sum:
                    _best_sum = current_sum
                    best_start = (row, col)
            else:
                _best_sum = current_sum
                best_start = (row, col)
    row, col = best_start
    _best_sub_matrix = [
        [best_matrix[row][col], best_matrix[row][col + 1], best_matrix[row][col + 2]],
        [best_matrix[row + 1][col], best_matrix[row + 1][col + 1], best_matrix[row + 1][col + 2]],
        [best_matrix [row + 2][col], best_matrix[row + 2][col + 1], best_matrix [row + 2][col + 2]]
    ]
    return _best_sum, _best_sub_matrix


def print_matrix(best_sum_, best_sub_matrix_):
    print(f'Sum = {best_sum_}')
    for row in best_sub_matrix_:
        print(' '.join([str(num) for num in row]))


matrix = read_matrix()
best_sum, best_sub_matrix = find_best_sub_matrix(matrix)
print_matrix(best_sum, best_sub_matrix)
