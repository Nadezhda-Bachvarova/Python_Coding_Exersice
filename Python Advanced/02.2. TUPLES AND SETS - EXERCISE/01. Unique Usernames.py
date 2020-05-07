n = int(input())
unique_name = set()

for _ in range(n):
    username = input()
    unique_name.add(username)

[print(x) for x in unique_name]