from nmbrz.sde import Nmbr

"""
Math module for `Nmbr` class

Contains some math functions for calculations
- sigma - iterational sum of function results
- prod - iterational _product_ of function results
- factorial - product of all number from 1 to x
- sin - mathematical sin(alpha) function
"""

# Functions

def sigma(start: int, end: int, func) -> Nmbr:
    result = Nmbr((0, [0], 0))
    for i in range(start, end):
        loop = func(i)
        if loop() == (0, [0], 0):
            continue
        result += loop
    return result
def prod(start: int, end: int, func) -> Nmbr:
    result = Nmbr((1, [1], 0))
    for i in range(start, end):
        loop = func(i)
        if loop() == (0, [0], 0):
            return Nmbr((0, [0], 0))
        result *= loop
    return result
def factorial(a: int):
    if a in [0, 1]:
        return Nmbr((1, [1], 0))
    elif a < 0 or a % 1 != 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return prod(1, a+1, lambda x: Nmbr(x))
def sin(a, terms = 10):
    a = a % (pi * Nmbr(2))
    if a() == (0, [0], 0):
        return Nmbr((0, [0], 0))
    elif a() == (pi / Nmbr(2))():
        return Nmbr((1, [1], 0))
    elif a == pi():
        return Nmbr((0, [0], 0))
    elif a() == (pi * Nmbr(1.5))():
        return Nmbr((-1, [1], 0))
    else:
        def term(x):
            n = int(x)
            return Nmbr(1 if n % 2 == 0 else -1) * (a ** (2*n + 1))/factorial(2*n + 1)
        return sigma(0, terms, term)

# Constants

pi = sigma(
    0, 10, lambda x: Nmbr((-1)**x * 4) / Nmbr(2*x + 1)
)
e = prod(
    0, 10, lambda x: Nmbr(1) + (Nmbr(1)/Nmbr(10))
)
