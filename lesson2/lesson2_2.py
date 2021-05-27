class Bird:

    def __init__(self, size, feather, color):
        self.size = size
        self.feather = feather
        self.color = color

    def fly(self):
        return "Bird flying!"

    def eat(self):
        return "Eating"


class Parrot(Bird):

    def __init__(self, size, feather, color, can_talk, can_fly):
        super(Parrot, self).__init__(size, feather, color)
        self.can_talk = can_talk
        self.can_fly = can_fly

    def fly(self):
        return "Parrot flying!"

    def talk(self):
        return "Parrot is talking"


class Kakadu(Parrot):

    def __init__(self, size, feather, color, can_talk, can_fly, hair_style):
        super(Kakadu, self).__init__(size, feather, color, can_talk, can_fly)
        self.hair_style = hair_style

    def fly(self):
        return "Kakadu flying"


class AraKakadu(Kakadu):

    def __init__(self, size, feather, color, can_talk, can_fly, hair_style, pattern):
        super(AraKakadu, self).__init__(size, feather, color, can_talk, can_fly, hair_style)
        self.pattern = pattern

    def talk(self):
        if self.can_talk:
            return "AraKakadu can talk"
        else:
            return "AraKakadu can't talk"


k1 = Kakadu(15, 'long', 'black', True, True, 'bold')
print(k1.fly())
ar1 = AraKakadu(15, 'long', 'black', False, True, 'bold', "rainbow")
print(ar1.talk())
print(ar1.eat())
