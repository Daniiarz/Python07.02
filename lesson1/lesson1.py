l = [1, 2, 3, 4, 5]
# for i in range(10):
#     print(i)
#
# d = 10
# print()
# while d > 0:
#     print(d)
#     d -= 1


def a_b(a, b):
    # print(a+b)
    return a + b


n1 = a_b(a=2, b=2)
n2 = a_b(a=n1, b=2)
n3 = a_b(a=n2, b=2)
print(n3)
print()


def c_d(a, *args, **kwargs):
    print(a)
    print(*args)
    print(kwargs)
    pass


print()
user = {'name': "Damiiar", "surname": "M"}
n4 = c_d(9, 1, 1, c=1, b=1, **user)
n5 = "My name is Jibek"
n6 = [1, 2, 3, 4, 5]
print(n5[6:9])
print(n6[1:3])
