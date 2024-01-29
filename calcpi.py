from decimal import Decimal
from time import time

limit = eval(input('Limit > '))

def chronometer(func):
    def wrapper(*args, **kwargs):
        before = time()
        _return = func(*args, **kwargs)
        after = time()
        
        return (after - before, _return)
    return wrapper

def sqrt(n):
    return n**Decimal(1/2)

@chronometer
def calc():
    f = lambda x: sqrt((sqrt(limit**2 - (x + 1)**2) - sqrt(limit**2 - x**2))**2 + 1)

    _sum = 0
    for x in range(limit):
        _sum += f(x)
        print("{}%".format(round((x+1)/limit*100)), end="\r")

    return 2 * _sum / limit

duration, result = calc()
print(f"approximation : {result}")
print(f"took {round(duration, 2)} seconds")
