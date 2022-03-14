# Data Types

## Numbers
Immutables.

### Integer

```python
type(26) # => <class 'int'>
```

### Float

```python
type(-20.0) # => <class 'float'>
```

### Complex Number

```python
# [real] + [imaginary]j
type(63 + 5j) # => <class 'complex'>
```

<hr>

## Boolean

```python
type(True) # => <class 'bool'>
type(False) # => <class 'bool'>
```

<hr>

## String

```python
# immutable sequence of Unicode code points
"Hello World"
'Hello World'
"""Hello World"""
'''hello world'''
```

<hr>

## List

```python
# mutable, ordered list

type([]) # => <class 'list'>
type([{'name': 'Laura'}, {'name': 'Kevin'}]) # => <class 'list'>
```

<hr>

## Tuple

```python
# immutable sequence of objects.
# more memory and time efficient than lists

type(()) # => <class 'tuple'>
type((1, 'hi', 9.0, {}, [], ())) # => <class 'tuple'>
```

<hr>

## Dictionary

```python
# mutable, unordered collection of key-value pairs

type({}) # => <class 'dict'>
type({1: 'L', 2: 'a', 3: 'u', 4: 'r', 5: 'a'}) # => <class 'dict'>
type({'name': 'Laura', 'occupation': 'software engineer'}) # => <class 'dict'>
```

<hr>

## Set

```python
# unordered, iterable, and mutable
# no duplicate items
# two types: `set` and `frozenset`
# note: `frozenset`s are actually immutable

type(set()) # => <class 'set'>
type(type({'h', 'i'})) # => <class 'set'>
set('hi') # => {'h', 'i'}
set("TeachersTeachingTeachers") # => {'T', 'e', 'r', 'i', 'c', 's', 'a', 'g', 'h', 'n'}
set([6,8,9,3,3]) # => {8, 9, 3, 6}
set([1, 4, 'hello', 4, 3, 'world'])  # => {1, 3, 4, 'hello', 'world'}
```

<hr>

## Functions

```python
# functions are objects in Python
# can be passed as a callback

def some_func():
    return 'hi'

type(some_func) # => <class 'function'>
```