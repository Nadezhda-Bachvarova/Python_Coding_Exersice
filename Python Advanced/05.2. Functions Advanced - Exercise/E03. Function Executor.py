def func_executor(*args):
    result = []
    for arg in args:
        func = arg[0]
        params = arg[1]
        result.append(func(*params))
    return result

#test my func with functions in judge sistem:


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))