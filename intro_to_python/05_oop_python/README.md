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

## Instance Methods vs Class Methods

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

> Wow what a well trained dog.

- We saved a method into df `df = d.add_trick ` then used it in a while loop later on.

- You may have noticed that when we defined `d.add_trick(self, name)`it requires two arguments, while when we use it above we only pass it one argument `d.add_trick('roll over')`.
  - The special thing about methods is that the instance object is passed as the first argument in a list of the function.<sup><a href="https://docs.python.org/3/tutorial/classes.html#method-objects">1</a></sup>

## Resources

[1. Classes Python Docs](https://docs.python.org/3/tutorial/classes.html)
