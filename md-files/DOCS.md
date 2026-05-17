# Full documetation for [Nmbrz](README.md) module

---

- [Full documetation for Nmbrz module](#full-documetation-for-nmbrz-module)
- [0. Install](#0-install)
- [1. SDE and nmbr's](#1-sde-and-nmbrs)
  - [1.1. Start](#11-start)
  - [1.2. Operations](#12-operations)
    - [1.2.0 Type convertions](#120-type-convertions)
    - [1.2.1. Math](#121-math)
    - [1.2.2. Iterations](#122-iterations)
    - [1.2.3. Comparison](#123-comparison)
    - [1.2.4. Bool operations](#124-bool-operations)
- [2. Mth module](#2-mth-module)
  - [2.1. Function usage](#21-function-usage)
  - [2.2. Constants' formulas](#22-constants-formulas)

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

## 1.2. Operations

Now we can do almost anything with your nmbr (we will call "nmbr" any number with SDE repr).

### 1.2.0 Type convertions

These nmbr's can be coverted in to:

- int - just floor of starter number
- float - starter number
- bool - checks if != 0 like int or float
- str - representation like:
```python
>>>print(Nmbr(math.pi))
3.141592653589E+0
```


### 1.2.1. Math

For examlpe here some operators for math:

```python
n1 + - * / % // n2
n1 ** float
```

### 1.2.2. Iterations

So how you remember, we have S**D**E *(D - digits)*, and this is list, so we can read it, get length and change some elements

```python
len(n1) # digits decimal places
_ = n1[0]
n1[i] = 0
```

### 1.2.3. Comparison

Like greater, smaller, equals, not equals ect.
* all from float(n) conv or n() call

```python
n1 == != < > <= >= n2
```

### 1.2.4. Bool operations

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
