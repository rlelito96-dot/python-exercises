
class Animal:
    counter = 0
    animals_list = []


    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

        Animal.counter += 1
        Animal.animals_list.append(self)

    def sleep(self):
        print("To zwierze spi")

    def wake_up(self):
        print("To zwierze wstało")

    def eat(self, food):
        self.food = food
        print("To zwierze je", self.food)
        self.weight += 1

        self.stop_eating()

    def stop_eating(self):
        print("To zwierze przestało jesc", self.food)

    def make_sound(self):
        print("To zwierze daje głos")

class Bird(Animal):
    def __init__(self, weight, age, can_fly):
        super().__init__(weight, age)

        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print("Ten ptak potrafi latac")
        else:
            print("Ten ptak nie potrafi latac")

    def make_sound(self):
        print("Ten ptak spiewa")

class Mammal(Animal):
    def __init__(self, weight, age, can_swim):
        super().__init__(weight, age)

        self.can_swim = can_swim

    def swim(self):
        if self.can_swim:
            print("Ten ssak potrafi pływać")
        else:
            print("Ten ssak nie potrafi pływać")

    def make_sound(self):
        print("Ten ssak daje glos")

class Dog(Mammal):
    def __init__(self, weight, age, can_swim, breed):
        super().__init__(weight, age, can_swim)

        self.breed = breed

    def fetch(self):
        print("Ten pies potrafi aportowac")

    def make_sound(self):
        print("Ten pies szczeka")

class Cat(Mammal):
    def __init__(self, weight, age, can_swim, breed):
        super().__init__(weight, age, can_swim)

        self.breed = breed

    def make_sound(self):
        print("Ten kot miauczy")

animal = Animal(6, 10)
bird = Bird(2, 8, True)
mammal = Mammal(8,12, False)
dog = Dog(4, 2, True, "Bulldog")
cat = Cat(5, 8, True, "Anubis")

for animal in Animal.animals_list:
    animal.make_sound()


