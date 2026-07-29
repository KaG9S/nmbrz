class Nmbr:
    """
    A class to represent numbers larger Python's built-in limits.
    The number is represented as a tuple  in new SDE represent system.

    - Sign: 1 for positive, -1 for negative, 0 for zero
    - Digits: list of integers representing the digits of the number
    - Exponent: integer representing the power of 10
    """

    base = 3

    def __init__(self, inp):
        t = type(inp)

        if t in [int, float]:
            atr = (0, [0], 0)
            if inp != 0:
                inp /= (sign := (1 if inp > 0 else -1))
                digits = []
                exponent = 0
                while inp % 1 != 0:
                    inp *= 10
                    exponent -= 1
                while inp != 0:
                    digits.append(int(inp % 10**Nmbr.base))
                    inp = int(inp / 10**Nmbr.base)
                    exponent += 3
                inp *= 10**Nmbr.base
                exponent -= 3
                digits.reverse()
                atr = (sign, digits, exponent)

        elif t in [tuple, list]:
            assert len(inp) == 3
            assert inp[0] in [-1, 0, 1]
            assert type(inp[1]) == list
            assert inp[2] % 1 == 0

            if type(inp) == tuple: inp = [inp[0], inp[1], inp[2]]

            cycle = 0

            while cycle < len(inp[1]):
                inp, cycle = reformat(cycle, inp)
                cycle += 1
            while len(inp[1]) > 1 and inp[1][0] == 0:
                inp[1] = inp[1][1:]
            while len(inp[1]) > 1 and inp[1][-1] == 0:
                inp[1] = inp[1][:-1]
                inp[2] += 3

            inp = tuple(inp[0:3])

        else:
            raise TypeError("Input must be of type tuple, list, int, or float. Got " + t.__name__)

        self.atr = atr
    def __call__(self):
        return self.atr

    # type conversions
    def __float__(self):
        sign, digits, exponent = self.atr
        if self.atr == (0, [0], 0):
            return 0.0
        num = 0
        for i in range(len(digits)): num = num * 10**Nmbr.base + digits[i]
        return float(sign * num * (10 ** exponent))
    def __int__(self):
        return int(float(self))
    def __str__(self):
        sign, digits, exponent = self()
        if digits == [0]: return '0.0E0'
        d = str(digits[0]) + ''.join([str(g) for g in digits[1:]])
        if len(d) < 12: d += '0' * (12 - len(d))
        return (('-' if sign == -1 else '') + d[0] + '.' + d[1:12] +
                'E' + ('+' if exponent > 0 else '') + str(exponent))

    # math
    def __add__(self, other):
        if self() == (0, [0], 0): return other
        if other() == (0, [0], 0): return self
        if self()[0] == other()[0] and self()[0] == -1:
            return -((-self) + (-other))

        sa, da, ea = self()
        sb, db, eb = other()
        sc = 1
        ec = min(ea, eb)
        sa = sa / ec
        sb = sb / ec

        da = [i*(10**( 3-(eb-ec)%3 )) for i in da]
        it = 0
        while it < len(da): da[it], it = reformat(it, da)
        db = [i*(10**( 3-(ea-ec)%3 )) for i in db]
        it = 0
        while it < len(db): da[it] = reformat(it, db)

        da = [0]*(eb-ec) + da
        db = [0]*(ea-ec) + db

        db = db + [0]*(len(da)-len(db))
        da = da + [0]*(len(db)-len(da))

        dc = []
        for i in range(len(da)): dc.append((da[i]*sa + db[i]*sb)/sa)

        ans = Nmbr((sc, dc, ec))
        return ans
    def __sub__(self, other):
        if self() == (0, [0], 0): return -other
        elif other() == (0, [0], 0): return self
        return self + (-other)
    def __mul__(self, other):
        if self() == (0, [0], 0) or \
        other() == (0, [0], 0): return Nmbr((0, [0], 0))

        sa, da, ea = self()
        sb, db, eb = other()

        sc = sa * sb
        ec = ea + eb
        x = 1
        for i in db: x *= i
        dc = [i*x for i in da]
        ans = Nmbr((sc, dc, ec))
        return ans
    def __truediv__(self, other):
        if other() == (0, [0], 0): raise ZeroDivisionError("Division by zero is not allowed.")
        elif self() == (0, [0], 0): return Nmbr((0, [0], 0))

        sa, da, ea = self()
        sb, db, eb = other()
        b_ = 0
        for i in db: b_ += i + b_*(10**Nmbr.base)
        dc = [(i)/b_ for i in da]
        ans = Nmbr((sa/sb, dc, ea - eb))
        return ans
    def __floordiv__(self, other):
        res = self / other
        return res - (res % Nmbr(1))
    def __pow__(self, other: float):
        if self() == (0, [0], 0) and other > 0: return Nmbr((0, [0], 0))
        elif self() == (0, [0], 0) and other <= 0: raise ZeroDivisionError("0 cannot be raised to a negative power.")
        elif other == 0: return Nmbr((1, [1], 0))

        sa, da, ea = self()
        if sa < 0 and other % 1 != 0: raise ValueError(
            "Negative numbers cannot be raised to a fractional power."
        )

        sc = sa ** other
        ec = ea * other
        dc = []
        for i in da: dc.append(i ** other)
        ans = Nmbr((sc, dc, ec))
        return ans
    def __mod__(self, other):
        if other() == (0, [0], 0): raise ZeroDivisionError("Modulo by zero is not allowed.")
        elif other()[0] == -1: raise ValueError("Modulo divisor must be a positive number.")
        elif self() == other(): return Nmbr((0, [0], 0))
        elif self() == (0, [0], 0): return Nmbr((0, [0], 0))

        ans = self
        if self()[0] == -1:
            while (ans - other)()[0] == 1: ans += other
        elif self()[0] == 1:
            while (ans - other)()[0] == 1: ans -= other
        return ans
    def __neg__(self):
        s, d, e = self()
        return Nmbr((-s, d, e))

    # comparison
    def __eq__(self, other):
        return self.atr == other.atr
    def __ne__(self, other):
        return self.atr != other.atr
    def __lt__(self, other): # main compare
        return (self-other)()[0] == -1
    def __le__(self, other):
        return self < other or self == other
    def __gt__(self, other):
        return other < self
    def __ge__(self, other):
        return other < self or other == self

    # iterations
    def __len__(self):
        return len(self.atr[1])+self.atr[2]

    # boolean operations
    def __bool__(self):
        return self.atr != (0, [0], 0)
    def __or__(self, other):
        return bool(self) or bool(other)
    def __and__(self, other):
        return bool(self) and bool(other)
    def __not__(self):
        return not bool(self)

def reformat(i: int, inp):
    l = inp[1]
    if l[i] % 1 != 0:
        if i == len(l) - 1:
            l.append(0)
            inp[2] -= 1
        l[i+1] += int((l[i] % 1) * 10**Nmbr.base)
        l[i] //= 10**Nmbr.base
        inp[1] = l
        reformat(i+1, inp)
    if l[i] != l[i] % 10**Nmbr.base:
        if i == 0:
            l = [0] + l
        l[i-1] += l[i] // 10**Nmbr.base
        l[i] %= 10**Nmbr.base
        inp[1] = l
        reformat(0, inp)
    inp[1] = l
    return (inp, i)
