from collections import deque

n = int(input())
petrol_pumps = deque()
index = 0
diff = 0

for i in range(n):
    pump = [int(x) for x in input().split()]
    fuel, distance = pump
    diff = fuel - distance
    petrol_pumps.append(diff)

for i in range(len(petrol_pumps) - 1):
    if petrol_pumps[i] < 0:
        index = i + 1
    if petrol_pumps[i] > 0:
        petrol_pumps[i + 1] = petrol_pumps[i] + petrol_pumps[i + 1]

print(index)