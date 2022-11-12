x = lambda a, b : a + b
print(x(2,3))

squire = lambda a: a * a
print(squire(10))


def dual(n):
    return lambda a: a * n

double = dual(10)
print(double(3))

cars = ["Ford", "Volvo", "BMW"]

print(cars)