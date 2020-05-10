def sum_elements(list_in_matrix):
    the_sum = 0
    for x in list_in_matrix:
        the_sum += x
    return the_sum


def sum_matrix(matrix):
    the_sum = 0
    row_count = len(matrix)

    for row_index in range(row_count):
        the_sum += sum_elements(matrix[row_index])
    return the_sum


matrix = [
    [7, 1, 3, 3, 2, 1],

    [1, 3, 9, 8, 5, 6],

    [4, 6, 7, 9, 1, 0],
]

print(sum_matrix(matrix))