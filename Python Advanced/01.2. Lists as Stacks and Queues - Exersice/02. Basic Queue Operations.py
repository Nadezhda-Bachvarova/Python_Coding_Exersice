from collections import deque

numbers = [int(x) for x in input().split(' ')]
to_queue, to_deque, searched_number = numbers
queue = deque(int(x) for x in input().split(' '))

for _ in range(to_deque):
    queue.popleft()

if searched_number in queue:
    print('True')
else:
    if queue:
        print(min(queue))
    else:
        print(0)