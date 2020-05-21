n = int(input())
numbers = map(int, input().split(' '))
multiplied = map(lambda x: x * n, numbers)
print(*multiplied)