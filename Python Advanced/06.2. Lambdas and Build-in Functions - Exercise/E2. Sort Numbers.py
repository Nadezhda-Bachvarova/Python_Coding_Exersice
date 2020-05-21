#test_code = nuGosho 7 10 St20amat Pesho 3 47

line = input().split(' ')
numbers_as_strins = filter(lambda x: x.isdigit(), line)
numbers = filter(lambda x: x > len(line), map(int, numbers_as_strins))
sorted_numbers = sorted(numbers)
print(*sorted_numbers)