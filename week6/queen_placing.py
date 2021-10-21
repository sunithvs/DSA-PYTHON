class Animal:
    def __init__(self, name, legs, owner):
        self.name = name
        self.legs = legs
        self.owner = owner
        self.describe()

    def say_hi(self):
        print(f"animal name is {self.name}")

    def describe(self):
        print(f"animal name is {self.name}\n it has {self.legs} legs and its owner is {self.owner}")


class Dog(Animal):

    def __init__(self, name, legs, owner, a, breed):
        self.amount = a
        self.breed = breed
        super(Dog, self).__init__(name, legs, owner)
        self.bark()

    # def __str__(self):
    #     return f"name:{self.name}\nbreed:{self.breed}\n cash:{self.amount}\nowner {self.owner}"

    def bark(self):
        print("bow now bow")


class Shapered(Dog):
    def __init__(self, name, legs, owner, a, breed, color):
        self.color = color
        super().__init__(name, legs, owner, a, breed)
