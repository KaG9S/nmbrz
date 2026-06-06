from nmbrz.sde import Nmbr

class Array:
    def __init__(self, inp):
        self.data = inp
        self.l = len(inp)
    def __call__(self):
        return self.data

    def __add__(self, other):
        if type(other) == Array:
            return Array(self.data + other.data)
        else:
            return Array([i*other for i in self])
    def __sub__(self, other):
        return self + (-other)
    def __mul__(self, other):
        if type(other) == Nmbr:
            return Array([i*other for i in self.data])
        elif type(other) == Array:
            m = [[self[x]*other[y] for x in range(len(self))] for y in range(len(self))]
            return Matrix(m)
    def __truediv__(self, other):
        return Array([i/other for i in self])
    def __floordiv__(self, other):
        return Array([i//other for i in self])

    def __len__(self):
        return self.l
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value

class Matrix:
    def __init__(self, inp):
        t = type(inp)

        if t == Matrix:
            self = inp
            x, y = inp.x, inp.y
            t0 = inp.t0

        elif t == list:
            t0 = type(inp[0][0])
            if not t0 in [int, float, Nmbr]:
                raise TypeError(
                    "Elements can only be these types: int, float, Nmbr"
                )
            y = len(inp[0])
            x = len(inp)
            for i in inp:
                if y != len(i):
                    raise ValueError(
                        "all rows in matrix need to be same lenght"
                    )
                for j in i:
                    if t0 != type(j):
                        raise TypeError(
                            "all elements need to be the same type: int, float, Nmbr"
                        )

            # if no errors -> then all good

        elif t == tuple:
            assert inp[0] > 0 and inp[1] > 0
            if len(inp) == 2:
                inp = [[Nmbr(0) for y in range(inp[1])] for x in range(inp[0])]
                t0 = Nmbr
            elif len(inp) == 3:
                inp = [[inp[2] for y in range(inp[1])] for x in range(inp[0])]
                t0 = type(inp[2])
                if not t0 in [int, float, Nmbr]:
                    raise TypeError(
                        "Elements can only be these types: int, float, Nmbr"
                    )
            else:
                raise ValueError(
                    f"can't create matrix with these params: {inp.get(0, None)}x{inp.get(1, None)}" + (f", zero: {str(inp.get(2, None))}" if len(inp) >= 3 else '')
                )
            x, y = len(inp), len(inp[0])

        elif t == str:
            inp = inp.split('x')
            x, y, t0 = int(inp[0]), int(inp[1]), Nmbr
            inp = [[t0(0) for i in range(y)] for j in range(x)]

        else:
            raise ValueError(
                f"can't create matrix with these params: {str(inp)}"
            )

        self.data: list[list] = inp
        self.x, self.y = x, y
        self.t = t0

