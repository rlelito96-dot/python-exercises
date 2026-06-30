
class Animal():
    counter = 0
    animals_list = []

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

        Animal.animals_list.append(self)
        Animal.counter += 1

    def sleep(self):
        print("To zwierze śpi.")

    def wake_up(self):
        print("To zwierze wstalo.")

    def eat(self, food):
        self.food = food
        print("To zwierze je", food)
        self.weight += 1

        self.stop_eating()

    def stop_eating(self):
        print("To zwierze przestalo jesc", self.food)

    def make_sound(self):
        print("To zwierze daje glos.")

class Bird(Animal):
    def __init__(self, weight, age, can_fly):
        super().__init__(age, weight)

        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            print("Ten ptak potrafi latac.")
        else:
            print("Ten ptak nie potrafi latać.")


    def make_sound(self):
        print("Ten ptak śpiewa.")


class Mammal(Animal):
    def __init__(self, weight, age, can_swim):
        super().__init__(weight, age)

        self.can_swim = can_swim

    def swim(self):
        if self.can_swim:
            print("Ten ssak potrafi plywac.")
        else:
            print("ten ssak nie potrafi plywać.")

    def make_sound(self):
        print("Ten ssak daje glos.")

class Dog(Mammal):
    def __init__(self, weight, age, can_swim, breed):
        super().__init__(weight, age, can_swim)

        self.breed = breed


    def fetch(self):
        print("Ten pies potrafi aportować.")

    def make_sound(self):
        print("Ten pies szczeka.")

class Cat(Mammal):
    def __init__(self, weight, age, can_swim, breed):
        super().__init__(weight, age, can_swim)

        self.breed = breed

    def make_sound(self):
        print("Ten kot miauczy.")



animal = Animal(20, 20)
bird = Bird(2,4,True)
mammal = Mammal(14,10, False)
dog = Dog(2, 2, False, "bulldog")
cat = Cat(4,8,True, "Maine coon")

for animal in Animal.animals_list:
    animal.swim()