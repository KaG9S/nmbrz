# Nmbrz

$\color{yellow}{\text{Improving calculations acuracy with Python.
Smallest module for numbers!}}$

---

- [Nmbrz](#nmbrz)
- [0. How to install](#0-how-to-install)
- [1. Nmbrz module](#1-nmbrz-module)
- [The end](#the-end)

---

# 0. How to install

1. Download the lastest realese from releases page: nmbrz folder or zip-file (unpack it)
2. Move this folder to your local folder (`C:/ProgramFiles/Python/Lib`) or virtual env (`path/to/venv/Lib/site-packages`)
3. Write into your code
```python
from nmbrz import *
```
4. Run. If you got error, reinstall package in other way.
5. Read our [documentation](docs.md).

# 1. Nmbrz module

Using custom class `Nmbr` which can save number in new reprasantation "SDE":

- S - sign: can be 1 if positive; -1 if negative; 0 if number is 0,
- D - digits: list of digits' groops by decimal places
- E - exponent: +1 for every 0 at the end of number until the digits
and -1 for every 0 after comma before digits; 0 if number is 0

Then we got number by `sign * digits * (10 ** Exponent)` and our arguments by `(sign, digits, exponent)`.

For examlpe:

- 1234 = `1 * 1'234 * (10 ** 0)` = `(1, [1, 234], 0)`;
- -0.002 = `-1 * 2 * (10 ** -3)` = `(-1, [2], -3)`;
- 0 = `0 * 0 * (10 ** 0)` = `(0, [0], 0)`;
- -45678900 = `-1 * 456'789 * (10 ** 2)` = `(-1, [456, 789], 2)`.

# The end
Thanks for using my package.
License: [MIT](LICENSE.md)

Contact:
- TG: [@KaG9S](https://t.me/KaG9S)
- Email: jokageogik@gmail.com

Copyright: __C: KaG9S__

Author: @KaG9S

- Documentation: [DOCS.md](md-files/DOCS.md)
- Manifest: [MANIFEST.md](md-files/MANIFEST.md)
- Security policy: [SECURITY.md](md-files/SECURITY.md)
