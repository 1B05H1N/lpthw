## Animal is-a object (yes, sort of confusing) lok at the extra credit
class Animal(object):
    pass
    
## Dog is-a animal class
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
        
## Cat is-a animal class
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name
        
## Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        
## Fish is-a object
class Fish(object):
    pass
    
## Salmon is-a fish
class Salmon(Fish):
    pass
    
## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mart is a person
mary = Person("Mary")

## Mary has-a pet named satan
mary.pet = satan

## Frank is-a employee and has-a salary of 120,000
frank = Employee("Frank", 120000)

## Frank has-a pet named rover
frank.pet = rover

## flippper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()