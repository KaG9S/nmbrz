from nmbrz.sde import Nmbr

class Array:
    def __init__(self, inp):
        t = type(inp)

        if t == Array:
            inp = inp()

        elif t == list:
            for i in inp:
                if type(i) != Nmbr:
                    raise TypeError("All elements should be \"Nmbr\" type.")

        elif t == tuple:
            if len(inp) == 1:
                inp = [Nmbr(0)]*inp[0]
            elif len(inp) == 2:
                if type(inp[1]) != Nmbr:
                    raise TypeError("All elements can only be Nmbr")
                inp = [inp[1]]*inp[0]
            else:
                raise ValueError(f"Can't create a Array with this tuple input: {str(inp)}.")

        else:
            raise ValueError(f"Can't create a Array with this input: {str(inp)}.")

        # if no errors -> then all good

        self.data = inp
        self.l = len(inp)
    def __call__(self):
        ret = [i for i in self.data]
        return ret

    # math
    def __add__(self, other):
        if type(other) == Array:
            if len(self) == len(other):
                return Array([self[i]+other[i] for i in range(len(self))])
            else:
                return Array(self.data + other.data)
        elif type(other) == Nmbr:
            return Array([i+other for i in self])
        else:
            raise TypeError(f"Can't add object ({type(other)}) to array")
    def __sub__(self, other):
        if type(other) == Nmbr:
            return Array([i-other for i in self])
        else:
            raise TypeError(f"Can't add object ({type(other)}) to array")
    def __mul__(self, other):
        if type(other) == Nmbr:
            return Array([i*other for i in self.data])
        elif type(other) == Array:
            raise Exception("Matrix is not released yet")

            m = [[self[x]*other[y] for x in range(len(self))] for y in range(len(self))]
            return Matrix(m)
    def __truediv__(self, other):
        return Array([i/other for i in self])
    def __floordiv__(self, other):
        return Array([i//other for i in self])

    # items
    def __len__(self):
        return self.l
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value

    # bools
    def __not__(self):
        return self.data != []
    def __and__(self, other):
        return bool(self) and bool(other)
    def __or__(self, other):
        return bool(self) or bool(other)
