def pretty_result(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Result is {result}"

    return inner


@pretty_result
def a_b(a, b, c, d):
    return a + b + c + d


@pretty_result
def a_mul_b(a, b, c, d):
    return a * b * c * d


def execute(func, func2, *args):
    print(func2(*args))
    return func(*args)


print(execute(a_b, a_mul_b, 1, 2, 3, 4))
print()
print(a_b(2, 2, 2, 2))
print(a_mul_b(2, 9, 3, 2))