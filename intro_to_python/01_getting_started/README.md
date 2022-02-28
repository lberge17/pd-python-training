# Intro To Python

## Environment Setup

With Homebrew and [Pyenv](https://github.com/pyenv/pyenv) on MacOS (using zsh)
```bash
$ brew install pyenv
$ pyenv global 3.9.10
$ pyenv versions
$ echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
Close terminal and open a new session.
```bash
$ python --version
```

- [WSL set up](https://www.techtronic.us/install-python-pyenv-on-wsl-ubuntu/) - still untested

- [Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Install PyCharm (alternative to VSCode)](https://www.jetbrains.com/pycharm/download/#section=mac)

## Print Statements
```python
print('Hello World') # prints 'Hello World\n'
print('Hello World', end='') # prints 'Hello World'
print('Hello', 'World') # prints 'Hello World\n'
print('Hello', 'World', sep='') # prints 'HelloWorld\n'
print('Hello', 'World', sep=None) # prints 'Hello World\n'
print('/laura', 'Flatiron', 'lectures', sep='/', end='/*') # prints '/laura/Flatiron/lectures/*'
```

## Variables
- can be any length
- can consist up upper and lowercase letters, digits, and underscores (_)
- variables are case sensitive (name is different from Name)
- variables cannot start with a number
- snake case should be used for functions and variables
- pascal case should be used for class names

```python
x = 10
name = 'Laura'
NAME = 'Berge'
Age = 25
is_19 = False
x, y, z = 4, 2, 19
a = b = c = 'hi'
```

- we can also delete an object
- Note: we can't delete an item within a tuple or string since they are immutables (we'll learn about tuples and strings more later)

```python
num1 = 5
num2 = 6
num3 = 10
del num1
del num2, num3

class ExampleClass:
    # code here

del ExampleClass

example_tuple = (4,2,9)
del example_tuple[1] # Error
del example_tuple # we can delete the tuple itself though
```

## Operators
| Operator | Usage | Example |
| :---: | :---: | :---: |
|  | ARITHMETIC |  |
| + | add | 10 + 5 # => 15 |
| - | subtract | 9 - 3 # => 6 |
| * | multiply | 2 * 4 # => 8 |
| / | divide | 15 / 4 # => 3.75 |
| % | modulus (remainder) | 22 % 6 #=> 4 |
| ** | exponent | 5 ** 7 # => 78125 |
| // | floor divison | 15 / 4 # => 3 |
| | ASSIGNMENT | |
| = | assignment | count = 5 |
| += | reassignment with addition | count += 5 # => 10 |
| -= | reassignment with subtraction | count -= 1 # => 9 |
| *= | reassignment with multiplication | count *= 3 # => 27 |
| /= | reassignment with division | count /= 3 # => 9 |
| %= | reassigment to the remainder | count %= 5 # => 4 |
| **= | reassignment with exponent | count **= 3 # => 64 |
| //= | reassignment with floor division | count //= 7 # => 9 |
|  | COMPARISON |  |
| == | equal to | 4 == 4 # => True |
| != | not equal to | 4 != 4 # => False |
| > | greater than | 10 > 3 # => True |
| < | less than | 82 < 5 # => False |
| <= | less thn or equal to | 10 <= 9 # => False |
| >= | greater than or equal to | 9 >= 9 # => True |
|  | LOGICAL |  |
| and | return first value if falsy else second value | True and 9 # => 9 |
| or | returns first value if truthy else second value | True or 9 # => True |
| not | return True if falsy or False if truthy | not(True and 9) # => False |
|  | MEMBERSHIP |  |
| in | return True/False if value is in second value or not | 'a' in 'Laura' # => True |
| not in | returns opposite of in | 'a' not in 'Laura' # => False |
|  | IDENTITY |  |
| is | used to determine if variables reference the same object | a is b |
| is not | returns opposite boolean of is | a is not b |

- Note: I have not included bitwise operators in this table


## Falsy values

```python
None
False
# Zeros, including:
0
0.0
0j
decimal.Decimal(0)
fraction.Fraction(0, 1)
# Empty sequences and collections, including:
[] - an empty list
{} - an empty dict
() - an empty tuple
'' - an empty str
b'' - an empty bytes
set() - an empty set
# an empty range, like 
range(0)
# objects for which
obj.__bool__() returns False
obj.__len__() returns 0
```

## Functions
- indentation determines end of function ([PEP 8 Python style guide](https://www.python.org/dev/peps/pep-0008/#indentation) says to use 4 spaces for indentation)
- defined using `def` keyword
- should use snake case for name
- can use return keyword to return a value, else will return `None` by default

```python
def function_name(parameters):
    # code here and optional return
# no longer in function
```

- nested functions in Python create closures if they are returned by parent and access a value from outer function's lexical scope

```python
def outer_function(parameters):
    # code here
    def inner_function():
        print(parameters)

    return inner_function

my_closure = outer_function('Hi!!!')
my_closure() # => prints 'Hi!!!'
del outer_function
my_closure() # => prints 'Hi!!!'
```
