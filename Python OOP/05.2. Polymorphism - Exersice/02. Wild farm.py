from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        pass


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 0.25
            self.food_eaten += food.quantity
        else:
            return f'Owl does not eat {food.__class__.__name__}!'

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        pass


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if food.__class__.__name__ in ('Vegetable', 'Fruit'):
            self.weight += food.quantity * 0.10
            self.food_eaten += food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region},{self.food_eaten}]'


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__ (name, weight, living_region)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 0.40
            self.food_eaten += food.quantity
        else:
            return f'Dog does not eat {food.__class__.__name__}!'

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.living_region}, {self.weight}, {self.food_eaten}]'


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        if food.__class__.__name__ in ('Meat', 'Vegetable'):
            self.weight += food.quantity * 0.40
            self.food_eaten += food.quantity
        else:
            return f'Cat does not eat {food.__class__.__name__}!'

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.living_region}, {self.weight}, {self.food_eaten}]'


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 1
            self.food_eaten += food.quantity
        else:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.living_region}, {self.weight}, {self.food_eaten}]'


# Test Code:

owl = Owl('Pip', 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

# Expected output:

# Owl [Pip, 10, 10, 0]
# Hoot Hoot
# Owl does not eat Vegetable!
# Owl [Pip, 10, 11.0, 4]


# Test Code:

hen = Hen('Harry', 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

print(type(hen).__name__)

# Expected output:

# Hen [Harry, 10, 10, 0]
# Cluck
# Hen [Harry, 10, 13.15, 9]

