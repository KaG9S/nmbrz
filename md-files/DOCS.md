# Full documetation for [Nmbrz](README.md) module

---

Table of contents:

0. [Install](#0-install)
1. [SDE and nmbr's](#1-sde-and-nmbrs)
  1. [Start](#11-start)
  2. [Type convertions](#120-type-convertions)
  3. [Math](#121-math)
  4. [Iterations](#122-iterations)
  5. [Comparison](#123-comparison)
  6. [Boolean operations](#124-boolean-operations)
2. [Mth module](#2-mth-module)
  1. [Function usage](#21-function-usage)
  2. [Constants' formulas](#22-constants-formulas)
3. [UTILS](#3-utils)
  1. [Files](#31-files)
  2. [Docs](#32-docs-for-utils)

---

# 0. Install

So, to start your jorney by this module, first you need to install it.
We've already told about this in [README](README.md) (0. How to install).
To check if everything runs properly, run:

```python
from nmbrz import *
# this will import the Nmbr class and test()
```

If there is no errors, then program can work with it now.

# 1. SDE and nmbr's

[SDE](src/nmbrz/sde.py) is module with `Nmbr` class which can save very big or small numbers in different fractions' length and powers

## 1.1. Start

So, you have already imported module. If not, write this:
```python
from nmbrz import *
```

To init some new numbers, write this
```python
NEW_NMBR_NUMBER = Nmbr(YOUR_START_NUMBER)
```


Now we can do almost anything with your nmbr (we will call "nmbr" any number with SDE repr).

## 1.2 Type convertions

These nmbr's can be coverted in to:

- int - just floor of starter number
- float - starter number
- bool - checks if != 0 like int or float
- str - representation like:
```python
>>>print(Nmbr(math.pi))
3.141592653589E+0
```

## 1.3. Math

For examlpe here some operators for math:

```python
n1 + - * / % // n2
n1 ** float
```

## 1.4. Iterations

So how you remember, we have S**D**E *(D - digits)*, and this is list, so we can read it, get length and change some elements

```python
len(n1) # digits decimal places
_ = n1[0]
n1[i] = 0
```

## 1.5. Comparison

Like greater, smaller, equals, not equals ect.
* all from float(n) conv or n() call

```python
n1 == != < > <= >= n2
```

## 1.6. Boolean operations

All from `bool()` convertion

```python
n1 and or n2
not n1 # if n == 0
```

---

# 2. Mth module

So there is module named [mth](src/nmbrz/mth.py) (short of "math"), which contains some functions:

- sigma: $\sum$
- product (prod): $\prod$
- factorial: $x!$
- trigonometric sin: $\sin()$

and constants:

- pi: $\pi \approx 3.1415...$
- Euler`s number: $e\approx 2.718...$ 

## 2.1. Function usage

1. sigma
```python
pi = mth.sigma(
    0, # start
    10, # end (skip this iter)
    lambda x: Nmbr((-1)**x * 4) / Nmbr(2*x + 1)
    # function for each iter, where int(x) is iterator
)
```
2. prod
```python
e = mth.prod(
    0, # start
    10, # end (skip this iter)
    lambda x: Nmbr(1) + (Nmbr(1)/Nmbr(10))
    # function for each iter, where int(x) is iterator
)
```
3. factorial
```python
>>>print(int(mth.factorial(10)))
3628800
```
4. sin
```python
>>>print(float(mth.sin(mth.pi)))
1.0
```

## 2.2. Constants' formulas

1. pi:

$\pi=\sum_{i}^{n}{\frac{(-1)^{i}*4}{2i+1}}$

2. e (Eulers number):

$e=(1+\frac{1}{n})^{n}$

# 3. UTILS

There is the folder (i will take [__init__.py](../src/nmbrz/utils/__init__.py) as a reference) named `utils`, because there're can be a lot of utilites for nmbrz package like: timer, [SOME USEFUL UTILS HERE], etc.

## 3.1. Files

This [folder](../src/nmbrz/utils/) is root for this module.

Tree:
- [`__init__.py`](../src/nmbrz/utils/__init__.py):
  initalisation for module
- [`__main__.py`](../src/nmbrz/utils/__main__.py):
  some small utils for nmbrz work

## 3.2. Docs for utils

I don't know where to put a large documentation file for this module, so it will be [here](utils.md).

