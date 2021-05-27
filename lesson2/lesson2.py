class Animal:

    def __init__(self, color, sex, klass):
        self.color = color
        self.sex = sex
        self.klass = klass


class Neko(Animal):

    def __init__(self, color, sex, klass, ear_size, fur, eye_color):
        super(Neko, self).__init__(color, sex, klass)
        self.ear_size = ear_size
        self.fur = fur
        self.eye_color = eye_color


class Dog(Animal):

    def __init__(self, color, sex, klass, tail_size, paroda, size):
        super(Dog, self).__init__(color, sex, klass)
        self.tail_size = tail_size
        self.paroda = paroda
        self.size = size


class Alabai(Dog):

    def __init__(self, color, sex, klass, tail_size, paroda, size, name):
        super(Alabai, self).__init__(color, sex, klass, tail_size, paroda, size)
        self.name = name


n1 = Neko("grey", "male", "cats", 5, "long", "green")
d1 = Dog("black", "female", "dog", 10, "pitbul", "small")
d2 = Dog("yellow", "male", "dog", 5, "chi hua", "big")
a1 = Alabai("white with black dots", "male", "dog", 5, "alabai", "small", "rex")
print(a1.name)
print(a1.paroda)
print(a1.sex)
print(a1.color)
