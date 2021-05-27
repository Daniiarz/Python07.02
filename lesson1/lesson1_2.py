class Home:

    def __init__(self, door, windows, area, height, rooms):
        self.door = door
        self.windows = windows
        self.area = area
        self.height = height
        self.rooms = rooms


n = Home("Black", "White", 51, 2.85, 2)
aidia_house = Home("Green", "Black", 60, 2.1, 10)
igor = Home("Brown", "Brown", 5, 3, 2)
temirlan = Home("Red", "Pink", 1000, 3, 60)
mirlan = Home("Black", "White", 100, 3, 4)
print(n.door)
print(aidia_house.door)
print(igor.door)
print(temirlan.door)
print(mirlan.door)
print()
print(n.height)
print(aidia_house.height)
print(igor.height)
print(temirlan.height)
print(mirlan.height)
print()
print(type(n))