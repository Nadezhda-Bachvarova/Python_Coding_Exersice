class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError ('Invalid age value')
        self.__age = age


# Test Code:

person = Person("George", 32)
print(person.get_name())
print(person.get_age())

# Expected Output:

# George
# 20