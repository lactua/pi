from decimal import Decimal

limit = eval(input('Limit > '))

def sqrt(n):
    return n**Decimal(1/2)

print(2 * sum(sqrt((sqrt(limit**2 - (x + 1)**2) - sqrt(limit**2 - x**2))**2 + 1) for x in range(limit)) / limit)
