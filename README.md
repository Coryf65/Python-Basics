# Python-Basics

Learning the Syntax of the language, and trying to use it for for side projects.

snake_casing : for naming conventions hehe

```#for code comments```

- Blocks do not define Scope in Python
- Python does not have switch/case statements
- All functions have a return value, they default to None
- self is used to reference the object itself
- Single Quotes and Double Quotes are both used for Strings, with no special meanings
- Everything is an object

## Python Types

- Strings
```Python
x = 'Hello Github'
```

- Integers
```Python
x = 65
```

- Boolean, True and False
```Python
x = True
```

- Floating Points (Floats)
```Python
x = 100.0022001
```

- None (like NULL or NOTHING)
```Python
x = None
```
- Lists
```Python
x = [ 1, 2, 3, 4, 5 ]
```

- Tuples, Immutable (cannot change once initialized)
```Python
x = ( 1, 2, 3, 4, 5 )
```

- Dictionary, Key Value Pair
```Python
x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
```

### When using Python with Money you should use something like Decimals and NOT Floats

**example**
```Python
from decimal import *

a = Decimal('.10')
b = Decimal('.10')
x = a + a + a - b
print('x is a {}'.format(x))
print(type(x))
```

What evaluates as False ?

- 0
- ""
- None


## Cool Stuff

- You can check an objects uniqye ID by calling id(*object*)

*example*
```Python
a = (1, 'two', 3.0, [4, 'four'], 5)
print(f'x is {a}')
print(id(a)) # id(object) Returns an Unique ID for given object
```
