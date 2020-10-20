class Lion:
    amount_money = 50

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Lion'

    def get_needs(self):
        return self.amount_money

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Tiger:
    amount_money = 45

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Tiger'

    def get_needs(self):
        return self.amount_money

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Cheetah:
    amount_money = 60

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Cheetah'

    def get_needs(self):
        return self.amount_money

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Keeper:

    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Keeper'

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Caretaker:

    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Caretaker'

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Vet:

    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Vet'

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.type} added to the zoo' #return string name of the class/ or {animal.type} if will add 'self.type = type' in every class
        elif self.__budget < price:
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.type} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        to_pay = sum([worker.salary for worker in self.workers]) #worker is object, we need from salary for every worker is list workers
        if to_pay <= self.__budget:
            self.__budget -= to_pay
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        to_pay = sum([animal.get_needs() for animal in self.animals])
        if to_pay <= self.__budget:
            self.__budget -= to_pay
            return f'You tended all the animals.They are happy.Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ''
        result += f'You have {len(self.animals)} animals\n'
        for animal_type in ('Lion', 'Tiger', 'Cheetah'):
            result += f'----- {len([animal for animal in self.animals if animal.type == animal_type])} {animal_type}s:\n'
            for a in [animal for animal in self.animals if animal.type == animal_type]:
                result += f'{repr(a)}\n'
        return result

    def workers_status(self):
        result = ''
        result += f'You have {len(self.workers)} workers\n'
        for worker_type in ('Keeper', 'Caretaker', 'Vet'):
            result += f'----- {len([worker for worker in self.workers if worker.type == worker_type])} {worker_type}s:\n'
            for w in [worker for worker in self.workers if worker.type == worker_type]:
                result += f'{repr(w)}\n'
        return result


# Test Code:

zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())

# ---------------------------------------------------------

# Expected Output:

# Cheeto the Cheetah added to the zoo
# Cheetia the Cheetah added to the zoo
# Simba the Lion added to the zoo
# Zuba the Tiger added to the zoo
# Tigeria the Tiger added to the zoo
# Not enough space for animal
# John the Keeper hired successfully
# Adam the Keeper hired successfully
# Anna the Keeper hired successfully
# Bill the Caretaker hired successfully
# Marie the Caretaker hired successfully
# Stacy the Caretaker hired successfully
# Peter the Vet hired successfully
# Kasey the Vet hired successfully
# Not enough space for worker
# You tended all the animals. They are happy. Budget left: 1779
# You payed your workers. They are happy. Budget left: 611
# Adam fired successfully
# You have 5 animals
# ----- 1 Lions:
# Name: Simba, Age: 4, Gender: Male
# ----- 2 Tigers:
# Name: Zuba, Age: 3, Gender: Male
# Name: Tigeria, Age: 1, Gender: Female
# ----- 2 Cheetahs:
# Name: Cheeto, Age: 2, Gender: Male
# Name: Cheetia, Age: 1, Gender: Female
# You have 7 workers
# ----- 2 Keepers:
# Name: John, Age: 26, Salary: 100
# Name: Anna, Age: 31, Salary: 95
# ----- 3 Caretakers:
# Name: Bill, Age: 21, Salary: 68
# Name: Marie, Age: 32, Salary: 105
# Name: Stacy, Age: 35, Salary: 140
# ----- 2 Vets:
# Name: Peter, Age: 40, Salary: 300
# Name: Kasey, Age: 37, Salary: 280