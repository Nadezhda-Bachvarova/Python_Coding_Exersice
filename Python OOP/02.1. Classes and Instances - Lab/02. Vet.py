class Vet:
    animals = []
    total_space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, name_animal):
        if len(Vet.animals) == Vet.total_space:
            return 'Not enough space'

        self.animals.append(name_animal)
        Vet.animals.append(name_animal)
        return f'{name_animal} registered in the clinic'

    def unregister_animal(self, name_animal):
        if name_animal not in self.animals:
            return f'{name_animal} not in the clinic'

        self.animals.remove(name_animal)
        Vet.animals.remove(name_animal)

        return f'{name_animal} unregistered successfully'

    def info(self):
        animals_count = len(self.animals)
        space_left_in_clinic = Vet.total_space - len(Vet.animals)
        return f'{self.name} has {animals_count} animals. {space_left_in_clinic} space left in clinic'


# Test code:

peter = Vet('Peter')
george = Vet('George')
print(peter.register_animal('Tom'))
print(george.register_animal('Cory'))
print(peter.register_animal('Fishy'))
print(peter.register_animal('Bobby'))
print(george.register_animal('Kay'))
print(george.unregister_animal('Cory'))
print(peter.register_animal('Silky'))
print(peter.unregister_animal('Molly'))
print(peter.unregister_animal('Tom'))
print(peter.info())
print(george.info())

# Expected output:

# Tom registered in the clinic
# Cory registered in the clinic
# Fishy registered in the clinic
# Bobby registered in the clinic
# Kay registered in the clinic
# Cory unregistered successfully
# Silky registered in the clinic
# Molly not in the clinic
# Tom unregistered successfully
# Peter has 3 animals. 1 space left in clinic
# George has 1 animals. 1 space left in clinic


