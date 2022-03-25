# Object Oriented Programming With Python

## Constructor | Initialize

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

    "Data attributes correspond to “instance variables...Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to.”

```python
    d.age = 12
    d.age
    => 12
```

## Resources

[Classes Python Docs](https://docs.python.org/3/tutorial/classes.html)
