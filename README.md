# Python-Basics

Learning the Syntax of the language, and trying to use it for for side projects.


snake_casing : for naming conventions hehe

#for code comments

- Blocks do not define Scope in Python
- Python does not have switch/case statements
- All functions have a return value, they default to None
- self is used to reference the object itself
- Single Quotes and Double Quotes are both used for Strings, with no special meanings
- Everything is an object

## Python Types

- Strings
- Integers
- Boolean
- Floating Points (Floats)

When using Python with Money you should use something like Decimals and NOT Floats

**example**
```Python
from decimal import *

a = Decimal('.10')
b = Decimal('.10')
x = a + a + a - b
print('x is a {}'.format(x))
print(type(x))
```
