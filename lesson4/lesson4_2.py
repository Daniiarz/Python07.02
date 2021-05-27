class Parent:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


reagan = Parent("Reagan", None)
g_h_bush = Parent("G. H. Bush", reagan)
clinton = Parent("Clinton", g_h_bush)
g_w_bush = Parent("G. W. Bush", clinton)
obama = Parent("Obama", g_w_bush)
trump = Parent("Trump", obama)

trump2 = Parent("Trump 2", trump)
biden = Parent("Biden", trump)


person = trump

# while person.parent is not None:
#     print(person.name)
#     person = person.parent
#
# print(person.name)


def get_parents(parent):
    if parent.parent is None:
        return
    print(parent.name)
    return get_parents(parent.parent)


get_parents(person)
