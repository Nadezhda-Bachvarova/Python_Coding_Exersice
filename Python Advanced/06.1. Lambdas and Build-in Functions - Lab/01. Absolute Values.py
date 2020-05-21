def abs_func(values):   #First vesion with function
    result = []
    for x in values:
        result.append(abs(x))
    return result

values = list(map(float, input().split()))

print(abs_func(values))

result = list(map(abs, values))   #Second version without function
print(result)   #Test code -> 1 2.5 -3 -4.5