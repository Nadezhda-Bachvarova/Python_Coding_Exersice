n = int(input())
best_intersection = set()

for _ in range(n):
    ranges = input().split('-')
    first_range = [int(x) for x in ranges[0].split(',')]   #[0, 3]
    second_range = [int(x) for x in ranges[1].split(',')]  #[1, 2]
    first_set = set([x for x in range(first_range[0], first_range[1] + 1)])
    second_set = set([x for x in range(second_range[0],second_range[1] + 1)])
    intersection = first_set & second_set
    if len(intersection) > len(best_intersection):
        best_intersection = intersection

print(f'Longest intersection is {list(best_intersection)} with length {len(best_intersection)}')