# Object Oriented Programming With Python

## Creation of a class Python VS Ruby

```python

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


```

```ruby
class Dog

    def initialize(name)
        @name = name
        @tricks = []
    end

    def add_trick(trick)
        @tricks.append(trick)
    end

end
```

```python
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    d.tricks
    e.tricks
```

```ruby
    d = Dog.new('Fido')
    e = Dog.new('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    d.tricks
    e.tricks
```

> Data attributes correspond to 'instance variables'...
> Data attributes need not be declared; like local variables,
> they spring into existence when they are first assigned to.<sup><a href="https://docs.python.org/3/tutorial/classes.html#instance-objects">1</a></sup>

```python
    d.age = 5
    d.age
    => 5
```

### Instance Variables vs Class Variables

```python
  class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

  >>> d = Dog('Fido')
  >>> e = Dog('Buddy')
  >>> d.kind                  # shared by all dogs
  'canine'
  >>> e.kind                  # shared by all dogs
  'canine'
  >>> d.name                  # unique to d
  'Fido'
  >>> e.name                  # unique to e
  'Buddy'
```

#### Note on Privacy in Python

> "nothing in Python makes it possible to enforce data hiding — it is
> all based upon convention. (On the other hand, the Python
> implementation, written in C, can completely hide implementation
> details and control access to an object if necessary; this can be
> used by extensions to Python written in C.)"

## Instance Methods vs Class Methods

---

### Instance Methods

---

Instance methods work the same as in ruby. You can call them on an instance but cannot call them on a class.

```python
    d.add_trick('roll over')
    => ['roll over', 'roll over']
    Dog.add_trick('roll over')
    => TypeError: add_trick() missing 1 required positional argument: 'trick'
```

- The positional argument missing here is 'self' which does not get sent when you use the function on a class.

> Side note: You can save methods in variables. View the example below!

```python
    df = d.add_trick
    new_tricks = ['Wait', 'Bark', 'Speak', 'Howl', 'Army Crawling', 'Spin', 'Sit Pretty', 'Go and Fetch', 'Stand Tall (On Hind Legs)']

    while len(new_tricks) > 0:
      df(new_tricks.pop())

    d.tricks
    => ['roll over', 'roll over', 'Stand Tall (On Hind Legs)', 'Go and Fetch', 'Sit Pretty', 'Spin', 'Army Crawling', 'Howl', 'Speak', 'Bark', 'Wait']
```

> Wow what a well trained dog. -- @Laura shows her cute dog for moral support!

- We saved a method into df `df = d.add_trick ` then used it in a while loop later on.

- in fact you can also use define a function outside of a class and use it in the definition.

```python
def outer_function(self, a, b):
  return a+b

class C:
  inner_method = outer_function

  def another_method(self):
    return "Goodnight World!"

  method_to_method = another_method

>>> a = C()
>>> a.inner_method(1,2)
3
>>> a.another_method()
'Goodnight World!'
>>> a.method_to_method()
'Goodnight World!'

```

- This was pretty cool, until the documentation said this: `"Note that this practice usually only serves to confuse the reader of a program."`

## Lets talk about self

- You may have noticed that when we defined `d.add_trick(self, name)`it requires two arguments, while when we use it above we only pass it one argument `d.add_trick('roll over')`.
  - The special thing about methods is that the instance object is passed as the first argument in a list of the function.<sup><a href="https://docs.python.org/3/tutorial/classes.html#method-objects">1</a></sup>'
  - Although the first argument that we pass in this method is called self, this is nothing more than a convention. It is similar to Javascript's event, where the event is automatically passed into the first argument of a function. We only call it self for convention and to make the code more readable.

---

### Class Methods

Unlike ruby where we can set class methods using `self.method_name` for python we have to use a built-in function `classmethod()`.

    Syntax: classmethod(function)
    Parameters: accepts a function as a parameter
    Returns: The converted class method.

classmethods can be called by both the class and objects. Similar to class variables. <sup><a href="https://www.geeksforgeeks.org/classmethod-in-python/">2</a></sup>

Lets create a class that uses a class method.

```python

class Flatiron:
  se_managers = ["Ashlee Scott"]
  se_director = "Ashlee Scott"
  def hire(cls):
    if (cls.se_director in cls.se_managers):
      cls.se_managers.append("Laura Berge")
      print("Candidate Hired!")
      cls.se_managers.remove("Ashlee Scott")
    else:
      print("We're okay for now!")
      print(cls.se_managers)

>>> Flatiron.hire = classmethod(Flatiron.hire)
>>> Flatiron.hire()
Candidate Hired!
>>> Flatiron.hire()
"We're okay for now!"
['Laura Berge']

```

This is oddly similar to what we had to do with JS OOP and binding function. Before we invoke a class method we need to bind the class to it using classmethod().

> If you don't bind the class method this is the error you will receive:
>
> > `TypeError: hire() missing 1 required positional argument: 'cls'`

### @classmethod Decorator

A decorator is a function that takes a function as its only parameter and returns a function. <sup><a href="https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/">3</a></sup> We are able to do this because in python we can define a function inside another function and a function can be passed as a parameter to another function.

```python
"""
Note: some of the python documentation refer to functions as fun rather than
func like we are used to.
"""
def decorated_function(callback):
  def add(a,b):
    return a+b

  return sum # here we are return the function sum

@decorate_function
def sum(a,b)
  return (a,b) # def sum(1,2) => (1,2)


"""
The call below is the same thing as if we
passed the function sum(1,2) into the
decorated_function. Making it possible to
call sum directly without the need to
call the decorator function
>>> decorated_function(sum(1,2))
"""
>>> print(sum(1,2))
3

```

Luckily python has a built-in function decorator `@classmethod`.
This comes in really handy when we are talking about classes
because it allows us to be able to skip a step when we are declaring
class methods.

We can now use the decorator for the classmethod like so.

```python

class Flatiron:
  se_managers = ["Ashlee Scott"]
  se_director = "Ashlee Scott"

  @classmethod
  def hire(cls):
    if (cls.se_director in cls.se_managers):
      cls.se_managers.append("Laura Berge")
      print("Candidate Hired!")
      cls.se_managers.remove("Ashlee Scott")
    else:
      print("We're okay for now!")
      print(cls.se_managers)
### NO LONGER NEEDED ###
# >>> Flatiron.hire = classmethod(Flatiron.hire)
### NO LONGER NEEDED ###
>>> Flatiron.hire()
Candidate Hired!
>>> Flatiron.hire()
"We're okay for now!"
['Laura Berge']

```

## Inheritance

Inheritance is handled a bit differently in python. You

```python

class FirstClass:
  data = ["Everyone", "here","is"]

  def add_data(self, new_data):
    self.data.appened(new_data)

class SecondClass(FirstClass):
  def display(self):
    print('Current Data = "%s"' % self.data)


>>> second_instance = SecondClass()
>>> second_instance.display()
Current data = "['Everyone', 'here', 'is']"
>>> second_instance.add_data("awesome")
>>> second_instance.add_data(".")
>>> second_instance.data
['Everyone', 'here', 'is', 'awesome', '.']


```

Importing classes <sup><a href="https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/">4</a></sup>

```python

from module_name import FirstClass

class SecondClass(FirstClass):
  def display(self): ...

---

import module_name

class SecondClass (modulename.FirstClass):
    def display(self): ...

```

---

## Resources

1. [Classes Python Docs](https://docs.python.org/3/tutorial/classes.html)
1. [classmethod() in Python](https://www.geeksforgeeks.org/classmethod-in-python/)
1. [Function Decorators in Python](https://www.geeksforgeeks.org/function-decorators-in-python-set-1-introduction/)
1. [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
1. [Classes Are Customized by Inheritance](https://learning.oreilly.com/library/view/learning-python-5th/9781449355722/ch27s02.html)
