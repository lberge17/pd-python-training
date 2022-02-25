# Python Debugger - pdb

## Getting Started

[Python Debugger Docs](https://docs.python.org/3/library/pdb.html)

```python
import pdb

def some_function():
    pdb.set_trace()
```

```python
def some_function():
    import pdb; pdb.set_trace()
```

```python
# Python 3.7 and beyond
def some_function():
    breakpoint()
```

## Navigating pdb

- You can use `q(uit)`, `exit` to quit the pdb session
- Use `c(ontinue)` to continue rest of program (or to hit the next breakpoint)
- Use `s(tep)` to execute the next line of code.
- Use `n(ext)` to execute the next line in the current function (more limited/specific than `step`)
- Use `r(eturn)` to execute the rest of the current function until the return value
- Use `unt(il) [line number]` if you are in an iteration and want to stop hitting the same breakpoint as you iterate but continue running the program. Also can give an optional line number argument and program with run until that line.
- To print inside debugger, you can use `p 'hello'`
- [more fun ways to use pdb](https://www.codementor.io/@stevek/advanced-python-debugging-with-pdb-g56gvmpfa)

```python
def my_function():
    print('hi')
    breakpoint()
    print('bye')

my_function
```

```bash
$ python ./intro_to_python/02_debugging_in_python/using_debugger.py
hi
> /Users/laura/Flatiron/pd/pd-python-training/intro_to_python/02_debugging_in_python/using_debugger.py(4)my_function()
-> print("bye")
(Pdb) q



$ python ./intro_to_python/02_debugging_in_python/using_debugger.py
hi
> /Users/laura/Flatiron/pd/pd-python-training/intro_to_python/02_debugging_in_python/using_debugger.py(4)my_function()
-> print("bye")
(Pdb) p 'hi'
'hi'
(Pdb) c
bye
```
