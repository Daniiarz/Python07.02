def factorial(num, m=1):
    if num == 1:
        return m
    print(num, m)
    return factorial(num-1, m*num)


f = factorial(3)
print(f)
