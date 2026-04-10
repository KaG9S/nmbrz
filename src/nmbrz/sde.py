from time import time
from math import floor

class Nmbr:
    """
    A class to represent numbers larger Python's built-in limits.
    The number is represented as a tuple  in new SDE represent system.

    - Sign: 1 for positive, -1 for negative, 0 for zero
    - Digits: list of integers representing the digits of the number
    - Exponent: integer representing the power of 10
    """

    def __init__(self, inp):
        t = type(inp)
        if t in [int, float]:
            if inp == 0:
                self.atr = (0, [0], 0)
            else:
                inp /= (sign := (1 if inp > 0 else -1))
                digits = []
                exponent = 0
                while inp % 1 != 0:
                    inp *= 10
                    exponent -= 1
                if inp >= 1:
                    while inp != 0:
                        digits.append(int(inp % 1000))
                        inp = floor(inp / 1000)
                        exponent += 3
                    inp *= 1000
                    exponent -= 3
                else:
                    while inp != 0:
                        digits.append(int(inp % 1000))
                        inp = floor(inp / 1000)
                        exponent -= 3
                    inp /= 1000
                    exponent += 3
                digits.reverse()
                self.atr = (sign, digits, exponent)

        elif t in [tuple, list]:
            reformat = False
            try: reformat = bool(inp[3])
            except: pass
            if reformat:
                pass
            else:
                assert len(inp) in [3, 4]
                assert inp[0] in [-1, 0, 1]
                assert inp[2] % 1 == 0

            self.atr = inp[:3]

        else:
            raise TypeError("Input must be of type tuple, list, int, or float. Got " + t.__name__)
    def __call__(self):
        return self.atr

    # type conversions
    def __float__(self):
        sign, digits, exponent = self.atr
        if self.atr == (0, [0], 0):
            return 0.0

        num = 0
        for i in range(len(digits)):
            num = num * 1000 + digits[i]
        return float(sign * num * (10 ** exponent))
    def __int__(self):
        return floor(float(self))
    def __str__(self):
        sign, digits, exponent = self()
        if digits == [0]:
            return '0.0E0'
        d = str(digits[0]) + ''.join([f'{g:03d}' for g in digits[1:]])
        if len(d) < 12: d += '0' * (12 - len(d))
        return (('-' if sign == -1 else '') + d[0] + '.' + d[1:12] +
                'E' + ('+' if exponent > 0 else '') + str(exponent))

    # math
    def __add__(self, other):
        if self() == (0, [0], 0):
            return other
        if other() == (0, [0], 0):
            return self

        sa, da, ea = self()
        sb, db, eb = other()
        sc = 1
        ec = min(ea, eb)
        if len(da) >= len(db):
            db = [0]*(len(da) - len(db)) + db
        else:
            da = [0]*(len(db) - len(da)) + da

        dc = [0] * len(da)
        for i in range(len(da)):
            dc[i] = da[i] + db[i]
            if dc[i] >= 1000:
                dc[i] -= 1000
                if i == 0:
                    dc = [0] + dc
                dc[i-1] += 1

        if all([i < 0 for i in dc]):
            sc = -1
            dc = [-i for i in dc]
        ans = Nmbr((sc, dc, ec))
        return ans
    def __sub__(self, other):
        if self() == (0, [0], 0):
            sb, db, eb = other()
            b = Nmbr((-sb, db, eb))
            return b
        elif other() == (0, [0], 0):
            return self

        sb, db, eb = other()
        other = Nmbr((-sb, db, eb))
        ans = self + other
        return ans
    def __mul__(self, other): # not work
        sa, da, ea = self()
        sb, db, eb = other()
        if (0, [0], 0) in [self(), other()]: return Nmbr((0, [0], 0))

        sc = sa * sb
        ec = ea + eb
        x = 1
        for i in db: x *= i
        dc = [i*x for i in da]
        ans = Nmbr((sc, dc, ec))
        return ans
    def __truediv__(self, other): # not work
        sa, da, ea = self()
        sb, db, eb = other()
        if other() == (0, [0], 0):
            raise ZeroDivisionError("Division by zero is not allowed.")
        elif self() == (0, [0], 0):
            return Nmbr((0, [0], 0))

        b_ = 0
        for i in db: b_ += i + b_*(10**3)
        dc = [(i)/b_ for i in da]
        ans = Nmbr((sa/sb, dc, ea - eb))
        return ans
    def __floordiv__(self, other):
        return floor(self / other)
    def __pow__(self, other: float):
        if self() == (0, [0], 0) and other > 0:
            return Nmbr((0, [0], 0))
        elif self() == (0, [0], 0) and other <= 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power.")
        elif other == 0:
            return Nmbr((1, [1], 0))

        sa, da, ea = self()
        if sa < 0 and other % 1 != 0:
            raise ValueError("Negative numbers cannot be raised to a fractional power.")

        sc = sa ** other
        ec = ea * other
        dc = []
        for i in da: dc.append(i ** other)
        ans = Nmbr((sc, dc, ec))
        return ans
    def __mod__(self, other):
        if other() == (0, [0], 0):
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        elif other(1) < 0:
            raise ValueError("Modulo divisor must be a positive number.")
        elif self() == other():
            return Nmbr((0, [0], 0))
        elif self() == (0, [0], 0):
            return Nmbr((0, [0], 0))

        ans = self
        if float(self) < 0:
            while float(ans - other) < 0:
                ans += other
        elif float(self) > 0:
            while float(ans - other) >= 0:
                ans -= other
        return ans

    # comparison
    def __eq__(self, other):
        return self.atr == other.atr
    def __ne__(self, other):
        return self.atr != other.atr
    def __lt__(self, other):
        return float(self) < other.real
    def __le__(self, other):
        return float(self) <= other.real
    def __gt__(self, other):
        return float(self) > other.real
    def __ge__(self, other):
        return float(self) >= other.real

    # iterations
    def __len__(self):
        return len(self.atr[1])+self.atr[2]

    # boolean operations
    def __bool__(self):
        return self.atr != (0, [0], 0)
    def __or__(self, other):
        return any([bool(self), bool(other)])
    def __and__(self, other):
        return all([bool(self), bool(other)])
    def __not__(self):
        return self() == (0, [0], 0)

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        time_taken = end_time - start_time
        str_args = f"{args if args else ''}{', ' if args and kwargs else ''}{kwargs if kwargs else ''}"
        func_repr = f"{func.__name__}({str_args})"
        print(f"Function {func_repr} executed in {time_taken} seconds")
        print("Result:", result)
        return result
    return wrapper
