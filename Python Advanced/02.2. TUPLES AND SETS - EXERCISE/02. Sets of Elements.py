n, m = [int(x) for x in input().split(' ')]
set_1 = set()
set_2 = set()

for _ in range(n):
    number = int(input())
    set_1.add(number)

for _ in range(m):
    number = int(input())
    set_2.add(number)

intersection_set = set_1 & set_2

[print(x) for x in intersection_set]
