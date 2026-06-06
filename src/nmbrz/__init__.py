#!/workspaces/nmbrz/.venv/bin/python

"""
# Number representation module
Read more [here](https://github.com/KaG9S/nmbrz)
"""

from nmbrz.sde import Nmbr

def test():
    s = Nmbr(2) + Nmbr((1, [2], 0))
    assert s == Nmbr(4)
test()

version = ((0, 2), "stable", 'v0.2')

# version: v0.2
# Copyright: KaG9S/nmbrz 2026 MIT
