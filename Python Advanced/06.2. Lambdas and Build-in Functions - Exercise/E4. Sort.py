numbers = map(int, input().split(' '))
negative_numbers = filter(lambda x: x < 0, numbers)
negative_sum = sum(negative_numbers)
print(abs(negative_sum))
