class Human:

    def __init__(self, name, sex, skin_color, race, nation, character):
        self.name = name
        self.sex = sex
        self.skin_color = skin_color
        self.race = race
        self.nation = nation
        self.character = character

    def eat(self):
        return f"{self.name} eating!"

    def drink(self):
        return f"{self.race} {self.sex} drinking!"


h1 = Human('Jibek', 'female', 'white', 'mongoloid', 'kyrgyz', 'worst ever')
h2 = Human('Igor', 'male', 'white', 'mongoloid', 'korean', 'good')
h3 = Human('Aidai', 'female', 'white', 'mongoloid', 'kyrgyz', 'good')

print(h1.eat())
print(h2.eat())
print(h3.eat())

print()

print(h1.drink())
print(h2.drink())
print(h3.drink())


class Animal:

    def __init__(self, species, division, animal_class):
        self.species = species
        self.division = division
        self.animal_class = animal_class

    def eat(self):
        return f"{self.animal_class} eating!"

    def sleep(self):
        return f"{self.animal_class} sleeping!"

    def reproduce(self):
        return f"{self.division} reproducing!"

    def hunt(self):
        if self.species == 'predatory':
            return "hunting"
        else:
            return None


print()
a1 = Animal('pernatye', 'mamals', 'a')
a2 = Animal('predatory', 'cats', 'b')
print(a1.hunt())
print(a2.hunt())

