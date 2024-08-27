def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(add(1, 2, 3, 4))

def calcutate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calcutate(2, add=3, multiply = 5)