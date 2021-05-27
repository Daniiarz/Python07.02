class Fraction:

    def __init__(self, num, denum):
        self.num = num
        if denum == 0:
            raise ValueError("Denum can't be 0")
        self.denum = denum

    def add(self, other):
        num = self.num * other.denum + self.denum * other.num
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

    def multiply(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

    def __add__(self, other):
        num = self.num * other.denum + self.denum * other.num
        denum = self.denum * other.denum
        return Fraction(num, denum)

    def __sub__(self, other):
        pass
        # "-"

    def __truediv__(self, other):
        # "/"
        pass

    def __mul__(self, other):
        # "*"
        pass


if __name__ == '__main__':
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)
    f3 = Fraction(2, 3)
    f4 = ((f1 + f1) + f1) + f1
    print(f4.num)
    print(f4.denum)

