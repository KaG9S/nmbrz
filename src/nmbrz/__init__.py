#!/workspaces/nmbrz/.venv/bin/python

"""
Number representation module
"""

from nmbrz.sde import Nmbr

def test():
    s = Nmbr(2) + Nmbr((1, [2], 0))
    assert s == Nmbr(4)
test()
