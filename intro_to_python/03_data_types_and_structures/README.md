# Data Types

## Numbers

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
"Hello World"
'Hello World'
"""Hello World"""
'''hello world'''
```

<hr>

## List

```python
type([]) # => <class 'list'>
type([{'name': 'Laura'}, {'name': 'Kevin'}]) # => <class 'list'>
```

<hr>

## Tuple

```python
type(()) # => <class 'tuple'>
type((1, 'hi', 9.0, {}, [], ())) # => <class 'tuple'>
```

<hr>

## Dictionary

```python
# unordered collection of key-value pairs
type({}) # => <class 'dict'>
type({1: 'L', 2: 'a', 3: 'u', 4: 'r', 5: 'a'}) # => <class 'dict'>
type({'name': 'Laura', 'occupation': 'software engineer'}) # => <class 'dict'>
```

<hr>

## Set

```python
# unordered, iterable, and mutable
# no duplicate items

type(set()) # => <class 'set'>
type(type({'h', 'i'})) # => <class 'set'>
set('hi') # => {'h', 'i'}
set("TeachersTeachingTeachers") # => {'T', 'e', 'r', 'i', 'c', 's', 'a', 'g', 'h', 'n'}
set([6,8,9,3,3]) # => {8, 9, 3, 6}
set([1, 4, 'hello', 4, 3, 'world'])  # => {1, 3, 4, 'hello', 'world'}
```

## Functions

```python
def some_func():
    return 'hi'

type(some_func) # => <class 'function'>
```