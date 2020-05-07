numbers = [int(x) for x in input().split()]
to_push, to_pop, searched_number = numbers

elements = [int(x) for x in input().split()]

[elements.pop() for _ in range(to_pop)]

if searched_number in elements:
    print('True')
else:
    if elements:
        print(min(elements))
    else:
        print(0)