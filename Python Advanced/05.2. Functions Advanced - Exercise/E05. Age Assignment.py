def age_assignment(*args, **kwargs):
    result = {}
    for person in args:
        result[person] = kwargs[person[0]]
    return result


#test in judge:

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))