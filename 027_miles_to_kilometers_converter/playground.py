
def add(*args):
    total = 0
    for x in args:
        total += x
    return total

print(add(7, 13, 204, 1, 10, 100, 45, 83))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
