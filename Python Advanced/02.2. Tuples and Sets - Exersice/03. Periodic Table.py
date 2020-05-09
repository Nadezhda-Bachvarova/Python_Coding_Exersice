n = int(input())
unique_elements = set()

for _ in range(n):
    elements = set(input().split(' '))
    unique_elements = unique_elements | elements

[print(x) for x in unique_elements]