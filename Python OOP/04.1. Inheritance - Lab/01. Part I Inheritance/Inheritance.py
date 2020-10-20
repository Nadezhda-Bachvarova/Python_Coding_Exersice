#Single Inheritance


class Animal:
    def eat(self):
        return 'eating...'


class Dog(Animal):
    def bark(self):
        return 'barking...'


#Multiple Inheritance


class Person:
    def sleep(self):
        return 'sleeping...'


class Employee:
    def get_fired(self):
        return 'fired...'


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'

#Hierarchical Inheritance


class Animal:
    def eat(self):
        return 'eating...'


class dog(Animal):
    def bark(self):
        return 'barking...'


class Cat(Animal):
    def meow(self):
        return 'meowing...'