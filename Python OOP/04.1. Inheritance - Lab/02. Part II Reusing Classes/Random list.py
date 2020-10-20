class RandomList(list):
    def get_random_element(self):
        import random
        element = random.choice(self)
        self.remove(element)
        return element


random_list = RandomList()
[random_list.append(x) for x in range(15)]


print(random_list.get_random_element())
print(random_list.get_random_element())
print(random_list.get_random_element())
print(random_list)
