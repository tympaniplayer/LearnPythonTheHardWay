## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## Dog is an Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has a name
        self.name = name


## Cat is an Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has a name
        self.name= name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## Person has a name

        ## Person has a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## Call the super class constructor passing in name
        ## Employee has a name because it is a person
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

# Halibut is fish
class Halibut(Fish):
    pass

## rover is a dog
rover = Dog("Rover")

## Sata is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## mary has a pet which is Satan
mary.pet = satan

## frank is an employee, who is also a person
frank = Employe("Frank", 120000) #who also makes  a nice salary

## frank has a pet who happens to be rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a Salmon and fish
crouse = Salmon()

## harry is a Halibut and Fish
harry = Halibut()
